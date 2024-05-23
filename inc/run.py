#!/usr/bin/env python
# coding=utf-8
   ################
  #   AabyssZG   #
 #    Fkalis    #
################

import itertools
from inc import output, console
import requests, sys, random, json
from tqdm import tqdm
from termcolor import cprint
from time import sleep
import requests.packages.urllib3
import time
import asyncio
import aiohttp

requests.packages.urllib3.disable_warnings()

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"
]

def JSON_handle(header1, header2):
    dict1 = json.loads(str(header1).replace("'", "\""))
    dict2 = json.loads(str(header2).replace("'", "\""))
    # Merge two dictionaries
    merged_dict = {**dict1, **dict2}
    # Convert the merged dictionary to a JSON string
    result_json = json.dumps(merged_dict, indent=2)
    return result_json

def url(urllist, proxies, header_new):
    with open("urlout.txt", "wb+"):
        pass
    cprint("====== Starting SpringBoot information leakage endpoint test for target URL ======", "cyan")
    sleeps = input("\nDo you want to delay the scan (default 0 seconds): ")
    if sleeps == "":
        sleeps = int("0")
    with open("Dir.txt", 'r') as web:
        webs = web.readlines()
        for web in webs:
            web = web.strip()
            u = urllist + web
            header = {"User-Agent": random.choice(ua)}
            newheader = json.loads(str(JSON_handle(header, header_new)).replace("'", "\""))
            try:
                requests.packages.urllib3.disable_warnings()
                r = requests.get(url=u, headers=newheader, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
                sleep(int(float(sleeps)))
                if r.status_code == 503:
                    sys.exit()
                if (r.status_code == 200 and 'need login' not in r.text and 'Forbidden' not in r.text and len(r.content) != 3318 and 'No access' not in r.text and 'Authentication failed' not in r.text):
                    cprint("[+] Status code %d" % r.status_code + ' ' + "Information leakage URL: " + u + '    ' + "Page length: " + str(len(r.content)), "red")
                    with open("urlout.txt", "a") as f2:
                        f2.write(u + '\n')
                elif r.status_code == 200:
                    cprint("[+] Status code %d" % r.status_code + ' ' + "but unable to get information URL: " + u + '    ' + "Page length: " + str(len(r.content)), "magenta")
                else:
                    cprint("[-] Status code %d" % r.status_code + ' ' + "Unable to access URL: " + u, "yellow")
            except KeyboardInterrupt:
                print("Process manually terminated with Ctrl + C")
                sys.exit()
            except Exception as e:
                cprint("[-] URL " + u + " is actively rejecting requests, skipping!", "magenta")
    count = len(open("urlout.txt", 'r').readlines())
    if count >= 1:
        print('\n')
        cprint("[+][+][+] Found SpringBoot sensitive information leakage in target URL, exported to urlout.txt with %d records" % count, "red")
    else:
        print('\n')
        cprint("[-] No SpringBoot sensitive information leakage found in target URL", "yellow")
    sys.exit()

def get_file(filename):
    with open(filename, 'r') as temp:
        temps = temp.readlines()
        for urls in temps:
            yield urls.strip()

async def async_dir(url, proxies, header_new, semaphore, sleeps):
    try:
        tasks = []
        u_list = []
        with open("Dir.txt", 'r') as web:
            web_lines = web.readlines()
            for web_line in web_lines:
                web_line = web_line.strip()
                if '://' not in url:
                    url = "http://" + url
                if url[-1] != "/":
                    u = url + "/" + web_line
                else:
                    u = url + web_line
                u_list.append(u)
        tasks = [asyncio.create_task(file_semaphore(u_dir, proxies, header_new, semaphore, sleeps)) for u_dir in u_list]
        result = await asyncio.gather(*tasks)
    except Exception as e:
        for task in tasks:
            if not task.cancelled():
                task.cancel()
        cprint("[-] URL " + url + " is actively rejecting requests, skipping!", "magenta")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

async def file(u, proxies, header_new):
    header = {"User-Agent": random.choice(ua)}
    newheader = json.loads(str(JSON_handle(header, header_new)).replace("'", "\""))
    async with aiohttp.ClientSession() as session:
        async with session.get(url=u, headers=newheader, proxy=proxies, timeout=6, allow_redirects=False, ssl=False) as r:
            conntext = await r.text()
            if (r.status == 200 and 'need login' not in conntext and 'Forbidden' not in conntext and len(conntext) != 3318 and 'No access' not in conntext and 'Authentication failed' not in conntext):
                cprint("[+] Status code %d" % r.status + ' ' + "Information leakage URL: " + u + '    ' + "Page length: " + str(len(conntext)), "red")
                with open("output.txt", "a") as f2:
                    f2.write(u + '\n')
            elif r.status == 200:
                cprint("[+] Status code %d" % r.status + ' ' + "but unable to get information URL: " + u + '    ' + "Page length: " + str(len(conntext)), "magenta")
            else:
                cprint("[-] Status code %d" % r.status + ' ' + "Unable to access URL: " + u, "yellow")

async def file_semaphore(url, proxies, header_new, semaphore, sleeps):
    async with semaphore:
        await file(url, proxies, header_new)
        await asyncio.sleep(int(sleeps))

async def file_main(urlfile, proxies, header_new):
    urls_lists = []
    with open("output.txt", "wb+"):
        pass
    cprint("====== Starting SpringBoot information leakage endpoint test for target TXT ======", "cyan")
    time_start = time.time()
    sleeps = input("\nDo you want to delay the scan (default no delay, must be an integer): ")
    if sleeps == "":
        sleeps = "0"
    else:
        sleeps = int(sleeps)
    max_concurrency = input("Enter maximum concurrency (default 10): ")
    if max_concurrency == "":
        max_concurrency = 10
    else:
        max_concurrency = int(max_concurrency)
    max_tasks = 100
    semaphore = asyncio.Semaphore(max_concurrency)
    urls_itr = get_file(urlfile)
    while True:
        try:
            urls_lists = list(itertools.islice(urls_itr, max_tasks))
            if not urls_lists:
                break
            tasks = [async_dir(url, proxies, header_new, semaphore, sleeps) for url in urls_lists]
            await asyncio.gather(*tasks)
        except StopIteration:
            break
    count = len(open("output.txt", 'r').readlines())
    if count >= 1:
        print('\n')
        cprint("[+][+][+] Found SpringBoot sensitive information leakage in target TXT, exported to output.txt with %d records" % count, "red")
    else:
        print('\n')
        cprint("[-] No SpringBoot sensitive information leakage found in target TXT", "yellow")
    time_end = time.time()
    time_sum = time_end - time_start
    cprint("[+] Batch scan took %s seconds" % time_sum, "red")
    sys.exit()

def dump(urllist, proxies, header_new):
    def download(url: str, fname: str, proxies: str, newheader):
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(url, headers=newheader, timeout=6, stream=True, verify=False, proxies=proxies)
        total = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
                desc=fname,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)

    cprint("====== Starting SpringBoot sensitive file leakage test and download for target URL ======", "cyan")
    url1 = urllist + "actuator/heapdump"
    url2 = urllist + "heapdump"
    url3 = urllist + "heapdump.json"
    url4 = urllist + "gateway/actuator/heapdump"
    url5 = urllist + "hystrix.stream"
    url6 = urllist + "artemis-portal/artemis/heapdump"
    header = {"User-Agent": random.choice(ua)}
    newheader = json.loads(str(JSON_handle(header, header_new)).replace("'", "\""))

    try:
        if str(requests.head(url1)) != "<Response [200]>":
            cprint("[-] No heapdump sensitive file leakage found at /actuator/heapdump", "yellow")
        else:
            url = url1
            cprint("[+][+][+] Found heapdump sensitive file leakage at /actuator/heapdump" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "heapdump", proxies, newheader)
            sys.exit()
        if str(requests.head(url2)) != "<Response [200]>":
            cprint("[-] No heapdump sensitive file leakage found at /heapdump", "yellow")
        else:
            url = url2
            cprint("[+][+][+] Found heapdump sensitive file leakage at /heapdump" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "heapdump", proxies, newheader)
            sys.exit()
        if str(requests.head(url3)) != "<Response [200]>":
            cprint("[-] No heapdump sensitive file leakage found at /heapdump.json", "yellow")
        else:
            url = url3
            cprint("[+][+][+] Found heapdump sensitive file leakage at /heapdump.json" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "heapdump.json", proxies, newheader)
            sys.exit()
        if str(requests.head(url4)) != "<Response [200]>":
            cprint("[-] No heapdump sensitive file leakage found at /gateway/actuator/heapdump", "yellow")
        else:
            url = url4
            cprint("[+][+][+] Found heapdump sensitive file leakage at /gateway/actuator/heapdump" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "heapdump", proxies, newheader)
            sys.exit()
        if str(requests.head(url5)) != "<Response [401]>" and str(requests.head(url5)) != "<Response [200]>":
            cprint("[-] No hystrix monitoring data file leakage found at /hystrix.stream, please verify manually", "yellow")
        else:
            url = url5
            cprint("[+][+][+] Found hystrix monitoring data file leakage at /hystrix.stream" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "hystrix.stream", proxies, newheader)
            sys.exit()
        if str(requests.head(url6)) != "<Response [200]>":
            cprint("[-] No heapdump monitoring data file leakage found at /artemis-portal/artemis/heapdump, please verify manually", "yellow")
        else:
            url = url6
            cprint("[+][+][+] Found heapdump monitoring data file leakage at /artemis-portal/artemis/heapdump" + ' ' + "Download endpoint URL: " + url, "red")
            download(url, "heapdump", proxies, newheader)
            sys.exit()
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] Download failed, please try to download manually")
        sys.exit()

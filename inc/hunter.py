#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

import requests, sys, json, re, random, base64
from termcolor import cprint
from time import sleep
import urllib3
urllib3.disable_warnings()

def JSON_load(text):
    json_str = text
    data = json.loads(json_str)
    if data["data"]["arr"]:
        # Extract IP and port information
        ip_port_list = [match["url"] for match in data["data"]["arr"]]
    else:
        cprint("[-] No assets found. Please check if your syntax is correct", "yellow")
        sys.exit()
    # Print extracted information
    for service in ip_port_list:
        outurl = str(service)
        with open("hunterout.txt", "a") as f2:
            f2.write(str(outurl) + '\n')
        print(f"Service: {outurl}")

def Key_Download(key, proxies, choices, searchs):
    cprint("====== Downloading data via Hunter API key ======", "green")
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    pagesys = choices % 20
    pageszc = choices // 20
    pages = pageszc + 1 if pagesys > 0 else pageszc
    for i in range(1, pages + 1):
        page_url = "&page=" + str(i)
        keyurl = f"https://hunter.qianxin.com/openApi/search?api-key={key}&search={searchs}&page_size=20&is_web=1"
        download_url = keyurl + page_url
        cprint(f"[+] Attempting to download page {i} data", "red")
        try:
            requests.packages.urllib3.disable_warnings()
            download_response = requests.get(url=download_url, headers=Headers, timeout=10, verify=False, proxies=proxies)
            if "\"code\":200" in str(download_response.text):
                JSON_load(download_response.text)
                cprint("-" * 45, "red")
                sleep(2)
            else:
                cprint(f"[-] API returned status code {download_response.status_code}", "yellow")
                cprint("[-] Please refer to the official manual based on the returned status code: https://hunter.qianxin.com/home/helpCenter?r=5-1-1", "yellow")
        except KeyboardInterrupt:
            print("Process manually terminated with Ctrl + C")
            sys.exit()
        except Exception as e:
            print(e)
            print("[-] An error occurred, logged in error.log\n")
            with open("error.log", "a") as f2:
                f2.write(str(e) + '\n')

def Key_Test(key, proxies, choices, searchs):
    cprint("====== Testing your Hunter API key ======", "green")
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    keytest_url = f"https://hunter.qianxin.com/openApi/search?api-key={key}&search=dGl0bGU9IuWMl-S6rCI=&page=1&page_size=10&is_web=1"
    try:
        requests.packages.urllib3.disable_warnings()
        test_response = requests.get(url=keytest_url, headers=Headers, timeout=10, verify=False, proxies=proxies)
        data = json.loads(test_response.text)
        recode = data["code"]
        if str(recode) == "200":
            cprint("[+] Your key is valid, test successful!", "red")
            rest_quota = data["data"]["rest_quota"]
            cprint(f"[+] {rest_quota}", "red")
            sleep(2)
            Key_Download(key, proxies, choices, searchs)
        else:
            cprint(f"[-] API returned status code {recode}", "yellow")
            cprint("[-] Please refer to the official manual based on the returned status code: https://hunter.qianxin.com/home/helpCenter?r=5-1-1", "yellow")
            sys.exit()
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def HunterDownload(key, proxies):
    cprint("====== Starting Hunter API interface for Spring asset mapping ======", "green")
    cprint(f'[+] Your Hunter API key: {key}', "green")
    try:
        choices = input("\n[.] Enter the number of assets to map (default 100): ")
        if choices == '':
            choices = "100"
        elif int(choices) <= 0:
            print("Please do not enter a negative number")
            sys.exit()
        choices = int(choices)
    except Exception:
        print("Please do not enter meaningless strings")
        sys.exit()
    search = input("[.] Enter the mapping query (default app.name=\"Spring Whitelabel Error\"): ")
    if search == "":
        searchs = str("YXBwLm5hbWU9IlNwcmluZyBXaGl0ZWxhYmVsIEVycm9yIg==")
    else:
        search = base64.urlsafe_b64encode(search.encode("utf-8")).decode('utf-8')
        searchs = str(search)
    with open("hunterout.txt", "wb+"):
        pass
    Key_Test(key, proxies, choices, searchs)
    count = len(open("hunterout.txt", 'r').readlines())
    if count >= 1:
        cprint(f"[+][+][+] Exported Hunter asset results to hunterout.txt with {count} records", "red")
    sys.exit()

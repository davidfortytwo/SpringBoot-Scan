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
    # Extract IP and port information
    ip_port_list = [service[0] for service in data["results"]]
    # Print extracted information
    if ip_port_list == []:
        cprint("[-] No assets found. Please check if your syntax is correct", "yellow")
        sys.exit()
    for service in ip_port_list:
        if ("https" not in service):
            service = "http://" + service
        outurl = str(service)
        with open("fofaout.txt", "a") as f2:
            f2.write(str(outurl) + '\n')
        print(f"Service: {outurl}")

def Key_Download(key, proxies, choices, searchs):
    cprint("====== Downloading data via Fofa API key ======", "green")
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    pagesys = (choices % 100)
    pageszc = (choices // 100)
    pages = pageszc + 1 if pagesys > 0 else pageszc
    for i in range(1, pages + 1):
        page_url = "&page=" + str(i)
        keyurl = "https://fofa.info/api/v1/search/all?&key=" + key + "&qbase64=" + str(searchs)
        download_url = keyurl + page_url
        cprint(f"[+] Attempting to download page {i} data", "red")
        try:
            requests.packages.urllib3.disable_warnings()
            download_response = requests.get(url=download_url, headers=Headers, timeout=10, verify=False, proxies=proxies)
            if "\"error\":false" in str(download_response.text):
                JSON_load(download_response.text)
                cprint("-" * 45, "red")
            else:
                cprint(f"[-] API returned status code {download_response.status_code}", "yellow")
                cprint("[-] Please refer to the official manual based on the returned status code: https://fofa.info/api", "yellow")
        except KeyboardInterrupt:
            print("Process manually terminated with Ctrl + C")
            sys.exit()
        except Exception as e:
            print("[-] An error occurred, logged in error.log\n")
            with open("error.log", "a") as f2:
                f2.write(str(e) + '\n')

def Key_Test(key, proxies, choices, searchs):
    cprint("====== Testing your Fofa API key ======", "green")
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    keytest_url = "https://fofa.info/api/v1/info/my?key=" + key
    try:
        requests.packages.urllib3.disable_warnings()
        test_response = requests.get(url=keytest_url, headers=Headers, timeout=6, verify=False, proxies=proxies)
        data = json.loads(test_response.text)
        if data["error"] == 0:
            username = str(data["username"])
            cprint(f"[+] Your key is valid, test successful! Your account is {username}", "red")
            if data["isvip"] == 1:
                cprint("[+] Your account is a VIP member", "red")
            else:
                cprint("[.] Your account is not a VIP member", "yellow")
            Key_Download(key, proxies, choices, searchs)
        else:
            apierror = data["errmsg"]
            cprint(f"[-] An error occurred, API returned: {apierror}", "yellow")
            cprint("[-] Please refer to the official manual based on the returned result: https://fofa.info/api", "yellow")
            sys.exit()
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def FofaDownload(key, proxies):
    cprint("====== Starting Fofa API interface for Spring asset mapping ======", "green")
    cprint(f'[+] Your Fofa API key: {key}', "green")
    try:
        choices = input("\n[.] Enter the number of assets to map (default 100): ")
        if choices == '':
            choices = 100
        elif int(choices) <= 0:
            print("Please do not enter a negative number")
            sys.exit()
        choices = int(choices)
    except Exception:
        print("Please do not enter meaningless strings")
        sys.exit()
    search = input("[.] Enter the mapping query (default icon_hash=\"116323821\"||body=\"Whitelabel Error Page\"): ")
    if search == "":
        searchs = str("aWNvbl9oYXNoPSIxMTYzMjM4MjEifHxib2R5PSJXaGl0ZWxhYmVsIEVycm9yIFBhZ2Ui")
    else:
        searchs = base64.b64encode(search.encode("utf-8")).decode('utf-8')
    with open("fofaout.txt", "wb+"):
        pass
    Key_Test(key, proxies, choices, searchs)
    count = len(open("fofaout.txt", 'r').readlines())
    if count >= 1:
        cprint(f"[+][+][+] Exported Fofa asset results to fofaout.txt with {count} records", "red")
    sys.exit()

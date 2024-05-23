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
    ip_port_list = [(match["portinfo"]["hostname"], match["portinfo"]["service"], match["ip"], match["portinfo"]["port"]) for match in data["matches"]]
    if not ip_port_list:
        cprint("[-] No assets found. Please check your query syntax.", "yellow")
        sys.exit()
    # Print extracted information
    for hostname, service, ip, port in ip_port_list:
        if "https" in service:
            service = "https://"
        else:
            service = "http://"
        if hostname:
            outurl = f"{service}{hostname}:{port}"
        else:
            outurl = f"{service}{ip}:{port}"
        with open("zoomout.txt", "a") as f2:
            f2.write(f"{outurl}\n")
        print(f"Service: {outurl}")

def Key_Download(key, proxies, choices, searchs):
    cprint("====== Downloading data using ZoomEye API key ======", "green")
    Headers = {
        "API-KEY": key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    pages = (choices + 19) // 20  # Calculate the number of pages needed
    for i in range(1, pages + 1):
        page_url = f"&page={i}"
        keyurl = f"https://api.zoomeye.org/host/search?query={searchs}&t=web"
        downloadurl = keyurl + page_url
        cprint(f"[+] Attempting to download data from page {i}", "red")
        try:
            requests.packages.urllib3.disable_warnings()
            download_response = requests.get(url=downloadurl, headers=Headers, timeout=6, verify=False, proxies=proxies)
            if download_response.status_code in [200, 201]:
                JSON_load(download_response.text)
                cprint("-" * 45, "red")
            else:
                cprint(f"[-] API returned status code {download_response.status_code}", "yellow")
                cprint("[-] Please refer to the official documentation: https://www.zoomeye.org/doc", "yellow")
        except KeyboardInterrupt:
            print("Process terminated manually with Ctrl + C")
            sys.exit()
        except Exception as e:
            print("[-] An error occurred. Logged in error.log\n")
            with open("error.log", "a") as f2:
                f2.write(str(e) + '\n')

def Key_Test(key, proxies, choices, searchs):
    cprint("====== Testing ZoomEye API key ======", "green")
    Headers = {
        "API-KEY": key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    keytesturl = "https://api.zoomeye.org/host/search?query=app:\"Spring Framework\"&page=1"
    try:
        requests.packages.urllib3.disable_warnings()
        test_response = requests.get(url=keytesturl, headers=Headers, timeout=6, verify=False, proxies=proxies)
        if test_response.status_code in [200, 201]:
            cprint("[+] Your key is valid, test successful!", "red")
            Key_Download(key, proxies, choices, searchs)
        else:
            cprint(f"[-] API returned status code {test_response.status_code}", "yellow")
            cprint("[-] Please refer to the official documentation: https://www.zoomeye.org/doc", "yellow")
            sys.exit()
    except KeyboardInterrupt:
        print("Process terminated manually with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred. Logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def ZoomDownload(key, proxies):
    cprint("====== Initiating ZoomEye interface for Spring asset mapping ======", "green")
    cprint(f'[+] Your ZoomEye API key: {key}', "green")
    try:
        choices = input("\n[.] Enter the number of assets to map (default is 100): ")
        if choices == '':
            choices = "100"
        elif int(choices) <= 0:
            print("Please do not enter a negative number")
            sys.exit()
        choices = int(choices)
    except Exception:
        print("Please do not enter meaningless strings")
        sys.exit()
    search = input("[.] Enter the query statement (default is app:\"Spring Framework\"): ")
    if not search:
        searchs = "app:\"Spring Framework\""
    else:
        searchs = search
    with open("zoomout.txt", "wb+"):
        pass
    Key_Test(key, proxies, choices, searchs)
    count = len(open("zoomout.txt", 'r').readlines())
    if count >= 1:
        cprint(f"[+][+][+] ZoomEye asset mapping results exported to zoomout.txt, total {count} records", "red")
    sys.exit()

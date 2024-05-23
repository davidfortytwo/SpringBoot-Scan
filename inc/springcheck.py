#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, run, vul, console
import requests, sys, hashlib, json
from termcolor import cprint
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def Spring_Check(url, proxies, header_new):
    cprint("[.] Performing Spring fingerprint recognition", "cyan")
    Spring_hash = "0488faca4c19046b94d07c3ee83cf9d6"
    Paths = ["favicon.ico", "AabyssZG666"]
    for path in Paths:
        test_url = str(url) + path
        r = requests.get(test_url, timeout=10, verify=False, headers=header_new, proxies=proxies)
        try:
            content_type = r.headers.get("Content-Type", "")
            if "image" in content_type or "octet-stream" in content_type:
                favicon_hash = hashlib.md5(r.content).hexdigest()
                if favicon_hash == Spring_hash:
                    cprint("[+] The site's favicon is a Spring icon, recognition successful", "red")
                    break
            elif r.text and ('timestamp' in r.text):
                cprint("[+] The site's error content matches Spring characteristics, recognition successful", "red")
                break
            else:
                cprint("[-] The site's fingerprint does not match Spring characteristics, it might not be a Spring framework", "yellow")
        except KeyboardInterrupt:
            print("Process manually terminated with Ctrl + C")
            sys.exit()
        except Exception as e:
            print("[-] An error occurred, logged in error.log\n")
            with open("error.log", "a") as f2:
                f2.write(str(e) + '\n')

def check(url, proxies, header_new):
    header_new = json.loads(header_new)
    if '://' not in url:
        url = "http://" + str(url)
    if url[-1] != "/":
        url += "/"
    try:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, timeout=6, verify=False, headers=header_new, proxies=proxies)
        if r.status_code == 503:
            sys.exit()
        else:
            Spring_Check(url, proxies, header_new)
            return url
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        cprint(f"[-] The target URL {url} actively rejected the request, skipping! Logged in error.log", "magenta")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')
        sys.exit()

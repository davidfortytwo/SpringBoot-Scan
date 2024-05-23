#!/usr/bin/env python3
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, run, vul, console
import requests, sys, json
from termcolor import cprint
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

# Check the usage of proxy
def SpringBoot_Scan_Proxy(args):
    if args.proxy:
        proxies = {
            "http": "http://%(proxy)s/" % {'proxy': args.proxy},
            "https": "http://%(proxy)s/" % {'proxy': args.proxy}
        }
        cprint("===== Checking proxy availability =====", "cyan")
        testurl = "https://www.baidu.com/"
        headers = {"User-Agent": "Mozilla/5.0"}  # Response headers
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.get(testurl, timeout=10, proxies=proxies, verify=False, headers=headers)
            print(res.status_code)
            # Send request and return response code
            if res.status_code == 200:
                print("GET www.baidu.com status code:" + str(res.status_code))
                cprint("[+] Proxy is available, executing now!", "cyan")
                if args.urlfile:
                    proxies = f'http://{args.proxy}'
                SpringBoot_Scan_Header(args, proxies)
        except KeyboardInterrupt:
            print("Process manually terminated with Ctrl + C")
            sys.exit()
        except Exception as e:
            print('Error:', e)
            cprint("[-] Proxy is not available, please change the proxy!", "magenta")
            sys.exit()
    else:
        proxies = ''
        SpringBoot_Scan_Header(args, proxies)


# Import custom HTTP headers
def SpringBoot_Scan_Header(args, proxies):
    if args.newheader:
        cprint("===== Importing custom HTTP headers =====", "cyan")
        filename = args.newheader
        with open(filename, 'r') as file:
            lines = file.readlines()
        # Create JSON object
        header_json = {}
        for line in lines:
            # Split each line by ':', taking the parts before and after
            parts = line.split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                header_json[key] = value
        header_new = json.dumps(header_json, indent=2)
        print(header_new)
        SpringBoot_Scan_Main(args, proxies, header_new)
    else:
        header_new = '{}'
        SpringBoot_Scan_Main(args, proxies, header_new)


def SpringBoot_Scan_Main(args, proxies, header_new):
    if (args.url or args.urlfile or args.vul or args.vulfile or args.dump or args.zoomeye or args.fofa or args.hunter):
        console.SpringBoot_Scan_console(args, proxies, header_new)
    else:
        output.usage()
        sys.exit()

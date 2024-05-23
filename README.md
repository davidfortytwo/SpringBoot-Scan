![SpringBoot-Scan](https://socialify.git.ci/AabyssZG/SpringBoot-Scan/image?description=1&descriptionEditable=Open%20source%20penetration%20framework%20for%20SpringBoot%20and%20high-risk%20vulnerability%20exploitation%20tools%20related%20to%20Spring&font=Rokkitt&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F54609266%3Fv%3D4&name=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

# ✈️ 1. Tool Overview

During routine penetration testing, we often encounter microservices built with Spring Boot. This inspired the creation of an open-source penetration framework specifically for Spring Boot, primarily used for scanning sensitive information leakage endpoints and directly testing for high-risk vulnerabilities related to Spring. Thus, the tool **SpringBoot-Scan** (abbreviated as "SB-Scan") was developed.

**Current tool version: V2.51-2024/05/19**

**I have also compiled a guide on Spring Boot penetration techniques on my personal blog. Feel free to check it out and exchange ideas: [https://blog.zgsec.cn/archives/129.html](https://blog.zgsec.cn/archives/129.html)**

# 📝 2. TODO

## Vulnerability Support Updates

* [x] Added support for 2023 JeeSpringCloud arbitrary file upload vulnerability
* [x] Added support for CVE-2022-22947 (Spring Cloud Gateway SpEL RCE vulnerability)
* [x] Added support for CVE-2022-22963 (Spring Cloud Function SpEL RCE vulnerability)
* [x] Added support for CVE-2022-22965 (Spring Core RCE vulnerability)
* [x] Added support for CVE-2021-21234 (arbitrary file read vulnerability)
* [x] Added support for 2021 SnakeYAML_RCE vulnerability
* [x] Added support for 2021 Eureka_Xstream deserialization vulnerability
* [x] Added support for 2020 Jolokia misconfiguration leading to RCE vulnerability
* [x] Added support for CVE-2018-1273 (Spring Data Commons RCE vulnerability)
* [x] Added module to select single or multiple vulnerabilities for detection
* [x] Interactive command execution for command execution vulnerabilities
* [x] Added batch vulnerability verification module (finally here!)

Future updates will include more built-in modules for vulnerability exploitation (please consider giving it a star, coding is quite labor-intensive, haha).

## Feature Support Updates

* [x] Thanks to [`@Viking`](https://github.com/VK2000), added more content to the `Dir.txt` sensitive endpoints dictionary
* [x] Thanks to [`@Fkalis`](https://github.com/FFR66), used `aiohttp` for concurrent batch information leakage scanning, significantly speeding up the `-uf` parameter
* [x] Added support for multiple custom HTTP headers (request headers) during operations
* [x] Added support for custom query statements when exporting asset mappings
* [x] Added delay scanning during sensitive endpoint brute force to prevent being blocked due to fast scanning speed
* [x] Added [Hunter asset mapping](https://hunter.qianxin.com/) export module, automatically interfacing with the API to export assets to `hunterout.txt`
* [x] Added [Fofa asset mapping](https://fofa.info/) export module, automatically interfacing with the API to export assets to `fofaout.txt`
* [x] Added [ZoomEye asset mapping](https://www.zoomeye.org/) export module, automatically interfacing with the API to export assets to `zoomout.txt`
* [x] Filtering out some invalid echo pages during Spring endpoint brute force, improving work efficiency
* [x] Optimized the endpoint brute force dictionary, added some bypass statements (feel free to submit any additions)
* [x] Automatic fingerprint recognition for Spring
* [x] Output errors to `error.log` in the vulnerability exploitation module
* [x] Support for using authenticated HTTP proxy nodes, automatically checking node status
* [x] GUI version created by `@13exp`
* [x] Verify proxy availability, support using HTTP/HTTPS proxy for all traffic
* [x] Random User-Agent request headers
* [x] Resolve SSL certificate issues (use `http://` for self-signed certificates)
* [x] Intelligent target address recognition (e.g., `example.com`, `http://example.com/`, and `http://example.com` are all accepted without error)

## Notes

- **This tool enhances user experience by accepting `example.com`, `http://example.com/`, and `http://example.com` without error. The program will automatically identify and process these formats.**
- **SSL certificate issues have been resolved, allowing scans on Spring Boot frameworks using SSL certificates (use `http://` for self-signed certificates).**
- **For Spring projects deployed in subdirectories, simply provide the corresponding path to the tool (e.g., if `example.com/test/` deploys a Spring project, pass `example.com/test/` as the parameter to the tool).**

**GUI version created by [`@13exp`](https://github.com/13exp/), available at: [https://github.com/13exp/SpringBoot-Scan-GUI](https://github.com/13exp/SpringBoot-Scan-GUI)**

![GUI](./pic/GUI.png)

**Note: Both the main project `vul.py` and the GUI project contain vulnerability exploitation modules. It's normal for antivirus software to flag them. If you find the tool useful, consider giving it a star, haha!**

# 🚨 3. Install Python Dependencies
```
pip install -r requirements.txt
```

If the installation is slow, you can use a domestic source:
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

# 🐉 4. Usage

How to find Spring frameworks on the internet, ZoomEye syntax:
```
app:"Spring Framework"
```

Fofa syntax:
```
icon_hash="116323821" || body="Whitelabel Error Page"
```

Tool parameters:
```
# python3 SpringBoot-Scan.py
  ______                       __                      _______                        __     
 /      \                     |  \                    |       \                      |  \    
|  $$$$$$\  ______    ______   \$$ _______    ______  | $$$$$$$\  ______    ______  _| $$_   
| $$___\$$ /      \  /      \ |  \|       \  /      \ | $$__/ $$ /      \  /      \|   $$ \  
 \$$    \ |  $$$$$$\|  $$$$$$\| $$| $$$$$$$\|  $$$$$$\| $$    $$|  $$$$$$\|  $$$$$$\\$$$$$$  
 _\$$$$$$\| $$  | $$| $$   \$$| $$| $$  | $$| $$  | $$| $$$$$$$\| $$  | $$| $$  | $$ | $$ __ 
|  \__| $$| $$__/ $$| $$      | $$| $$  | $$| $$__| $$| $$__/ $$| $$__/ $$| $$__/ $$ | $$|  \
 \$$    $$| $$    $$| $$      | $$| $$  | $$ \$$    $$| $$    $$ \$$    $$ \$$    $$  \$$  $$
  \$$$$$$ | $$$$$$$  \$$       \$$ \$$   \$$ _\$$$$$$$ \$$$$$$$   \$$$$$$   \$$$$$$    \$$$$ 
          | $$                              |  \__| $$                                       
          | $$                               \$$    $$                                       
           \$$                                \$$$$$$                                        
            ______                                                                           
           /      \                                  +-------------------------------------+ 
          |  $$$$$$\  _______  ______   _______      + Version: 2.51                       + 
          | $$___\$$ /       \|      \ |       \     + Author: 曾哥(@AabyssZG)             + 
           \$$    \ |  $$$$$$$ \$$$$$$\| $$$$$$$\    + Whoami: https://github.com/AabyssZG + 
           _\$$$$$$\| $$      /      $$| $$  | $$    +-------------------------------------+ 
          |  \__| $$| $$_____|  $$$$$$$| $$  | $$    + 多进程速度提升: Fkalis              + 
           \$$    $$ \$$     \\$$    $$| $$  | $$    + Whoami: https://github.com/FFR66    + 
            \$$$$$$   \$$$$$$$ \$$$$$$$ \$$   \$$    +-------------------------------------+ 

Usage:
    Scan a single URL for information leakage:        python3 SpringBoot-Scan.py -u example.com
    Read target TXT for batch information leakage scanning:    python3 SpringBoot-Scan.py -uf url.txt
    Exploit vulnerabilities in a single URL:         python3 SpringBoot-Scan.py -v example.com
    Read target TXT for batch vulnerability scanning:      python3 SpringBoot-Scan.py -vf url.txt
    Scan and download Spring Boot sensitive files:      python3 SpringBoot-Scan.py -d example.com
    Use HTTP proxy and perform connectivity tests:    python3 SpringBoot-Scan.py -p <proxy IP:port>
    Import custom HTTP headers from TXT file:        python3 SpringBoot-Scan.py -t header.txt
    Download data via ZoomEye API key:      python3 SpringBoot-Scan.py -z <ZoomEye API-KEY>
    Download data via Fofa API key:         python3 SpringBoot-Scan.py -f <Fofa API-KEY>
    Download data via Hunter API key:       python3 SpringBoot-Scan.py -y <Hunter API-KEY>
```

# 🛸 5. Tool Demonstration

## 0# Spring Asset Mapping

### Asset Mapping via ZoomEye

This tool interfaces with the [ZoomEye API](https://www.

zoomeye.org/doc), allowing you to batch download Spring asset mapping data using the API key:
```
python3 SpringBoot-Scan.py -z <ZoomEye API-KEY>
```

![ZoomEye](./pic/ZoomEye.png)

**Note: This module now supports custom syntax for asset mapping export; the results will be exported to `zoomout.txt` after the asset mapping is complete, and you can use other parameters for operations.**

### Asset Mapping via Fofa

This tool interfaces with the [Fofa API](https://fofa.info/api), allowing you to batch download Spring asset mapping data using the API key:
```
python3 SpringBoot-Scan.py -f <Fofa API-KEY>
```

![Fofa](./pic/Fofa.png)

**Note: This module now supports custom syntax for asset mapping export; the results will be exported to `fofaout.txt` after the asset mapping is complete, and you can use other parameters for operations.**

### Asset Mapping via Hunter

This tool interfaces with the [Hunter API](https://hunter.qianxin.com/home/helpCenter?r=5-1-2), allowing you to batch download Spring asset mapping data using the API key:
```
python3 SpringBoot-Scan.py -y <Hunter API-KEY>
```

![Hunter](./pic/Hunter.png)

**Note: This module now supports custom syntax for asset mapping export; the results will be exported to `hunterout.txt` after the asset mapping is complete, and you can use other parameters for operations.**

## 1# Testing and Using Proxy and Custom HTTP Headers

### Testing and Using Proxy

```
python3 SpringBoot-Scan.py -p <proxy IP:port>
python3 SpringBoot-Scan.py -p <HTTP auth username:HTTP auth password@proxy IP:port>
```

![Test Proxy](./pic/测试代理.png)

For example, to scan a single URL for information leakage using a proxy:
```
python3 SpringBoot-Scan.py -u example.com -p <proxy IP:port>
python3 SpringBoot-Scan.py -p <HTTP auth username:HTTP auth password@proxy IP:port>
```
Similarly, other parameters (`-u` / `-uf` / `-v` / `-vf` / `-d`) can be used with a proxy.

### Testing and Using Custom HTTP Headers

```
python3 SpringBoot-Scan.py -t header.txt
```

![Headers](./pic/Headers.png)

To use this custom HTTP header feature, modify the contents of `header.txt` accordingly. This feature supports the (`-u` / `-uf` / `-v` / `-d`) parameters. Batch vulnerability scanning does not have a clear need for this feature, so it was not included.

## 2# Brute Forcing Sensitive Endpoints for a Single URL

`Dir.txt` is a built-in Spring endpoint brute force dictionary. It contains most sensitive information leakage endpoints related to Spring Boot.

If there are any omissions, feel free to contact me.

```
python3 SpringBoot-Scan.py -u example.com
```

![Scan Single URL](./pic/扫描单一URL.png)

Added delay scanning option; if you do not want delay scanning, enter `0` and press Enter.

**Note: Successful results will be exported to `urlout.txt` in the same directory.**

## 3# Reading Target TXT for Batch Information Leakage Scanning

```
python3 SpringBoot-Scan.py -uf url.txt
```

![Batch Scan from TXT](./pic/读取TXT并批量扫描.png)

Added delay scanning option; if you do not want delay scanning, enter `0` and press Enter. Thanks to [`@Fkalis`](https://github.com/FFR66), added concurrent scanning option, with a default concurrency of 10.

**Note: Due to version updates, the parameter for reading TXT and scanning has been changed to `uf` from version 2.21 onwards. Successful results will be exported to `output.txt` in the same directory.**

## 4# Exploiting Vulnerabilities in a Single URL

```
python3 SpringBoot-Scan.py -v example.com
```

![Exploit Single URL](./pic/对单一URL进行漏洞利用.png)

Implemented RCE vulnerability and command customization feature (don't use it for bad purposes).

**More built-in modules for vulnerability exploitation will be added in the future, so stay tuned!**

## 5# Reading Target TXT for Batch Vulnerability Scanning

```
python3 SpringBoot-Scan.py -vf url.txt
```

![Poc](./pic/Poc.png)

You can freely select vulnerabilities from the vulnerability library for batch verification. Successful results will be exported to `vulout.txt`.

## 6# Scanning and Downloading SpringBoot Sensitive Files

```
python3 SpringBoot-Scan.py -d example.com
```

![Scan and Download Sensitive Files](./pic/扫描并下载SpringBoot敏感文件.png)

**Note: Scanned sensitive files will be automatically downloaded to the script's running directory, with a progress bar showing real-time download progress.**

Currently, the built-in sensitive file directories include:
```
actuator/heapdump
gateway/actuator/heapdump
heapdump
heapdump.json
hystrix.stream
artemis-portal/artemis/heapdump
```

If you know of other sensitive file directories, please submit an issue. Thank you!

# 🖐 6. Disclaimer

1. By downloading, installing, using, or modifying this tool and related code, you indicate your trust in this tool.
2. We are not responsible for any form of loss or damage caused to you or others while using this tool.
3. You are responsible for any illegal activities conducted while using this tool. We are not liable for any legal or joint responsibilities.
4. Please read and fully understand the terms, especially those that exempt or limit liability, and choose to accept or not accept them.
5. Unless you have read and accepted all terms of this agreement, you do not have the right to download, install, or use this tool.
6. Your download, installation, and use of this tool constitute your agreement to the terms of this agreement.

# 🙏 7. Thanks to All Contributors

## Stargazers

[![Stargazers repo roster for @AabyssZG/SpringBoot-Scan](http://reporoster.com/stars/AabyssZG/SpringBoot-Scan)](https://github.com/AabyssZG/SpringBoot-Scan/stargazers)

## Forkers

[![Forkers repo roster for @AabyssZG/SpringBoot-Scan](http://reporoster.com/forks/AabyssZG/SpringBoot-Scan)](https://github.com/AabyssZG/SpringBoot-Scan/network/members)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AabyssZG/SpringBoot-Scan&type=Date)](https://star-history.com/#AabyssZG/SpringBoot-Scan&Date)

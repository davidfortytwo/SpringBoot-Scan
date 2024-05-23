  #!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

import time, os, sys

def logo():
    logo0 = r'''
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
          | $$                               \$$    $$   [+] V2.51-2024 Year of the Dragon New Year Edition     
           \$$                                \$$$$$$    [+] Thanks to all the masters who supported and followed us along the way  
            ______                                                                           
           /      \                                  +-------------------------------------+ 
          |  $$$$$$\  _______  ______   _______      + Version: 2.51                       + 
          | $$___\$$ /       \|      \ |       \     + Author: 曾哥(@AabyssZG)             + 
           \$$    \ |  $$$$$$$ \$$$$$$\| $$$$$$$\    + Whoami: https://github.com/AabyssZG + 
           _\$$$$$$\| $$      /      $$| $$  | $$    +-------------------------------------+ 
          |  \__| $$| $$_____|  $$$$$$$| $$  | $$    + Speed improvement via multiprocessing: Fkalis              + 
           \$$    $$ \$$     \\$$    $$| $$  | $$    + Whoami: https://github.com/FFR66    + 
            \$$$$$$   \$$$$$$$ \$$$$$$$ \$$   \$$    +-------------------------------------+ 
'''
    print(logo0)

def usage():
    print('''
Usage:
    Scan a single URL for information leakage:         python3 SpringBoot-Scan.py -u http://example.com/
    Read target TXT for batch information leakage scanning:    python3 SpringBoot-Scan.py -uf url.txt
    Scan a single URL for vulnerabilities:             python3 SpringBoot-Scan.py -v http://example.com/
    Read target TXT for batch vulnerability scanning:  python3 SpringBoot-Scan.py -vf url.txt
    Scan and download SpringBoot sensitive files:      python3 SpringBoot-Scan.py -d http://example.com/
    Use HTTP proxy and perform connectivity test:      python3 SpringBoot-Scan.py -p <proxy IP:port>
    Import custom HTTP headers from TXT file:          python3 SpringBoot-Scan.py -t header.txt
    Download data via ZoomEye API key:                 python3 SpringBoot-Scan.py -z <ZoomEye API-KEY>
    Download data via Fofa API key:                    python3 SpringBoot-Scan.py -f <Fofa API-KEY>
    Download data via Hunter API key:                  python3 SpringBoot-Scan.py -y <Hunter API-KEY>

██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗    ███╗   ██╗███████╗██╗    ██╗██╗   ██╗███████╗ █████╗ ██████╗ 
██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔════╝██║    ██║╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗
███████║███████║██████╔╝██████╔╝ ╚████╔╝     ██╔██╗ ██║█████╗  ██║ █╗ ██║ ╚████╔╝ █████╗  ███████║██████╔╝
██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝      ██║╚██╗██║██╔══╝  ██║███╗██║  ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗
██║  ██║██║  ██║██║     ██║        ██║       ██║ ╚████║███████╗╚███╔███╔╝   ██║   ███████╗██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝       ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                         [+] SpringBoot-Scan V2.51-2024 Year of the Dragon New Year Edition

Disclaimer:
    1. By downloading, installing, using, or modifying this tool and related code, you indicate your trust in this tool.
    2. We are not responsible for any form of loss or damage caused to you or others while using this tool.
    3. You are responsible for any illegal activities conducted while using this tool. We are not liable for any legal or joint responsibilities.
    4. Please read and fully understand each clause, especially those that exempt or limit liability, and choose to accept or not accept them.
    5. Unless you have read and accepted all terms of this agreement, you do not have the right to download, install, or use this tool.
    6. Your download, installation, and use constitute your agreement to be bound by this agreement.
        ''')

"""
Parameters:
    -u  --url       Scan a single URL for information leakage
    -uf  --urlfile  Read target TXT for batch information leakage scanning  
    -v  --vul       Exploit vulnerabilities in a single URL
    -vf  --vulfile  Read target TXT for batch vulnerability scanning
    -d  --dump      Scan and download SpringBoot sensitive files (extract sensitive information)
    -p  --proxy     Use HTTP proxy (default connectivity test www.baidu.com)
    -z  --zoomeye   Batch download Spring asset mapping data via ZoomEye API
    -f  --fofa      Batch download Spring asset mapping data via Fofa API
    -y  --hunter    Batch download Spring asset mapping data via Hunter API
    -t  --newheader Import custom HTTP headers from a TXT file
"""

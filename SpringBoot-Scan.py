#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, console, run ,proxycheck
import re, binascii, argparse, sys, time

def get_parser():
    parser = argparse.ArgumentParser(usage='python3 SpringBoot-Scan.py', description='SpringBoot-Scan: An open-source penetration framework for SpringBoot')
    p = parser.add_argument_group('SpringBoot-Scan Parameters')
    p.add_argument("-u", "--url", type=str, help="Scan a single URL for information leakage")
    p.add_argument("-uf", "--urlfile", type=str, help="Read target TXT file for information leakage scanning")
    p.add_argument("-v", "--vul", type=str, help="Exploit vulnerabilities in a single URL")
    p.add_argument("-vf", "--vulfile", type=str, help="Read target TXT file for batch vulnerability scanning")
    p.add_argument("-d", "--dump", type=str, help="Scan and download SpringBoot sensitive files (extract sensitive information)")
    p.add_argument("-p", "--proxy", type=str, default='', help="Use HTTP proxy")
    p.add_argument("-z", "--zoomeye", type=str, default='', help="Export Spring framework assets using ZoomEye")
    p.add_argument("-f", "--fofa", type=str, default='', help="Export Spring framework assets using Fofa")
    p.add_argument("-y", "--hunter", type=str, default='', help="Export Spring framework assets using Hunter")
    p.add_argument("-t", "--newheader", type=str, help="Import custom HTTP headers from a TXT file")
    args = parser.parse_args()
    return args

def main():
    output.logo()
    args = get_parser()
    proxycheck.SpringBoot_Scan_Proxy(args)
    #console.SpringBoot_Scan_console(args)

if __name__ == '__main__':
    main()

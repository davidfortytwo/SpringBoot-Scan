#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output, run, vul, springcheck, zoom, fofa, poc, hunter
import sys, asyncio

# Console - parameter processing and program invocation
def SpringBoot_Scan_console(args, proxies, header_new):
    if args.url:
        urlnew = springcheck.check(args.url, proxies, header_new)
        run.url(urlnew, proxies, header_new)
    if args.urlfile:
        asyncio.run(run.file_main(args.urlfile, proxies, header_new))
    if args.vul:
        urlnew = springcheck.check(args.vul, proxies, header_new)
        vul.vul(urlnew, proxies, header_new)
    if args.vulfile:
        poc.poc(args.vulfile, proxies)
    if args.dump:
        urlnew = springcheck.check(args.dump, proxies, header_new)
        run.dump(urlnew, proxies, header_new)
    if args.zoomeye:
        zoom.ZoomDownload(args.zoomeye, proxies)
    if args.fofa:
        fofa.FofaDownload(args.fofa, proxies)
    if args.hunter:
        hunter.HunterDownload(args.hunter, proxies)
    else:
        output.usage()
        sys.exit()

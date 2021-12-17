#!/usr/bin/python
# -*- coding: UTF-8 -*-
#这是一个用于IP和域名碰撞匹配访问的小工具
import requests
import re
import argparse
import datetime
import os

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('-ip', dest='ip', type=str, help='traget ip')
parser.add_argument('-domain', dest='domain', type=str, help='target domain')
parser.add_argument('-dict', dest='dict', type=str, help='subdomain dict, default="subdomain.txt"',default="subdomain.txt")

args = parser.parse_args()
ip = args.ip
domain = args.domain
lists=[]
files = open(domain+now_time+'.txt','w+',encoding='utf-8')
#读取IP地址
print("====================================开 始 匹 配====================================")
#读取host地址
# http_s = ['http://','https://']
http_s = ['http://']
for sub in open(args.dict, "r"):
    for h in http_s :
        host = sub.strip('\n') + "." + domain.strip('\n')
        headers = {'Host':host,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        try:
            r = requests.session()
            requests.packages.urllib3.disable_warnings()
            rhost = r.get(h + ip,verify=False,headers=headers,timeout=5)
            rhost.encoding='utf-8'
            title = re.search('<title>(.*)</title>', rhost.text).group(1) #获取标题
            info = '%s -- %s 协议: %s 数据包大小: %d 标题: %s' % (ip,host,h,len(rhost.text),title)
            if rhost.status_code in [200,302,401]:    
                lists.append(info)
                files.write(info + "\n")
            print(info)
        except Exception :
            error = ip + " --- " + host + " --- 访问失败！~"
            print(error)
if lists:
    print("====================================匹 配 成 功 的 列 表====================================")
    for i in lists:
        print(i)
    print("Please open the result file {}\{}.txt".format(os.path.split(os.path.realpath(__file__))[0],domain+now_time))
else:
    print("====================================未 能 匹 配 到 域 名====================================")

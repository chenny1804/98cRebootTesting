
# -*- coding: cp936 -*-
import urllib
import sys,getopt,base64
from time import sleep
import time
import json,os
import requests
from config_lib import getConfig
SERVER_IP_ADDR=getConfig("baseconfig","SERVER_IP_ADDR")
DATA_TYPE=getConfig("baseconfig","DATA_TYPE")
SERVER_PORT=getConfig("baseconfig","SERVER_PORT")
CLIENT_PORT=getConfig("baseconfig","CLIENT_PORT")
AP_WORK_MODE=getConfig("wifi","AP_WORK_MODE")
CHANNEL_MAP=getConfig("wifi","CHANNEL_MAP")
AUTOCH_SS_TIME=getConfig("wifi","AUTOCH_SS_TIME")
MONITOR_TIME=getConfig("wifi","MONITOR_TIME")
AUTOCH_CNT=getConfig("wifi","AUTOCH_CNT")
IPLIST=getConfig("IPLIST","IP").split("|")
Author=("guest","guest")
def kuyuan_config(ip):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    data={"ap_work_mode":AP_WORK_MODE,
    "server_ip_addr":SERVER_IP_ADDR,
    "data_type":DATA_TYPE,
    "autoch_ss_time":AUTOCH_SS_TIME,
    "autoch_ch_map":CHANNEL_MAP,
    "monitor_time":MONITOR_TIME,
    "server_port":SERVER_PORT,
    "client_port":CLIENT_PORT,
    "autoch_ss_cnt":AUTOCH_CNT}
    result=url_request_post(url,data,5)
    if result:
        if result["status_code"] == 200 and "SUCCESS" in result["text"]:
            print "Set kuyuan_config  OK"
        else:
            print "Set kuyuan_config Error"
    else:
        print "CONFIG Error!!!!!Please Check IP"
def set_led_location(ip):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    data={"mode_name":"netcore_set",
    "CurrentApp":"Welcome",
    "location_time_enable":"0",
    "location_time":"2"}
    result=url_request_post(url,data,5)
    if result:
        if result["status_code"] == 200 and "SUCCESS" in result["text"]:
            print "Set Led locatpion OK"
        else:
            print "Set Led locatpion Error"
    else:
        print "CONFIG Error!!!!!Please Check IP"
def url_request_post(url,param,timeout):
    data=urllib.urlencode(param)
    headers = {'content-type': 'text/plain; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    result={}
    try:
        response=requests.get(url+"?"+data,headers=headers,timeout=timeout)
        result["status_code"]=response.status_code
        result["text"]=response.text
        return result
    except Exception as e:
        print e,"CONFIG Error!!!!!Please Check IP"
        return False   
def main():
    for ip in IPLIST:
        print "CONFIG",ip
        kuyuan_config(ip)
if __name__ == '__main__':
    main()
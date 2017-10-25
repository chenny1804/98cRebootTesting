# -*- coding: cp936 -*-
import urllib2,urllib
import sys,getopt,base64
from time import sleep
import time
import json,os
import requests
########
#Menu
#######
def usage():
    print
    print "-----------------------------------------------------"
    print 'USAGE: upgrade.py [OPTIONS]'
    print
    print ' OPTIONS:'
    print "\t -n operate times"
    print "\t -T sleep time"
    print "\t -F choice Fuction"
    print "\t -f the file name of upgrade"
    print "\t -O login user and password"
    print "\t -R reboot"
    print "\t -D default"
    print "\t -U upgrade"
    print "\t -C config ROUTER"
    print "EXAMPLE:"
    print "\t98cTools.py 192.168.1.254 -RO guest:guest"
    print "\t98cTools.py 192.168.1.254 -DO guest:guest"
    print "\t98cTools.py 192.168.1.254 -UO guest:guest -f 881.bin "
    print "\t98cTools.py 192.168.1.254 -UO guest:guest -f 881.bin|882.bin "
    print "\t98cTools.py 192.168.1.254 -n 10 -RO guest:guest"
    print "\t98cTools.py 192.168.1.254 -n 10 -T 180 -RO guest:guest"
    print "\t98cTools.py 192.168.1.254 -n 0 -T 180 -RO guest:guest"
    print "-----------------------------------------------------"



#########
#upgrade
#########
def UpgradeAp(ip,filename,Author):
    boundary = hex(int(time() * 1000))
    HEADER ={"Authorization": "Basic "+Author,
         "Content-Type": "multipart/form-data; boundary=---------------------------%s"%boundary,
         "Referer": "http://"+ip+"/update.htm"
    }
    data=[]
    fr=open(filename,"rb")
    data.append('-----------------------------%s' % boundary)
    data.append('Content-Disposition: form-data; name="put_file"; filename='+filename+'\r\n')
    data.append('Content-Type: application/octet-stream\r\n')
    data.append(fr.read())
    fr.close()
    data.append('-----------------------------%s' % boundary)
    http_body="\r\n".join(data)
    http_url="http://"+ip+"/cgi-bin-igd/put_file.cgi"
    count=1
    req=urllib2.Request(http_url, data=http_body,headers=HEADER)
    try:
        resp=urllib2.urlopen(req)
        if resp.code == 200:
            print "upgrade OK"
    except Exception as e:
        print e,"upgrade error! Please Check IP"
        sys.exit()
def Upgrade(filename):
    url="http://"+ip+"/router/put_file.cgi"
    upgradefiles={'file':open(filename,"rb")}
    try:
        response=requests.post(url,files=upgradefiles,auth=Author)
        if response.status_code == 200:
            print "Upgrade text:",response.text
            if response.text == "1":
                print "Upgrade SUCCESS"
            else:
                print "Upgrade Error,RESULT:",response.text
            return response.text
        else:
            print "Upgrade Error"
    except Exception as e:
        print e,"Upgrade Error!!!!!Please Check IP"
        sys.exit()        
########
# Reboot
########
def Reboot(ip,Author):
    url="http://"+ip+"/router/reboot.cgi?noneed=noneed"
    try:
        response=requests.post(url,auth=Author,timeout=5)
        response_str=response.text
        if "SUCCESS" in response_str:
            print "Reboot SUCCESS"
        else:
            print "response_str:",response_str
            print "Reboot Error"
    except Exception as e:
        print e,"SET Qos Error!!!!!Please Check IP"
        sys.exit() 


######
#default
######
def DefaultAp(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={"mode_name":"netcore_set",
          "redefault":"1",
          "default_set":"1",
          "reboot_set":"1",
          "reboot":"1",
          "CurrentApp":"default"
          }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "Default SUCCESS"
        else:
            print "Default Error"
    except Exception as e:
        print e,"Default Error!!!!!Please Check IP"
        sys.exit()

#############
# set wlan ssid
#############

def set_wifi(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "ssid":"HONYAR321321",
        "ssid_broad":"1",
        "wifi_idx":"1",
        "sec_mode":"3",
        "key_type":"2",
        "key_mode_wpa":"0",
        "key_wpa":"123456789012345678901234567890123456789012345678901234567890abcd",
        "sta_live_time":"300",
        "ap_user_name":"0",
        "wlan_vlan_id":"0",
        "CurrentApp":"Welcome",
        "wl_enable":"1",
        "mode_name":"netcore_set",
        "wlan_vlan_qos":"0",
        "wl_mac_filter_enable":"0",
        "ap_flag":"1",
        "vwlan_idx":"0"
    }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "SET WIFI CONFIG SUCCESS"
        else:
            print "SET WIFI CONFIG Error"
    except Exception as e:
        print e,"SET WIFI CONFIG Error!!!!!Please Check IP"
        sys.exit()


def set_wifi_enable(ip,Author,status):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "mode_name":"netcore_set",
        "wifi_enable":status
          }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "SET WIFI ENABLE or DISABLE SUCCESS"
        else:
            print "SET WIFI ENABLE or DISABLE Error"
    except Exception as e:
        print e,"SET WIFI ENABLE or DISABLE Error!!!!!Please Check IP"
        sys.exit()
def end_led_location(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "mode_name":"netcore_set",
        "CurrentApp":"Welcome",
        "location_time_enable":"0"
    }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "END LED LOCATION SUCCESS"
        else:
            print "END LED LOCATION SUCCESS Error"
    except Exception as e:
        print e,"END LED LOCATION SUCCESS!!!!!Please Check IP"
        sys.exit()
def start_led_location(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "mode_name":"netcore_set",
        "CurrentApp":"Welcome",
        "location_time_enable":"1",
        "location_time":"2"
    }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "START LED LOCATION SUCCESS"
        else:
            print "START LED LOCATION Error"
    except Exception as e:
        print e,"START LED LOCATION!!!!!Please Check IP"
        sys.exit()

def set_led_on_off(ip,Author,status):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "mode_name":"netcore_set",
        "led_off_on_status":status,
        "CurrentApp":"Welcome"
    }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "SET LED ON or OFF  SUCCESS"
        else:
            print "SET LED ON or OFF  Error"
    except Exception as e:
        print e,"SET LED ON or OFF  Error!!!!!Please Check IP"
        sys.exit()   
def set_wifi_advance(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={
        "mode_name":"netcore_set",
        "wl_stand":"11",
        "channel_width":"0",
        "channel":"0",
        "wlan_partition":"0",
        "out_power":"0",
        "wl_limitnum":"0",
        "wl_rssi_threshold":"0",
        "wl_rssi_threshold_refuse":"0",
        "wl_advanced_set":"ap",
        "wl_limitnum_enable":"0",
        "wl_rssi_threshold_enable":"0",
        "wl_rssi_threshold_refuse_enable":"0"
          }
    req=urllib2.Request(url)
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data)
        if "SUCCESS" in response.read():
            print "SET WIFI ADVANCE SUCCESS"
        else:
            print "SET WIFI ADVANCE Error"
    except Exception as e:
        print e,"SET WIFI ADVANCE Error!!!!!Please Check IP"
        sys.exit()

def del_all_virtual_service_list():
    url="http://"+ip+"/router/virtual_service_clean.cgi?no=no"
    try:
        response=requests.post(url,auth=Author,timeout=5)
        if response.status_code == 200 and json.loads(response.text) == ["SUCCESS"]:
            print "DEL all virtual service list SUCCESS"
        else:
            print "response_status_code:",response.status_code
            print "DEL all virtual service list Error",
    except Exception as e:
        print e,"DEL all virtual service list Error!!!!!Please Check IP"
        sys.exit()
def set_virtual_service_add():
    url="http://"+ip+"/router/virtual_service_add_del.cgi"
    data={"in_end_port":"",
    "in_ip":"192.168.1.33",
    "in_start_port":"22",
    "mode":"0",
    "name":"1",
    "out_end_port":"",
    "out_start_port":"22",
    "proto":"tcp",
    "remote_ip":"10.0.0.10",
    "uiname":"ALL"}
    data=urllib.urlencode(data)
    try:
        response=requests.post(url+"?"+data,auth=Author)
        response_str=response.text
        if "SUCCESS" in response_str:
            print "SET Virtual service SUCCESS"
        else:
            print "response_str:",response_str
            print "SET Virtual service Error"
    except Exception as e:
        print e,"SET Virtual service Error!!!!!Please Check IP"
        sys.exit()
def check_Virtual_service_add():
    url="http://"+ip+"/router/virtual_service_list_show.cgi?noneed=noneed"
    try:
        response=requests.post(url,auth=Author)
        if response.status_code == 200:
            response_str=json.loads(response.text)
        # print "check virtual service add",response_str
            if response_str == [{"name":"1","remote_ip":"10.0.0.10","in_ip":"192.168.1.33","proto":"tcp","uiname":"ALL","in_start_port"
:"22","in_end_port":"22","out_start_port":"22","out_end_port":"22"}]:
                print "Check add virtual list OK"
            else:
                print "Check add virtual list Error"
        else:
            print "Check add virtual list Error,status_code:",response.status_code
    except Exception as e:
        print e,"Check add virtual list Error!!!!!Please Check IP"
        sys.exit()
def set_Qos(max_count,qos_down_xianzhi_def,qos_up_xianzhi_def):
    """
    # max_count:  the max connect number
    # qos_down_xianzhi_def: the speed of down  
    """
    url="http://"+ip+"/router/qos_xianz_ok.cgi?max_count="+str(max_count)+\
    "&qos_down_xianzhi_def="+str(qos_down_xianzhi_def)+\
    "&qos_up_xianzhi_def="+str(qos_up_xianzhi_def)
    try:
        response=requests.post(url,auth=Author,timeout=5)
        response_str=response.text
        if "SUCCESS" in response_str:
            print "SET QoS SUCCESS"
        else:
            print "response_str:",response_str
            print "SET Qos Error"
    except Exception as e:
        print e,"SET Qos Error!!!!!Please Check IP"
        sys.exit() 
def check_Qos(max_count,down_max_speed,up_max_speed):
    url="http://"+ip+"/router/qos_xianz_ok_show.cgi?noneed=noneed"
    try:
        response=requests.post(url,auth=Author,timeout=5)
        if response.status_code == 200:
            response_str=json.loads(response.text)
            # print response_str
            if response_str["max_count"] == str(max_count) \
            and response_str["down_max_speed"]==str(down_max_speed)\
            and response_str["up_max_speed"]== str(up_max_speed):
                    print "Check Qos OK"
            else:
                print "response_str:",response_str
        else:
            print "response_status_code:",response.status_code
            print "SET Qos Error"
    except Exception as e:
        print e,"SET Qos Error!!!!!Please Check IP"
        sys.exit()     

def config(ip,Author):
    #del_all_virtual_service_list()
    #set_virtual_service_add()
    check_Virtual_service_add()
    #set_Qos(200,700,500)
    #Reboot(ip, Author)
    #Upgrade(ip,"1.fmw",Author)
    check_Qos(200,700,500)

#######
#main
######
def main():
    global ip,Author
    try:

        if len(sys.argv) < 2:
            usage()
            sys.exit()
        opts, args = getopt.getopt(sys.argv[2:], "hn:T:F:O:RCDUf:", [ "help",'num',"Time" ,'function',"password","config","reboot","default","upgrade","file"])
        ip=sys.argv[1]
        funname=""
        count=1
        flag=False
        TIME=25
        print 'IP:',ip
        for o,a in opts:
            if o in ("-h","--help"):
                usage()
                sys.exit()
            if o in ("-F","--function"):
                funname=a
                print "FUNCTION:",funname
            if o in ("-n","--num"):
                if a == "0":
                    flag=True
                else:
                    count=int(a)
            if o in ("-T","--time"):
                TIME=int(a)
            if o in ("-O"):
                # Author=base64.encodestring(a)
                Author=(a.split(":")[0],a.split(":")[1])
                print "Author",Author
            if o in ("-R","--reboot"):
                funname="reboot"
            if o in ("-D","--default"):
                funname="default"
            if o in ("-U","--upgrade"):
                funname="upgrade"
            if o in ("-C","--config"):
                funname="config"
            if o in ("-f","--file"):
                filenames=[]
                if "|" in a:
                    filenames=a.split("|")
                else:
                    filenames.append(a)
                print "FILE:",filenames

        COUNT=0
        while flag == True or count > 0 :
            
            if funname == "upgrade":
                for filename in filenames:
                    if Upgrade(filename) == "0":
                        os.system("echo  "+time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))+"  >> upgrade.txt")
                    sleep(120)
            elif funname == "reboot":
                Reboot(ip,Author)
            elif funname == "default":
                DefaultAp(ip,Author)
            elif funname == "config":
                config(ip,Author)
            else:
                usage()
                sys.exit()
                
            count=count-1
            COUNT=COUNT+1
            print funname+"---",str(COUNT)
            if count == 0 and flag == False:
                sys.exit()
            sleep(TIME)

    except getopt.GetoptError, err:

        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit()

if __name__ == "__main__":
    main()
            

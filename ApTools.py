# -*- coding: cp936 -*-
import urllib2,urllib
import sys,getopt,base64
from time import sleep,time

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
    print "\t -C config AP"
    print "EXAMPLE:"
    print "\tupgrade.py 192.168.1.254 -RO guest:guest"
    print "\tupgrade.py 192.168.1.254 -DO guest:guest"
    print "\tupgrade.py 192.168.1.254 -UO guest:guest -f 881.bin "
    print "\tupgrade.py 192.168.1.254 -n 10 -RO guest:guest"
    print "\tupgrade.py 192.168.1.254 -n 10 -T 180 -RO guest:guest"
    print "\tupgrade.py 192.168.1.254 -n 0 -T 180 -RO guest:guest"
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


########
# Reboot
########
def RebootAp(ip,Author):
    url="http://"+ip+"/cgi-bin-igd/netcore_set.cgi"
    HEADER ={"Authorization": "Basic "+Author,
         'content-type':'application/x-www-form-urlencoded',
         "Referer": "http://"+ip+"/index.htm"
    }
    data={"mode_name":"netcore_set",
          "reboot_set":"1",
          "reboot":"1",
          "CurrentApp":"reboot"
          }
    try:
        req=urllib2.Request(url)
    except Exception as e:
        print e,"Reboot Error!Time Out"
        sys.exit()
    data=urllib.urlencode(data)
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    #response = opener.open(req, data)
    try:
        response=urllib2.urlopen(req,data,timeout=10)
        if "SUCCESS" in response.read():
            print "Reboot SUCCESS"
        else:
            print "Reboot Error"
    except Exception as e:
        print e,"Reboot Error!!!!!Please Check IP"
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

def config(ip,Author):
    set_wifi_enable(ip,Author,1)
    sleep(30)
    set_wifi(ip,Author)
    sleep(30)
    set_wifi_advance(ip, Author)
    sleep(30)
    set_led_on_off(ip,Author,0)
    sleep(10)
    set_led_on_off(ip,Author,1)
    sleep(5)
    start_led_location(ip,Author)
    sleep(15)
    end_led_location(ip,Author)
    sleep(5)
    set_wifi_enable(ip,Author,0)
    sleep(5)
#######
#main
######
def main():
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
                Author=base64.encodestring(a)
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
                filename=a
                print "FILE:",filename

        COUNT=0
        while flag == True or count > 0 :
            
            if funname == "upgrade":
                UpgradeAp(ip,filename,Author)
            elif funname == "reboot":
                RebootAp(ip,Author)
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
            

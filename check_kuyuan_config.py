from Telnet import Telnet
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
INTERFACE=getConfig("wifi","INTERFACE")
IPLIST=getConfig("IPLIST","IP").split("|")
CHANNEL_MAP_VALUE=0
def calc_ch_map_value():
	global CHANNEL_MAP_VALUE
	ch_map_list={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0}
	for i in CHANNEL_MAP.split(","):
		if i in ch_map_list.keys():
			ch_map_list[i]=1
	CHANNEL_MAP_VALUE=0
	for i in ch_map_list.keys():
		#print i
		CHANNEL_MAP_VALUE=CHANNEL_MAP_VALUE+ch_map_list[i]*(2**(int(i)-1))
	# print str(CHANNEL_MAP_VALUE)

def check_ap_mode():

	# 	print "Can't Find func_off in MIB"
	result=check_flash("cur.AP_WORK_MODE",AP_WORK_MODE)
	if result == True:
		print "FLASH Check AP_WORK_MODE \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.AP_WORK_MODE in FLASH"
	else:
		print "FLASH Check AP_WORK_MODE\t\t\tFAIL",result
	if AP_WORK_MODE == str(1):
		result_mib=check_mib("func_off",str(1),INTERFACE)
	else:
		result_mib=check_mib("func_off",str(0),INTERFACE)
	if result_mib == True:
		print "MIB   Check AP_WORK_MODE \t\tSUCCESS"
	elif result_mib == False:
		print "Can't Find cur.AP_WORK_MODE in MIB"
	else:
		print "MIB   Check AP_WORK_MODE\t\t\tFAIL",result_mib	
def check_autoch_ss_count():
	result=check_flash("cur.AUTOCH_CNT",AUTOCH_CNT)
	if result == True:
		print "FLASH Check AUTOCH_CNT \t\t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.AUTOCH_CNT in FLASH"
	else:
		print "FLASH Check AUTOCH_CNT\t\t\t\tFAIL",result
	result_mib=check_mib("autoch_ss_cnt",AUTOCH_CNT,INTERFACE)
	if result_mib == True:
		print "MIB   Check AUTOCH_CNT \t\t\tSUCCESS"
	elif result_mib == False:
		print "Can't Find cur.AUTO_CNT in MIB"
	else:
		print "MIB   Check AUTO_SS_CNT\t\t\t\tFAIL",result_mib
def check_channel_map():
	result=check_flash("cur.CHANNEL_MAP",CHANNEL_MAP)
	if result == True:
		print "FLASH Check CHANNEL_MAP \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.CHANNEL_MAP in FLASH"
	else:
		print "FLASH Check CHANNEL_MAP\t\t\tFAIL",result
	result_mib=check_mib("ss_ch_map",str(CHANNEL_MAP_VALUE),INTERFACE)
	if result_mib == True:
		print "MIB   Check CHANNEL_MAP \t\tSUCCESS"
	elif result_mib == False:
		print "Can't Find cur.CHANNEL_MAP in MIB"
	else:
		print "MIB   Check CHANNEL_MAP\t\t\tFAIL",result_mib
def check_autoch_ss_time():
	result=check_flash("cur.AUTOCH_SS_TIME",AUTOCH_SS_TIME)
	if result == True:
		print "FLASH Check AUTOCH_SS_TIME \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.AUTO_SS_TIME in FLASH"
	else:
		print "FLASH Check AUTOCH_SS_TIME\t\t\t\tFAIL",result
	result_mib=check_mib("autoch_ss_to",AUTOCH_SS_TIME,INTERFACE)
	if result_mib == True:
		print "MIB   Check AUTOCH_SS_TIME \t\tSUCCESS"
	elif result_mib == False:
		print "Can't Find cur.AUTOCH_SS_TIME in MIB"
	else:
		print "MIB   Check AUTOCH_SS_TIME\t\t\t\tFAIL",result_mib
def check_monitor_time():
	result=check_flash("cur.MONITOR_TIME",MONITOR_TIME)
	if result == True:
		print "FLASH Check MONITOR_TIME \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.MONITOR_TIME in FLASH"
	else:
		print "FLASH Check MONITOR_TIME\t\t\t\tFAIL",result
def check_server_ip():
	result=check_flash("cur.KUYUAN_IP_ADDR",SERVER_IP_ADDR)
	if result == True:
		print "FLASH Check SERVER_IP_ADDR \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.KUYUAN_IP_ADDR in FLASH"
	else:
		print "FLASH Check SERVER_IP_ADDR\t\t\t\tFAIL",result
def check_data_type():
	result=check_flash("cur.DATA_TYPE",DATA_TYPE)
	if result == True:
		print "FLASH Check DATA_TYPE \t\t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.DATA_TYPE in FLASH"
	else:
		print "FLASH Check DATA_TYPE\t\t\t\t\tFAIL",result
def check_server_port():
	result=check_flash("cur.KUYUAN_SERVER_PORT",SERVER_PORT)
	if result == True:
		print "FLASH Check SERVER_PORT \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.KUYUAN_SERVER_PORT in FLASH"
	else:
		print "FLASH Check SERVER_PORT \t\t\tFAIL",result
def check_client_port():
	result=check_flash("cur.KUYUAN_CLIENT_PORT",CLIENT_PORT)
	if result == True:
		print "FLASH Check CLIENT_PORT \t\tSUCCESS"
	elif result == False:
		print "Can't Find cur.KUYUAN_CLIENT_PORT in FLASH"
	else:
		print "FLASH Check CLIENT_PORT \t\t\tFAIL",result
def check_flash(param,value):
	result=Tel.write_command("flash all | grep "+param)
	# print result
	if param+"=" in result:
		for i in result.split("\r\n"):
			if param+"=" not in i:
				continue
			param_value=i.split("=")[1]
			if param_value == value:
				return True
			else:
				return param_value,value
	else:
		return False
def check_mib(param,value,iface):
	result=Tel.write_command("iwpriv "+iface+" get_mib "+param)
	if "wlan0     get_mib:" in result:
		for i in result.split("\r\n"):
			if "wlan0     get_mib:" not in i:
				continue
			param_values=i.split(":")[1].strip().split(" ")
			value_3=int(param_values[4])
			value_4=int(param_values[6])
			param_value=str(value_3*256+value_4)
			if param_value == value:
				return True
			else:
				return param_value,value
	else:
		return False
def main():
	global Tel
	for ip in IPLIST:
		Tel=Telnet("guest","guest",ip,"23","#")
		Tel.login()
		check_server_ip()
		check_server_port()
		check_client_port()
		check_ap_mode()
		check_autoch_ss_count()
		calc_ch_map_value()
		check_channel_map()
		check_monitor_time()
		check_autoch_ss_time()
		check_data_type()
		Tel.close()
if __name__ == '__main__':
	main()

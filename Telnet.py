import  telnetlib
import time
class Telnet():
    """docstring for Telnet"""
    def __init__(self, username,passwd,ip,port,finish):
        self.username=username
        self.passwd=passwd
        self.ip=ip
        self.port=port
        self.finish=finish
        self.tn = telnetlib.Telnet(self.ip,self.port,timeout=5)
        self.tn.set_debuglevel(0)
    def login(self):
        try:
            self.tn.read_until('login: ',timeout=5)
            self.tn.write(self.username+'\n')
            self.tn.read_until('Password: ',timeout=5)
            self.tn.write(self.passwd+'\n')
            self.tn.read_until(self.finish)
        except Exception as e:
            print 'telnet not OK',e
            return False
    def write_command(self,command):
        try:
            self.tn.write(command+"\n")
            result=self.tn.read_until(self.finish)
            # print "set command->",command
            return result
        except Exception as e:
            print 'telnet not OK',e
            return False
    def close(self):
        self.tn.close()
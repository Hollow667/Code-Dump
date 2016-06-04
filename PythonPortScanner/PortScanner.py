import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('HiveMind\r\n')
        rezultate = connSkt.rcv(100)
        screenLock.acquire()
        print '[+] %/tcp deschis' %tgtPort
        print '[+] ' + str(rezultate)
    except:
        screenLock.acquire()
        print '[-] %d/tcp inchis' %tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Inaccesibil '%s': Host necunoscut" %tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Rezultat scanare pentru: ' + tgtName[0]
    except:
        print '\n[+] Rezultat scanare pentru: ' + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Instructiuni: %prog ' + \
                                   '-H <host tinta> -p <port tinta>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', \
                      help = 'specifica host-ul tinta')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', \
                      help = 'specifica port[urile] tinta. Porturile se separa prin virgula.')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(' ,')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

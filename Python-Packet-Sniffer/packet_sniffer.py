import socket
from struct import *


def eth_addr(a):
    b = "%.2x-%.2x-%.2x-%.2x-%.2x-%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b


s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))

while True:
    packet = s.recvfrom(65565)

    packet = packet[0]

    eth_length = 14

    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print 'Destinatie MAC : ' + eth_addr(packet[0:6]) + ' Sursa MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)

    if eth_protocol == 8:
        ip_header = packet[eth_length:20+eth_length]

        iph = unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        print 'Versiune : ' + str(version) + ' IP Lungime Header : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Adresa Expediere : ' + str(s_addr) + ' Adresa : ' + str(d_addr)

        if protocol == 6:
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]

            tcph = unpack('!HHLLBBHHH', tcp_header)

            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4

            print ' Port Sursa : ' + str(source_port) + ' Port Destinatar : ' + str(dest_port) + ' Numarul Secvential : ' + str(sequence) + ' Confirmare : ' + str(acknowledgement) + ' TCP lungime header : ' + str(tcph_length)

            h_size = eth_length + iph_length + tcph_length * 4
            data_size = len(packet) - h_size
            data = packet[data_size:]

            print 'Data : ' + data

        elif protocol == 1:
            u = iph_length + eth_length
            icmph_length = 4
            icmp_header = packet[u:u+4]

            icmph = unpack('!BBH', icmp_header)

            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]

            print 'Tipul : ' + str(icmp_type) + ' Cod : ' + str(code) + ' Checksum : ' + str(checksum)

            h_size = eth_length + iph_length + icmph_length
            data_size = len(packet) - h_size

            data = packet[data_size:]

            print 'Date : ' + data

        elif protocol == 17:
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]

            udph = unpack('!HHHH', udp_header)

            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]

            print 'Port Sursa : ' + str(source_port) + ' Port Destinatar : ' + str(dest_port) + ' Lungime : ' + str(length) + ' Checksum : ' + str(checksum)

            h_size = eth_length + iph_length + udph_length
            data_size = len(packet) - h_size

            data = packet[data_size:]

            print 'Date : ' + data

        else:
            print ' Protocolul nu e TCP/UDP/ICMP. '
            print

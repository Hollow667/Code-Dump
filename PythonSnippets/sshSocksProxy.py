


import sys
import chilkat

ssh = chilkat.CkSsh()

#  Unlock the SSH component:
success = ssh.UnlockComponent("Anything for 30-day trial.")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  To use a SOCKS4 or SOCKS5 proxy, simply set the following
#  properties prior to connecting:
#  The SOCKS hostname may be a domain name or
#  IP address:
ssh.put_SocksHostname("www.mysocksproxyserver.com")
ssh.put_SocksPort(1080)
ssh.put_SocksUsername("myProxyLogin")
ssh.put_SocksPassword("myProxyPassword")

#  Set the SOCKS version to 4 or 5 based on the version
#  of the SOCKS proxy server:
ssh.put_SocksVersion(5)

#  Note: SOCKS4 servers only support usernames without passwords.
#  SOCKS5 servers support full login/password authentication.

#  Connect to an SSH server via a SOCKS proxy:

#  Hostname may be an IP address or hostname:
hostname = "192.168.1.108"
port = 22

success = ssh.Connect(hostname,port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Your application is now connected to an SSH server
#  through a SOCKS4 or SOCKS5 proxy.
#  ...


import sys
import chilkat

#  Notice: This example requires Chilkat v9.5.0.51 or greater.

ssh = chilkat.CkSsh()

#  Unlock the SSH component:
success = ssh.UnlockComponent("Anything for 30-day trial.")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  To connect through an HTTP proxy, set the HttpProxyHostname
#  and HttpProxyPort properties to the hostname (or IP address)
#  and port of the HTTP proxy.  Typical port numbers used by
#  HTTP proxy servers are 3128 and 8080.
ssh.put_HttpProxyHostname("www.my-http-proxy.com")
ssh.put_HttpProxyPort(3128)

#  Important:  Your HTTP proxy server must allow non-HTTP
#  traffic to pass.  Otherwise this does not work.

#  Connect to an SSH server via an HTTP proxy:

#  Hostname may be an IP address or hostname:
hostname = "192.168.1.108"
port = 22

success = ssh.Connect(hostname,port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Your application is now connected to an SSH server
#  through an HTTP proxy.
#  ...

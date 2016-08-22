
import sys
import chilkat

#  Starting in v9.5.0.49, all Chilkat classes can be unlocked at once at the beginning of a program
#  by calling UnlockBundle.  It requires a Bundle unlock code.
chilkatGlob = chilkat.CkGlobal()
success = chilkatGlob.UnlockBundle("Anything for 30-day trial.")
if (success != True):
    print(chilkatGlob.lastErrorText())
    sys.exit()

#  This example requires Chilkat version 9.5.0.50 or greater.
tunnel = chilkat.CkSshTunnel()

sshHostname = "www.ssh-serverA.com"
sshPort = 22

#  Connect to an SSH server and establish the SSH tunnel:
success = tunnel.Connect(sshHostname,sshPort)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Authenticate with the SSH server via a login/password
#  or with a public key.
#  This example demonstrates SSH password authentication.
success = tunnel.AuthenticatePw("mySshLogin","mySshPassword")
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Indicate that the background SSH tunnel thread will behave as a SOCKS proxy server
#  with dynamic port forwarding:
tunnel.put_DynamicPortForwarding(True)

#  We may optionally require that connecting clients authenticate with our SOCKS proxy server.
#  To do this, set an inbound username/password.  Any connecting clients would be required to
#  use SOCKS5 with the correct username/password.
#  If no inbound username/password is set, then our SOCKS proxy server will accept both
#  SOCKS4 and SOCKS5 unauthenticated connections.

tunnel.put_InboundSocksUsername("chilkat123")
tunnel.put_InboundSocksPassword("password123")

#  Start the listen/accept thread to begin accepting SOCKS proxy client connections.
#  Listen on port 1080.
success = tunnel.BeginAccepting(1080)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Now that a background thread is running a SOCKS proxy server that forwards connections
#  through an SSH tunnel, it is possible to use any Chilkat implemented protocol that is SOCKS capable,
#  such as HTTP, POP3, SMTP, IMAP, FTP, Socket, etc.  The protocol may use SSL/TLS because the SSL/TLS
#  will be passed through the SSH tunnel to the end-destination.  Also, any number of simultaneous
#  connections may be routed through the SSH tunnel.

tunnelB = chilkat.CkSocket()

#  Indicate that the socket object is to use our portable SOCKS proxy/SSH tunnel running in our background thread.
tunnelB.put_SocksHostname("localhost")
tunnelB.put_SocksPort(1080)
tunnelB.put_SocksVersion(5)
tunnelB.put_SocksUsername("chilkat123")
tunnelB.put_SocksPassword("password123")

#  Open a new SSH tunnel through the existing tunnel (via what we treat as a SOCKS5 proxy,
#  but it is actually a dynamic port-forwarded SSH tunnel).
success = tunnelB.SshOpenTunnel("www.ssh-serverB.com",22)
if (success != True):
    print(tunnelB.lastErrorText())
    sys.exit()

#  Authenticate with ssh-serverB.com
success = tunnelB.SshAuthenticatePw("uname","pwd")
if (success != True):
    print(tunnelB.lastErrorText())
    sys.exit()

#  OK, the SSH tunnel (within a tunnel) is setup.  Now open a channel within the tunnel.
#  Once the channel is obtained, the Socket API may
#  be used exactly the same as usual, except all communications
#  are sent through the channel in the SSH tunnel.
#  Any number of channels may be created from the same SSH tunnel.
#  Multiple channels may coexist at the same time.

#  Connect to an NIST time server and read the current date/time

maxWaitMs = 4000
useTls = False
# channel is a CkSocket
channel = tunnelB.SshOpenChannel("time-c.nist.gov",37,useTls,maxWaitMs)
if (channel == None ):
    print(tunnelB.lastErrorText())
    sys.exit()

#  The time server will send a big-endian 32-bit integer representing
#  the number of seconds since since 00:00 (midnight) 1 January 1900 GMT.
#  The ReceiveInt32 method will receive a 4-byte integer, but returns
#  True or False to indicate success.  If successful, the integer
#  is obtained via the ReceivedInt property.
bigEndian = True
success = channel.ReceiveInt32(bigEndian)
if (success != True):
    print(channel.lastErrorText())

    sys.exit()

dt = chilkat.CkDateTime()
dt.SetFromNtpTime(channel.get_ReceivedInt())

#  Show the current local date/time
bLocalTime = True
print("Current local date/time: " + dt.getAsRfc822(bLocalTime))

#  Close the SSH channel.
success = channel.Close(maxWaitMs)
if (success != True):
    print(channel.lastErrorText())

    sys.exit()

#  Stop the background listen/accept thread:
waitForThreadExit = True
success = tunnel.StopAccepting(waitForThreadExit)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

#  Close the SSH tunnel (would also kick any remaining connected clients).
success = tunnel.CloseTunnel(waitForThreadExit)
if (success != True):
    print(tunnel.lastErrorText())
    sys.exit()

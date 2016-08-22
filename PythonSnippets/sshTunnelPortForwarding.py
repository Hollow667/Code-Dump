
import sys
import chilkat

#  Important: It is helpful to send the contents of the
#  ssh.LastErrorText property when requesting support.

ssh = chilkat.CkSsh()

#  Any string automatically begins a fully-functional 30-day trial.
success = ssh.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Connect to an SSH server:

#  Hostname may be an IP address or hostname:
hostname = "192.168.1.117"
port = 22

success = ssh.Connect(hostname,port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Wait a max of 5 seconds when reading responses..
ssh.put_IdleTimeoutMs(5000)

#  Authenticate using login/password:
success = ssh.AuthenticatePw("chilkat","myPassword")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Open a direct-tcpip channel.  We want the SSH server to connect
#  to www.chilkatsoft.com, port 80 (i.e. the web server).
#  Data sent through the SSH tunnel is forwarded to the remote
#  host:port.  (Note: The remote host:port does not need to be
#  a web server.  It can be anything.  It can be your own
#  customer application server that listens on a port, or any
#  other type of server.)
#  When we read from the SSH channel, we'll be reading data
#  sent from the remote host:port (i.e. the web server in this
#  example).

channelNum = ssh.OpenDirectTcpIpChannel("www.chilkatsoft.com",80)
if (channelNum < 0):
    print(ssh.lastErrorText())
    sys.exit()

#  Build a simple HTTP GET request for http://www.chilkatsoft.com/xyz.html
httpReq = "GET /xyz123.html HTTP/1.1\r\nHost: www.chilkatsoft.com\r\n\r\n"

#  Send the HTTP request:
success = ssh.ChannelSendString(channelNum,httpReq,"ansi")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Get the HTTP response.
#  First read the HTTP response header which ends with a double CRLF.
#  Calling ChannelReceiveUntilMatch will receive until match string is seen,
#  or until a timeout occurs (IdleTimeoutMs property).  ChannelReceiveUntilMatch
#  may read beyond the match string, but it will stop reading as soon as the match
#  string is seen.
caseSensitive = False
matchStr = "\r\n\r\n"
success = ssh.ChannelReceiveUntilMatch(channelNum,matchStr,"ansi",caseSensitive)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Extract the HTTP header from the receive buffer.
#  (GetReceiveTextS extracts up to and including the match string from the receive buffer)

responseHeader = ssh.getReceivedTextS(channelNum,matchStr,"ansi")
print("---- HTTP Response Header ----")
print(responseHeader)

#  Now get the body of the HTTP response (this is the HTML content
#  of http://www.chilkatsoft.com/xyz.html
#  It's possible we've already received the entire HTTP response in the
#  call to ChannelReceiveUntilMatch.  Therefore, we'll poll for any remaining data
#  and wait a max of .2 seconds.

pollTimeoutMs = 200
numBytesRead = ssh.ChannelPoll(channelNum,pollTimeoutMs)
#  We're not checking for an error here.
#  A return value of -2 means that no data was available and the poll simply timed out (not an error)
#  A return value of -1 indicates an error.
#  A return value greater than 0 indicates that additional data was received.

print("---- HTML BODY ----")

#  Extract the remainder of the accumulated data in the internal receive buffer.
#  This should be our HTML body:

htmlBody = ssh.getReceivedText(channelNum,"ansi")
print(htmlBody)

#  Close the channel:
success = ssh.ChannelSendClose(channelNum)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Disconnect
ssh.Disconnect()

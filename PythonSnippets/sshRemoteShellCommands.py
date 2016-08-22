
import sys
import chilkat

#  Important: It is helpful to send the contents of the
#  ssh.LastErrorText property when requesting support.

ssh = chilkat.CkSsh()

#  Any string automatically begins a fully-functional 30-day trial.
success = ssh.UnlockComponent("30-day trial")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  This is the prompt we'll be expecting to find in
#  the output of the remote shell.

myPrompt = "chilkat@ubuntu:~/workspace$"

#  Connect to an SSH server:

#  Hostname may be an IP address or hostname:
hostname = "www.some-ssh-server.com"
port = 22

success = ssh.Connect(hostname,port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Wait a max of 10 seconds when reading responses..
ssh.put_IdleTimeoutMs(10000)

#  Authenticate using login/password:
success = ssh.AuthenticatePw("myLogin","myPassword")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Open a session channel.  (It is possible to have multiple
#  session channels open simultaneously.)

channelNum = ssh.OpenSessionChannel()
if (channelNum < 0):
    print(ssh.lastErrorText())
    sys.exit()

termType = "dumb"
widthInChars = 120
heightInChars = 40
#  Use 0 for pixWidth and pixHeight when the dimensions
#  are set in number-of-chars.
pixWidth = 0
pixHeight = 0
success = ssh.SendReqPty(channelNum,termType,widthInChars,heightInChars,pixWidth,pixHeight)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Start a shell on the channel:
success = ssh.SendReqShell(channelNum)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#   Run the 1st command in the remote shell, which will be to
#   "cd" to a subdirectory.
success = ssh.ChannelSendString(channelNum,"cd workspace\r\n","ansi")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Retrieve the output.
success = ssh.ChannelReceiveUntilMatch(channelNum,myPrompt,"ansi",True)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#   Display what we've received so far.  This clears
#   the internal receive buffer, which is important.
#   After we send the command, we'll be reading until
#   the next command prompt.  If the command prompt
#   is already in the internal receive buffer, it'll think it's
#   already finished...
cmdOutput = ssh.getReceivedText(channelNum,"ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print(cmdOutput)

#   Run the 2nd command in the remote shell, which will be
#   to "ls" the directory.
success = ssh.ChannelSendString(channelNum,"ls\r\n","ansi")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Retrieve and display the output.
success = ssh.ChannelReceiveUntilMatch(channelNum,myPrompt,"ansi",True)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

cmdOutput = ssh.getReceivedText(channelNum,"ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print(cmdOutput)

#   Start the final command in the remote shell.  This example
#   will send a "ls -l" command to retrieve the long format directory listing.
success = ssh.ChannelSendString(channelNum,"ls -l\r\n","ansi")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Send an EOF.  This tells the server that no more data will
#  be sent on this channel.  The channel remains open, and
#  the SSH client may still receive output on this channel.
success = ssh.ChannelSendEof(channelNum)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Read whatever output may already be available on the
#  SSH connection.  ChannelReadAndPoll returns the number of bytes
#  that are available in the channel's internal buffer that
#  are ready to be "picked up" by calling GetReceivedText
#  or GetReceivedData.
#  A return value of -1 indicates failure.
#  A return value of -2 indicates a failure via timeout.

#  The ChannelReadAndPoll method waits
#  for data to arrive on the connection usingi the IdleTimeoutMs
#  property setting.  Once the first data arrives, it continues
#  reading but instead uses the pollTimeoutMs passed in the 2nd argument:
#  A return value of -2 indicates a timeout where no data is received.

pollTimeoutMs = 2000
n = ssh.ChannelReadAndPoll(channelNum,pollTimeoutMs)
if (n < 0):
    print(ssh.lastErrorText())
    sys.exit()

#  Close the channel:
success = ssh.ChannelSendClose(channelNum)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Perhaps we did not receive all of the commands output.
#  To make sure,  call ChannelReceiveToClose to accumulate any remaining
#  output until the server's corresponding "channel close" is received.
success = ssh.ChannelReceiveToClose(channelNum)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

cmdOutput = ssh.getReceivedText(channelNum,"ansi")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

print(cmdOutput)

#  Disconnect
ssh.Disconnect()

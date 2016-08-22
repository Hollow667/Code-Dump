
import sys
import chilkat

#  Important: It is helpful to send the contents of the
#  ssh.LastErrorText property when requesting support.

ssh1 = chilkat.CkSsh()

#  Any string automatically begins a fully-functional 30-day trial.
success = ssh1.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(ssh1.lastErrorText())
    sys.exit()

#  Hostname may be an IP address or domain name:
hostname = "192.168.1.108"
port = 22

#  Connect directly to the 1st SSH server:
success = ssh1.Connect(hostname,port)
if (success != True):
    print(ssh1.lastErrorText())
    sys.exit()

#  Wait a max of 15 seconds when reading responses..
ssh1.put_IdleTimeoutMs(15000)

#  Authenticate using login/password:
success = ssh1.AuthenticatePw("myLogin","myPassword")
if (success != True):
    print(ssh1.lastErrorText())
    sys.exit()

#  Connect through the 1st SSH connection to reach a 2nd SSH server.
#  Note: Any number of SSH connections may be simultaneously tunneled through a single
#  existing SSH connection.
ssh2 = chilkat.CkSsh()
success = ssh2.ConnectThroughSsh(ssh1,"someremoteserver.com",22)
if (success != True):
    print(ssh2.lastErrorText())
    sys.exit()

ssh2.put_IdleTimeoutMs(15000)

#  Authenticate with ssh2...
success = ssh2.AuthenticatePw("myLogin2","myPassword2")
if (success != True):
    print(ssh2.lastErrorText())
    sys.exit()

#  The application may now is connected and authenticated with ssh2.
#  The application can do whatever it desires just as if it was directly
#  connected to ssh2.   For example, the application might open
#  a session channel to send commands or start a remote shell..
channelNum = ssh2.OpenSessionChannel()
if (channelNum < 0):
    print(ssh2.lastErrorText())
    sys.exit()

#  ...
#  ...
#  ...

#  Close the connection with ssh2.  (This closes the the tunnel through ssh1.)
#  The connection with ssh1 is still alive, and may be used for more connections.
ssh2.Disconnect()

#  ...
#  ...
#  ...

ssh1.Disconnect()


import sys
import chilkat

#  Important: It is helpful to send the contents of the
#  sftp.LastErrorText property when sending email
#  to support@chilkatsoft.com

ssh = chilkat.CkSsh()

#  Any string automatically begins a fully-functional 30-day trial.
success = ssh.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Set some timeouts, in milliseconds:
ssh.put_ConnectTimeoutMs(5000)
ssh.put_IdleTimeoutMs(15000)

#  Connect to the SSH server.
#  The standard SSH port = 22
#  The hostname may be a hostname or IP address.

hostname = "www.my-ssh-server.com"
port = 22
success = ssh.Connect(hostname,port)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

key = chilkat.CkSshKey()

#  Read the PEM file into a string variable:
#  (This does not load the PEM file into the key.  The LoadText
#  method is a convenience method for loading the full contents of ANY text
#  file into a string variable.)
privKey = key.loadText("myPrivateKey.pem")
if (key.get_LastMethodSuccess() != True):
    print(key.lastErrorText())
    sys.exit()

#  Load a private key from a PEM string:
#  (Private keys may be loaded from OpenSSH and Putty formats.
#  Both encrypted and unencrypted private key file formats
#  are supported.  This example loads an unencrypted private
#  key in OpenSSH format.  PuTTY keys typically use the .ppk
#  file extension, while OpenSSH keys use the PEM format.
#  (For PuTTY keys, call FromPuttyPrivateKey instead.)
success = key.FromOpenSshPrivateKey(privKey)
if (success != True):
    print(key.lastErrorText())
    sys.exit()

#  Authenticate with the SSH server using the login and
#  private key.  (The corresponding public key should've
#  been installed on the SSH server beforehand.)
success = ssh.AuthenticatePk("myLogin",key)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

print(ssh.lastErrorText())
print("Public-Key Authentication Successful!")


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

#  Begin keyboard authentication..
xmlResponse = ssh.startKeyboardAuth("myLogin")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

#  If a user authentication banner was received, then your app
#  may display it prior to prompting for the password.
print("UserAuthBanner: " + ssh.userAuthBanner())

xml = chilkat.CkXml()

success = xml.LoadXml(xmlResponse)
#  Assume LoadXml succeeds for the example..
if (xml.HasChildWithTag("success") == True):
    print("No password required, already authenticated.")
    sys.exit()

if (xml.HasChildWithTag("error") == True):
    print("Authentication already failed.")
    sys.exit()

#  See the online reference documentation for Chilkat SSH.
#  The XML returned by StartKeyboardAuth will contain an infoRequest
#  with one or more prompts that your application may choose to display.

#  Call ContinueKeyboardAuth, passing in the whatever information is requires (such as the password).
#  Typically, keyboard authentication requires one call to ContinueKeyboardAuth
#  using the password.  Theoretically, the SSH server could prompt for additional pieces
#  of information.  The authentication is completed when the XML returned contains
#  either a "success" or "error" child node.

#  This example asumes only one call to ContinueKeyboardAuth is required.
xmlResponse = ssh.continueKeyboardAuth("myPassword")
if (ssh.get_LastMethodSuccess() != True):
    print(ssh.lastErrorText())
    sys.exit()

success = xml.LoadXml(xmlResponse)
#  Assume LoadXml succeeds for the example..
if (xml.HasChildWithTag("success") == True):
    print("SSH Keyboard Authentication Successful!")
    sys.exit()

if (xml.HasChildWithTag("error") == True):
    print("Authentication failed.")
    sys.exit()

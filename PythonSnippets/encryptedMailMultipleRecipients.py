
import sys
import chilkat

#  The mailman object is used for sending and receiving email.
mailman = chilkat.CkMailMan()

#  Any string argument automatically begins the 30-day trial.
success = mailman.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(mailman.lastErrorText())
    sys.exit()

#  Set the SMTP server.
mailman.put_SmtpHost("smtp.mymailserver.com")

#  Load each recipient's certificate into a Chilkat certificate object.
#  This example loads the certificates from files.  However, the Chilkat
#  certificate object provides other means for loading certificates,
#  such as from in-memory PEM strings, or in-memory binary DER encoded form, etc.
cert1 = chilkat.CkCert()
success = cert1.LoadFromFile("recipient1.cer")
if (success != True):
    print(cert1.lastErrorText())
    sys.exit()

cert2 = chilkat.CkCert()
success = cert2.LoadFromFile("recipient2.cer")
if (success != True):
    print(cert2.lastErrorText())
    sys.exit()

cert3 = chilkat.CkCert()
success = cert3.LoadFromFile("recipient3.cer")
if (success != True):
    print(cert3.lastErrorText())
    sys.exit()

#  Create a new email object
email = chilkat.CkEmail()

email.put_Subject("This email is encrypted and sent to 3 recipients")
email.put_Body("This is an S/MIME encrypted mail sent to 3 recipients")
email.put_From("Chilkat Support <support@chilkatsoft.com>")

#  Make each of the certificates available for encrypting the email
#  by calling AddEncryptCert for each.
success = email.AddEncryptCert(cert1)
if (success == True):
    success = email.AddEncryptCert(cert2)

if (success == True):
    success = email.AddEncryptCert(cert3)

if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  Add 3 recipients to the email (2 TO addresses, and 1 CC address)
success = email.AddTo("Recipient 1","admin@cknotes.com")
success = email.AddTo("Recipient 2","somebody001122@yahoo.com")
success = email.AddCC("Recipient 3","somebody123xyz@gmail.com")

#  Indicate that the email is to be sent encrypted.
email.put_SendEncrypted(True)

#  Send the encrypted email...
success = mailman.SendEmail(email)
if (success != True):
    print(mailman.lastErrorText())
else:
    print("Encrypted Email Sent!")

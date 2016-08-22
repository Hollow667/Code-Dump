import sys
import chilkat

email = chilkat.CkEmail()

#  Add a PFX (or .p12) to be used for decryption
success = email.AddPfxSourceFile("myCert.p12","passwordForP12")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  Loading the .eml automatically decrypts.
success = email.LoadEml("encrypted.eml")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  The email now exists as it was prior to encryption.
#  Your app may access the email's subject, body, attachments,
#  etc. using the Chilkat Email API...

#  Save the decrypted email:
success = email.SaveEml("decrypted.eml")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

print("Success.")

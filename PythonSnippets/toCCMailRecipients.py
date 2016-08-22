import sys
import chilkat

#  An email can have any number of To, CC, or Bcc recipients.
email = chilkat.CkEmail()

success = email.LoadEml("sample.eml")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  It doesn't matter if the email object was loaded from a .eml file,
#  or if it was downloaded from a POP3 or IMAP server.
#  The methods and properties for examining the TO and CC
#  recipients are the same.

#  The number of TO recipients is found in the NumTo property
numTo = email.get_NumTo()

#  Iterate over each TO recipient
if (numTo > 0):
    for i in range(0,numTo):
        print("TO Friendly Name and Address: " + email.getTo(i))
        print("TO Address: " + email.getToAddr(i))
        print("TO Friendly Name: " + email.getToName(i))
        print("---")

#  The number of CC recipients is found in the NumCC property
numCC = email.get_NumCC()

#  Iterate over each CC recipient
if (numCC > 0):
    for i in range(0,numCC):
        print("CC Friendly Name and Address: " + email.getCC(i))
        print("CC Address: " + email.getCcAddr(i))
        print("CC Friendly Name: " + email.getCcName(i))
        print("---")

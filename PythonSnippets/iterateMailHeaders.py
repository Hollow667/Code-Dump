
import sys
import chilkat

email = chilkat.CkEmail()

#  First, load an email from a file.
#  Note: an email object may be loaded from a file, or
#  downloaded directly from a POP3 or IMAP server...

success = email.LoadEml("testReceivedHdrs.eml")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  How many header fields?

n = email.get_NumHeaderFields()
if (n > 0):

    #  Display the name and value of each header:

    for i in range(0,n):
        name = email.getHeaderFieldName(i)
        value = email.getHeaderFieldValue(i)
        print(str(i))
        print(name)
        print(value)


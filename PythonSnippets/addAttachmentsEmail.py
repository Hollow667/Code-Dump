import sys
import chilkat

email = chilkat.CkEmail()

email.put_Subject("This is a test")
email.put_Body("This is a test")
email.put_From("support@chilkatsoft.com")
success = email.AddTo("Chilkat Admin","admin@chilkatsoft.com")

#  To add file attachments to an email, call AddFileAttachment
#  once for each file to be attached.  The method returns
#  the content-type of the attachment if successful, otherwise
#  returns cknull

contentType = email.addFileAttachment("something.pdf")
if (email.get_LastMethodSuccess() != True):
    print(email.lastErrorText())
    sys.exit()

contentType = email.addFileAttachment("something.xml")
if (email.get_LastMethodSuccess() != True):
    print(email.lastErrorText())
    sys.exit()

contentType = email.addFileAttachment("something.zip")
if (email.get_LastMethodSuccess() != True):
    print(email.lastErrorText())
    sys.exit()

success = email.SaveEml("email.eml")
if (success == False):
    print(email.lastErrorText())
    sys.exit()

print("Saved EML!")

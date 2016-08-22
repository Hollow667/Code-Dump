
import sys
import chilkat

#  Create a MailMan for the purpose
#  of unlocking the component.
mailman = chilkat.CkMailMan()
success = mailman.UnlockComponent("anything for 30-day trial")

email = chilkat.CkEmail()

#  Adding attachments, HTML/plain-text bodies, etc can be done
#  in any order:

#  Add an attachment
contentType = email.addFileAttachment("hamlet.zip")
if (email.get_LastMethodSuccess() != True):
    print(email.lastErrorText())
    sys.exit()

#  Add some headers:
email.put_Subject("This is a complex email")
success = email.AddTo("Chilkat Support","support@chilkatsoft.com")
email.put_From("Matt <matt@chilkatsoft.com>")

#  Add a plain-text body:
success = email.AddPlainTextAlternativeBody("This is the plain-text body")

#  Add an image that will be embedded in the HTML body.
contentIdDude = email.addRelatedFile("dude.gif")
if (email.get_LastMethodSuccess() != True):
    print(email.lastErrorText())
    sys.exit()

#  Update the CONTENT_ID_DUDE to the actual content ID when sending the email.
success = email.SetReplacePattern("CONTENT_ID_DUDE",contentIdDude)

#  Add an HTML body:

html = "<html><body><b>This is the HTML body</b><br><img src=\"cid:CONTENT_ID_DUDE\"></body></html>"

success = email.AddHtmlAlternativeBody(html)

#  Save the email as a .eml

success = email.SaveEml("complex.eml")
if (success != True):
    print(email.lastErrorText())
else:
    print("Created email!")


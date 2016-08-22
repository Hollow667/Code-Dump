import chilkat

#  An email can have any number of To, CC, or Bcc recipients.
email = chilkat.CkEmail()

#  One recipient per AddTo, AddCC, or AddBcc call may be added:
#  The 1st argument is the friendly name, the 2nd argument
#  is the email address.
success = email.AddTo("Chilkat Support","support@chilkatsoft.com")
success = email.AddTo("Person 1","person1@chilkatsoft.com")
success = email.AddTo("Person 2","person2@chilkatsoft.com")
success = email.AddTo("Person 3","person3@chilkatsoft.com")

#  This email now has 4 "To" recipients.

#  Now add some CC recipients:
#  Note: the friendly name may be empty if desired...
success = email.AddCC("Person 4","person4@chilkatsoft.com")
success = email.AddCC("","person5@chilkatsoft.com")
success = email.AddCC("Person 6","person6@chilkatsoft.com")

#  Now the email has 7 total recipients (3 "To" and 4 "CC")

#  Now add some Bcc recipients:
success = email.AddBcc("","person7@chilkatsoft.com")
success = email.AddBcc("Person 8","person8@chilkatsoft.com")

#  Clear all recipients via ClearTo, ClearCC, and ClearBcc:
email.ClearTo()
email.ClearCC()
email.ClearBcc()

#  The email is now back to 0 recipients...

#  Add recipients just as before, but this time use
#  AddMultipleTo, AddMultipleCC, and AddMultipleBcc.
#  These methods accept a comma-separated list of
#  email addresses.  For example:

success = email.AddMultipleTo("Chilkat Support <support@chilkatsoft.com>, Person 1 <person1@chilkatsoft.com>, Person 2 <person2@chilkatsoft.com>, Person 3 <person3@chilkatsoft.com>")

success = email.AddMultipleCC("Person 4 <person4@chilkatsoft.com>, person5@chilkatsoft.com, Person 6 <person6@chilkatsoft.com>")

success = email.AddMultipleBcc("person7@chilkatsoft.com, Person 8 <person8@chilkatsoft.com>")

email.put_Body("this is a test")
email.put_Subject("this is a test")

#  Display the MIME:
print(email.getMime())

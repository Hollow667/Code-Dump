import sys
import chilkat

email = chilkat.CkEmail()

#  A DSN email is a report about the attempt to delivery
#  an email.  It is usually a report that indicates failure or
#  or a delay in delivery.  The DSN is typically sent back to
#  the sender of an email.

#  IMPORTANT:
#  Note: Please be careful in sending automated DSN's.
#  It is important to be aware of an issue called "backscatter".
#  See the Wikipedia article here:  http://en.wikipedia.org/wiki/Backscatter_%28e-mail%29

#  The CreateDsn method will be called to create a new
#  DSN email based upon the email object calling CreateDsn.
#  The email object instance used to call CreateDsn would
#  typically be an email received from a POP3 or IMAP server.
#  In this case, to simplify the example, we'll load the email
#  from a .eml file.

#  This example will be creating a DSN for "someEmail.eml"
success = email.LoadEml("someEmail.eml")
if (success != True):
    print(email.lastErrorText())
    sys.exit()

#  The DSN created by CreateDsn will contain a
#  "message/delivery-status" MIME sub-part that will
#  be composed of a number of name-value pairs.
#  See RFC 3464 ( http://tools.ietf.org/html/rfc3464 )
#  The name-value content for this part is passed
#  as XML to CreateDsn. This part of the example
#  prepares the XML:
xml = chilkat.CkXml()

#  For this example, we're just adding a few name-value pairs.
#  These should not be considered to be correct, required or
#  even sensible -- it's simply for the example.
xml.put_Tag("DeliveryStatusFields")
xml.NewChild2("Status","5.1.2 (bad destination system: no such domain)")
xml.NewChild2("Diagnostic-Code","smtp; Permanent failure: no such domain")
xml.NewChild2("X-BounceCategory","bad-domain")

xmlStr = xml.getXml()

#  The last argument to be passed to CreateDsn will be a boolean
#  indicating whether to include the entire MIME of the calling
#  email object in the DSN, or only the header.
#  It may make sense to include the entire email for small emails,
#  but for large emails (with large attachments) it's probably
#  best to make the DSN header-only.
bHeaderOnly = True

#  The first argument to be passed to CreateDsn will
#  be a human-readable explanation that will be placed
#  into the 1st MIME part of the DSN (see RFC 3464).
humanReadableExplanation = "Blah blah blah. The delivery of this email failed. Blah blah blah"

#  OK, we're ready to create DSN....

# dsnEmail is a CkEmail
dsnEmail = email.CreateDsn(humanReadableExplanation,xmlStr,bHeaderOnly)

if (not (dsnEmail == None )):
    #  Show the MIME of the source (original) email:
    print(email.getMime())

    print("**************************************")

    #  Show the MIME of the DSN email:
    print(dsnEmail.getMime())
else:
    print(email.lastErrorText())

#  Sample output showing the MIME of the original email,
#  and the DSN email created based upon it:


/*-

X-Account-Key: account2
X-UIDL: 0D154945439D42BD80F180F6D9DE4D82
Received: with MailEnable Postoffice Connector;
	 Tue, 21 Jun 2011 09:21:23 -0400
Received: from qmta14.emeryville.ca.mail.comcast.net ([76.96.227.212]) by chilkatsoft.com with MailEnable ESMTP;
	 Tue, 21 Jun 2011 09:21:22 -0400
Received: from omta03.emeryville.ca.mail.comcast.net ([76.196.30.27]) by qmta14.emeryville.ca.mail.comcast.net with comcast id yd4k1g0050b6N64AEdLW9x;
	 Tue, 21 Jun 2011 13:20:30 +0000
Received: from [127.0.0.1] ([67.175.202.103]) by omta03.emeryville.ca.mail.comcast.net with comcast id ydLV1g00n2EMkZ78PdLWxi;
	 Tue, 21 Jun 2011 13:20:31 +0000
Message-ID: <4E009AA4.3090205@chilkatsoft.com>
Date: Tue, 21 Jun 2011 08:20:36 -0500
From: Chilkat Software <admin@chilkatsoft.com>
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.17) Gecko/20110414 Thunderbird/3.1.10
MIME-Version: 1.0
To: Chilkat Support <support@chilkatsoft.com>
Subject: test 123
Content-Type: text/plain; charset=ISO-8859-1; format=flowed
Content-Transfer-Encoding: 7bit
Return-Path: <>
X-Antivirus: avast! (VPS 110621-0, 06/21/2011), Inbound message
X-Antivirus-Status: Clean

This is a test 123



**************************************
Content-Type: multipart/report; report-type=delivery-status;
	 boundary="------------070202040604030701060106"

--------------070202040604030701060106
Content-Type: text/plain
Content-Transfer-Encoding: 7bit

Blah blah blah. The delivery of this email failed. Blah blah blah
--------------070202040604030701060106
Content-Type: message/delivery-status

Status: 5.1.2 (bad destination system: no such domain)
Diagnostic-Code: smtp; Permanent failure: no such domain
X-BounceCategory: bad-domain

--------------070202040604030701060106
Content-Type: text/rfc822-headers

X-Account-Key: account2
X-UIDL: 0D154945439D42BD80F180F6D9DE4D82
Received: with MailEnable Postoffice Connector;
	 Tue, 21 Jun 2011 09:21:23 -0400
Received: from qmta14.emeryville.ca.mail.comcast.net ([76.96.227.212]) by chilkatsoft.com with MailEnable ESMTP;
	 Tue, 21 Jun 2011 09:21:22 -0400
Received: from omta03.emeryville.ca.mail.comcast.net ([76.196.30.27]) by qmta14.emeryville.ca.mail.comcast.net with comcast id yd4k1g0050b6N64AEdLW9x;
	 Tue, 21 Jun 2011 13:20:30 +0000
Received: from [127.0.0.1] ([67.175.202.103]) by omta03.emeryville.ca.mail.comcast.net with comcast id ydLV1g00n2EMkZ78PdLWxi;
	 Tue, 21 Jun 2011 13:20:31 +0000
Message-ID: <4E009AA4.3090205@chilkatsoft.com>
Date: Tue, 21 Jun 2011 08:20:36 -0500
From: Chilkat Software <admin@chilkatsoft.com>
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.17) Gecko/20110414 Thunderbird/3.1.10
MIME-Version: 1.0
To: Chilkat Support <support@chilkatsoft.com>
Subject: test 123
Content-Type: text/plain; charset=ISO-8859-1; format=flowed
Content-Transfer-Encoding: 7bit
Return-Path: <>
X-Antivirus: avast! (VPS 110621-0, 06/21/2011), Inbound message
X-Antivirus-Status: Clean
--------------070202040604030701060106--



*/

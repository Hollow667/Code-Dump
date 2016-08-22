
import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

s = "A friend called me up the other day and talked about investing in a dot-com that sells lobsters. Internet lobsters. Where will this end? --Donald Trump"

#  Indicate that no encryption should be performed,
#  only encoding/decoding.
crypt.put_CryptAlgorithm("none")
crypt.put_EncodingMode("base64")

#  Other possible EncodingMode settings are:
#  "quoted-printable", "hex", "uu", "base32", and "url"

strBase64 = crypt.encryptStringENC(s)

print(strBase64)

decoded = crypt.decryptStringENC(strBase64)

print(decoded)

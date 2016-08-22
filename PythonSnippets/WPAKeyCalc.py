import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  The "ps" is the WPA passphrase
pw = "password"
pwCharset = "ansi"

#  Hash algorithms may be: sha1, md2, md5, etc.
hashAlg = "sha1"

#  Specify the SSID in hex:
#  For example, if the SSID is "ABC", then the
#  hex values for these us-ascii chars is "414243"
ssidHex = "414243"

#  The WPA key calculation will always use 4096 iterations.
iterationCount = 4096

#  The WPA hex output should be 256 bits.
outputBitLen = 256

#  Indicate that "hex" is to be returned.
enc = "hex"

wpaHexKey = crypt.pbkdf2(pw,pwCharset,hashAlg,ssidHex,iterationCount,outputBitLen,enc)

print(wpaHexKey)

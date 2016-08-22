
import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  http://www.di-mgt.com.au/cryptoKDFs.html#examplespbkdf

pw = "password"
pwCharset = "ansi"
#  Hash algorithms may be: sha1, md2, md5, etc.
hashAlg = "sha1"
#  The salt should be 8 bytes:
saltHex = "78578E5A5D63CB06"
iterationCount = 2048
#  Derive a 192-bit key from the password.
outputBitLen = 192

#  The derived key is returned as a hex or base64 encoded string.
#  (Note: The salt argument must be a string that also uses
#  the same encoding.)
enc = "hex"

hexKey = crypt.pbkdf2(pw,pwCharset,hashAlg,saltHex,iterationCount,outputBitLen,enc)

print(hexKey)

#  The output should have this value:
#  BFDE6BE94DF7E11DD409BCE20A0255EC327CB936FFE93643

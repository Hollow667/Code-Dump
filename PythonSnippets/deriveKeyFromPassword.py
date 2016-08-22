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
iterationCount = 1000
#  Derive a 128-bit key from the password.
outputBitLen = 128

#  The derived key is returned as a hex or base64 encoded string.
#  (Note: The salt argument must be a string that also uses
#  the same encoding.)
enc = "hex"

hexKey = crypt.pbkdf1(pw,pwCharset,hashAlg,saltHex,iterationCount,outputBitLen,enc)

print(hexKey)

#  The output should have this value:
#  DC19847E05C64D2FAF10EBFB4A3D2A20

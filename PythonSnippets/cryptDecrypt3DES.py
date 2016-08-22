import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial.")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Specify 3DES for the encryption algorithm:
crypt.put_CryptAlgorithm("3des")

crypt.put_CipherMode("ecb")

#  For 2-Key Triple-DES, use a key length of 128
#  (Given that each byte's msb is a parity bit, the strength is really 112 bits).
crypt.put_KeyLength(128)

#  Pad with zeros
crypt.put_PaddingScheme(3)

#  EncodingMode specifies the encoding of the output for
#  encryption, and the input for decryption.
#  It may be "hex", "url", "base64", or "quoted-printable".
crypt.put_EncodingMode("hex")

#  Let's create a secret key by using the MD5 hash of a password.
#  The Digest-MD5 algorithm produces a 16-byte hash (i.e. 128 bits)
crypt.put_HashAlgorithm("md5")
keyHex = crypt.hashStringENC("secretPassword")

#  Set the encryption key:
crypt.SetEncodedKey(keyHex,"hex")

#  Encrypt
encStr = crypt.encryptStringENC("The quick brown fox jumped over the lazy dog")
print(encStr)

#  Now decrypt:
decStr = crypt.decryptStringENC(encStr)
print(decStr)


import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Set properties for PBES1 encryption:

crypt.put_CryptAlgorithm("pbes1")
crypt.put_PbesPassword("mySecretPassword")

#  Set the underlying PBE algorithm (and key length):
#  For PBES1, the underlying algorithm must be either
#  56-bit DES or 64-bit RC2
#  (this is according to the PKCS#5 specifications at
#  http://www.rsa.com/rsalabs/node.asp?id=2127   )
crypt.put_PbesAlgorithm("rc2")
crypt.put_KeyLength(64)

#  The salt for PBKDF1 is always 8 bytes:
crypt.SetEncodedSalt("0102030405060708","hex")

#  A higher iteration count makes the algorithm more
#  computationally expensive and therefore exhaustive
#  searches (for breaking the encryption) is more difficult:
crypt.put_IterationCount(1024)

#  A hash algorithm needs to be set for PBES1:
crypt.put_HashAlgorithm("sha1")

#  Indicate that the encrypted bytes should be returned
#  as a hex string:
crypt.put_EncodingMode("hex")

plainText = "To be encrypted."

encryptedText = crypt.encryptStringENC(plainText)

print(encryptedText)

#  Now decrypt:
decryptedText = crypt.decryptStringENC(encryptedText)

print(decryptedText)


import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Set properties for PBES2 encryption:

crypt.put_CryptAlgorithm("pbes2")
crypt.put_PbesPassword("mySecretPassword")

#  Set the underlying PBE algorithm (and key length):
crypt.put_PbesAlgorithm("rc2")
crypt.put_KeyLength(128)
#  Only required for the RC2 algorithm:
crypt.put_Rc2EffectiveKeyLength(128)

#  By definition, the block encryption algorithm (RC2 or whichever
#  was selected) will run in CBC mode.  Therefore, we need
#  an IV.  The IV is equal in length to the block size of the
#  algorithm.  RC2 has a block size of 8 bytes (regardless of
#  key length), so set the IV to some value that is 8 bytes
#  in length:
crypt.SetEncodedIV("0000000000000000","hex")

#  Give it some salt:
crypt.SetEncodedSalt("0102030405060708","hex")

#  A higher iteration count makes the algorithm more
#  computationally expensive and therefore exhaustive
#  searches (for breaking the encryption) is more difficult:
crypt.put_IterationCount(1024)

#  A hash algorithm needs to be set for PBES2:
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

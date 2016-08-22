
import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print("Crypt component unlock failed")
    sys.exit()

#  Set the encryption algorithm to ARC4:
crypt.put_CryptAlgorithm("arc4")

#  We want the encrypted output to be a hex-encoded string.
crypt.put_EncodingMode("hex")

key = "000102030405060708090A0B0C0D0E0F"

data = "12345678"

#  Key length is 128 bits in this example.
crypt.put_KeyLength(128)
crypt.SetEncodedKey(key,"hex")

#  Generate 16 "random" 8-byte blocks, encoded as hex strings.
#  This example will generate the identical output each time
#  it is run.

for i in range(0,16):
    cipherHex = crypt.encryptStringENC(data)
    print(data)
    print(cipherHex)
    data = cipherHex



import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

s = "The quick brown fox jumps over the lazy dog"

crypt.put_HashAlgorithm("sha1")
crypt.put_EncodingMode("hex")

#  Other possible EncodingMode settings are:
#  "quoted-printable", "base64", and "url"

hash = crypt.hashStringENC(s)
print("SHA1: " + hash)

#  Hash using MD2
crypt.put_HashAlgorithm("md2")
hash = crypt.hashStringENC(s)
print("MD2: " + hash)

#  Hash using MD5
crypt.put_HashAlgorithm("md5")
hash = crypt.hashStringENC(s)
print("MD5: " + hash)

#  Note: SHA-2 is a set of cryptographic hash functions (SHA-224, SHA-256, SHA-384, SHA-512)

#  Hash using SHA-256
crypt.put_HashAlgorithm("sha256")
hash = crypt.hashStringENC(s)
print("SHA256: " + hash)

#  Hash using SHA-384
crypt.put_HashAlgorithm("sha384")
hash = crypt.hashStringENC(s)
print("SHA384: " + hash)

#  Hash using SHA-512
crypt.put_HashAlgorithm("sha512")
hash = crypt.hashStringENC(s)
print("SHA512: " + hash)

#  Hash using HAVAL
#  There are two additional properties relevant to HAVAL:
#  HavalRounds, and KeyLength.
#  HavalRounds can have values of 3, 4, or 5.
#  KeyLength can have values of 128, 160, 192, 224, or 256
crypt.put_HashAlgorithm("haval")
crypt.put_HavalRounds(5)
crypt.put_KeyLength(256)
hash = crypt.hashStringENC(s)
print("Haval: " + hash)

#  Hashes for "The quick brown fox jumps over the lazy dog"

#  SHA1:
#  2FD4E1C67A2D28FCED849EE1BB76E7391B93EB12

#  MD2:
#  03D85A0D629D2C442E987525319FC471

#  MD5:
#  9E107D9D372BB6826BD81D3542A419D6

#  SHA256:
#  D7A8FBB307D7809469CA9ABCB0082E4F8D5651E46D3CDB762D02D0BF37C9E592

#  SHA384:
#  CA737F1014A48F4C0B6DD43CB177B0AFD9E5169367544C494011E3317DBF9A509CB1E5DC1E85A941BBEE3D7F2AFBC9B1

#  SHA512:
#  07E547D9586F6A73F73FBAC0435ED76951218FB7D0C8D788A309D785436BBB642E93A252A954F23912547D1E8A3B5ED6E1BFD7097821233FA0538F3DB854FEE6

#  Haval:
#  B89C551CDFE2E06DBD4CEA2BE1BC7D557416C58EBB4D07CBC94E49F710C55BE4

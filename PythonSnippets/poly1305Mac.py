


import sys
import chilkat

crypt = chilkat.CkCrypt2()

success = crypt.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Set the MAC algorithm to poly1305
crypt.put_MacAlgorithm("poly1305")

#  EncodingMode specifies the encoding of the output for
#  encryption, and the input for decryption.
#  Valid modes are (case insensitive) "Base64", "modBase64", "Base32", "Base58", "UU",
#  "QP" (for quoted-printable), "URL" (for url-encoding), "Hex",
#  "Q", "B", "url_oauth", "url_rfc1738", "url_rfc2396", and "url_rfc3986".
crypt.put_EncodingMode("hex")

#  Poly1305 always uses a 32-byte (256-bit) MAC key.
keyHex = "1c9240a5eb55d38af333888604f6b5f0473917c1402b80099dca5cbc207075c0"
success = crypt.SetMacKeyEncoded(keyHex,"hex")

plainText = "'Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe:\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe."

#  The computed tag should match the Tag shown below.
#  (Note: hexidecimal encoding is case insensitive.)
encTag = crypt.macStringENC(plainText)
print(encTag)

#  Here is the Test Vector data copied from RFC 7539

#   Test Vector #4:
#   ==============
#
#   One-time Poly1305 Key:
#   000  1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0  ..@..U...3......
#   016  47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0  G9..@+....\. pu.
#
#   Text to MAC:
#   000  27 54 77 61 73 20 62 72 69 6c 6c 69 67 2c 20 61  'Twas brillig, a
#   016  6e 64 20 74 68 65 20 73 6c 69 74 68 79 20 74 6f  nd the slithy to
#   032  76 65 73 0a 44 69 64 20 67 79 72 65 20 61 6e 64  ves.Did gyre and
#   048  20 67 69 6d 62 6c 65 20 69 6e 20 74 68 65 20 77   gimble in the w
#   064  61 62 65 3a 0a 41 6c 6c 20 6d 69 6d 73 79 20 77  abe:.All mimsy w
#   080  65 72 65 20 74 68 65 20 62 6f 72 6f 67 6f 76 65  ere the borogove
#   096  73 2c 0a 41 6e 64 20 74 68 65 20 6d 6f 6d 65 20  s,.And the mome
#   112  72 61 74 68 73 20 6f 75 74 67 72 61 62 65 2e     raths outgrabe.
#
#   Tag:
#   000  45 41 66 9a 7e aa ee 61 e7 08 dc 7c bc c5 eb 62  EAf.~..a...|...b


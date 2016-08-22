import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Indicate the public-key encryption is to be used.
#  Do this by setting the encryption algorithm equal
#  to "PKI" (an acroynm for public-key infrastructure).
crypt.put_CryptAlgorithm("PKI")

#  Indicate the inner symmetric encryption algorithm to be used.
#  possible values are "aes", "des", "3des", and "rc2".
#  For this example, we'll use 256-bit AES encryption.
crypt.put_Pkcs7CryptAlg("aes")
crypt.put_KeyLength(256)

#  To encrypt, only a certificate w/ public key is needed.
#  (The certificate w/ private key is required for decryption.)

#  The LoadFromFile method can load virtually any certificate format:
#  1. DER encoded binary X.509 (.CER)
#  2. Base-64 encoded X.509 (.CER)
#  3. Cryptographic Message Syntax Standard - PKCS #7 Certificates (.P7B)
#  4. PEM format
encryptCert = chilkat.CkCert()
success = encryptCert.LoadFromFile("/Users/chilkat/testData/cer/acme.cer")
if (success != True):
    print(encryptCert.lastErrorText())
    sys.exit()

#  Tell the crypt object to use the certificate for encrypting:
crypt.AddEncryptCert(encryptCert)

#  Encrypt a file, producing a .p7m as output.
#  The input file is unchanged, the output .p7m contains the encrypted
#  contents of the input file.
inFile = "/Users/chilkat/testData/pdf/sample.pdf"
outFile = "/Users/chilkat/testData/p7m/sample.pdf.p7m"
success = crypt.CkEncryptFile(inFile,outFile)
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  For demonstration purposes, a different instance of the object will be used
#  for decryption.
decrypt = chilkat.CkCrypt2()

#  To decrypt, the certificate w/ private key is required.  A PFX (also known
#  as PKCS#12) is a common secure container for certs and private keys.
pfxFilename = "/Users/chilkat/testData/pfx/acme.pfx"
pfxPassword = "secret"

#  Tell the component to look in the PFX file for certs and private keys.
success = decrypt.AddPfxSourceFile(pfxFilename,pfxPassword)
if (success != True):
    print(decrypt.lastErrorText())
    sys.exit()

#  Tell the decrypt object that PKI (public key encryption) is to be used
#  for decryptiong.
decrypt.put_CryptAlgorithm("PKI")
#  There is no need to set the Pkcs7Alg or KeyLength because this information
#  is contained within the .p7m

#  Decrypt the .p7m
inFile = "/Users/chilkat/testData/p7m/sample.pdf.p7m"
outFile = "/Users/chilkat/testData/pdf/recovered.pdf"
success = decrypt.CkDecryptFile(inFile,outFile)
if (success == False):
    print(decrypt.lastErrorText())
    sys.exit()

print("Success!")

import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Use a digital certificate and private key from a PFX file (.pfx or .p12).
pfxPath = "myCertAndKey.pfx"
pfxPassword = "test123"

success = crypt.AddPfxSourceFile(pfxPath,pfxPassword)
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Set the  outPath to whatever is appropriate.
#  If you are decrypting a PDF, your output might be "out.pdf"...
inPath = "smime.p7m"
outPath = "original.txt"

#  Indicate that we're doing public key decryption (i.e. PKCS7)
crypt.put_CryptAlgorithm("pki")

success = crypt.CkDecryptFile(inPath,outPath)
if (success == False):
    print(crypt.lastErrorText())
    sys.exit()

print("Success.")

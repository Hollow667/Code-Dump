import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

#  Use a digital certificate and private key from a PFX file (.pfx or .p12).
signingCertSubject = "Acme Inc"
pfxFilename = "/Users/chilkat/testData/pfx/acme.pfx"
pfxPassword = "test123"

certStore = chilkat.CkCertStore()
success = certStore.LoadPfxFile(pfxFilename,pfxPassword)
if (success != True):
    print(certStore.lastErrorText())
    sys.exit()

# cert is a CkCert
cert = certStore.FindCertBySubjectCN(signingCertSubject)
if (cert == None ):
    print("Failed to find certificate by subject common name.")
    sys.exit()

#  Tell the crypt component to use this cert.
success = crypt.SetSigningCert(cert)

#  We can sign any type of file, creating a .p7m as output:
inFile = "/Users/chilkat/testData/pdf/sample.pdf"
outputFile = "/Users/chilkat/testData/p7m/sample.pdf.p7m"
success = crypt.CreateP7M(inFile,outputFile)
if (success == False):
    print(crypt.lastErrorText())

    sys.exit()

#  Verify and restore the original file:
success = crypt.SetVerifyCert(cert)

inFile = outputFile
outputFile = "/Users/chilkat/testData/pdf/restored.pdf"

success = crypt.VerifyP7M(inFile,outputFile)
if (success == False):
    print(crypt.lastErrorText())

    sys.exit()

print("Success!")

import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

certStore = chilkat.CkCertStore()

#  Load a PFX file into a certificate store object.
success = certStore.LoadPfxFile("myPfx.pfx","pfxPassword")
if (success != True):
    print(certStore.lastErrorText())
    sys.exit()

#  Get the certificate by subject common name.
#  This should be the cert within the PFX that also
#  has a private key (also stored within the PFX).
# cert is a CkCert
cert = certStore.FindCertBySubjectCN("myCert")
if (cert == None ):
    print(certStore.lastErrorText())
    sys.exit()

#  Tell the crypt object to use the certificate for signing:
success = crypt.SetSigningCert(cert)

#  Sign a file, producing a .p7m as output.
#  The input file is unchanged, the test.p7m contains the
#  contents of the input file and the signature.
inFile = "test.txt"
outFile = "testp7m"
success = crypt.CreateP7M(inFile,outFile)
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

print("Success!")

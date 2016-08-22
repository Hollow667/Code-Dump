import sys
import chilkat

crypt = chilkat.CkCrypt2()

#  Any string argument automatically begins the 30-day trial.
success = crypt.UnlockComponent("30-day trial")
if (success != True):
    print(crypt.lastErrorText())
    sys.exit()

outputFile = "/Users/chilkat/testData/pdf/sample.pdf"
inFile = "/Users/chilkat/testData/p7m/sample.pdf.p7m"

#  Verify and restore the original file:
success = crypt.VerifyP7M(inFile,outputFile)
if (success == False):
    print(crypt.lastErrorText())
    sys.exit()

print("Success!")

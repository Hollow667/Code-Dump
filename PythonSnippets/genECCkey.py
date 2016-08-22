
import sys
import chilkat

#  All Chilkat classes can be unlocked at once at the beginning of a program
#  by calling UnlockBundle.  It requires a Bundle unlock code.
chilkatGlob = chilkat.CkGlobal()
success = chilkatGlob.UnlockBundle("Anything for 30-day trial.")
if (success != True):
    print(chilkatGlob.lastErrorText())
    sys.exit()

#  Create a Fortuna PRNG and seed it with system entropy.
#  This will be our source of random data for generating the ECC private key.
fortuna = chilkat.CkPrng()
entropy = fortuna.getEntropy(32,"base64")
success = fortuna.AddEntropy(entropy,"base64")

ecc = chilkat.CkEcc()

#  Generate a random ECC private key on the secp256r1 curve.
#  Chilkat also supports other curves, such as secp384r1, secp521r1, and secp256k1.

# privKey is a CkPrivateKey
privKey = ecc.GenEccKey("secp256r1",fortuna)
if (privKey == None ):
    print(ecc.lastErrorText())
    sys.exit()

#  Save the private key to PKCS8 encrypted PEM
#  (The private key can be saved in a variety of different formats. See the online reference documentation.)
success = privKey.SavePkcs8EncryptedPemFile("pemPassword","myPemFiles/eccKey123.pem")
if (success != True):
    print(privKey.lastErrorText())

print("finished.")

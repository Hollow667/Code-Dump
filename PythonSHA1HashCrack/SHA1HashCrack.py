
import hashlib
import optparse

def crackSHA1Hash(_file,_hash):
        _wordlistfile = open(_file,"r")
        cracked = False
        for word in _wordlistfile:
                _purgedword = word.strip()
                sha1 = hashlib.sha1()
                sha1.update(_purgedword)
                _wordhash = sha1.hexdigest()
                if _wordhash == _hash:
                        print "[+] Hash ("+_hash+ ") cracked: "+_purgedword
                        cracked = True
                        break
        if(not cracked):
                print "[-] Unable to crack the hash."
                
def main():
        argparser = optparse.OptionParser("Utilizare -f <fisier wordlist> -p <hash>")
        argparser.add_option('-f', dest='filename',type='string',help='Please specify a word list')
        argparser.add_option('-p', dest='passhash',type='string',help='Please specify a password hash to be cracked')
        (options, arg) = argparser.parse_args()
        if (options.filename == None) | (options.passhash == None):
                print argparser.usage
                exit(0)
        else:
                filename = options.filename
                passhash = options.passhash
                print "[*] Cracking hash ..."
        crackSHA1Hash(filename,passhash)

if __name__ == '__main__':
        main()

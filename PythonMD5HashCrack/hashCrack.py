import hashlib
import os
import sys
import datetime

startTime = datetime.datetime.now()

#DEBUG MESSAGES
def error(msg)     : print '[!] - ' + msg
def errorExit(msg) : raise SystemExit('[!] - ' + msg)

def md5(string): return hashlib.md5(string).hexdigest()

#PERMUTATION BUILDER
def xpermutation(characters, size):
    if size == 0:
        yield []
    else:
        for x in xrange(len(characters)):
            for y in xpermutation(characters[:x] + characters[x:], size - 1):
                yield [characters[x]] + y

#BRUTE FORCE
def bruteForce(hash):
    attempt = 0
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    maxLength = xrange(0,25)
    stringBuilder = ''
    for length in maxLength:
        for x in xpermutation(characters, length):
            permutation = stringBuilder + ''.join(x)
            attempt = attempt + 1
            if md5(permutation) == hash:
                end_time = str(datetime.datetime.now() - startTime).split('.')[0]
                print '[' + str(attempt) + '] - ' + permutation + ' - CRACKED! Durata procesului ' + end_time
                raw_input('\nApasa <ENTER> pentru EXIT...')
                sys.exit()
            else:
                print '[' + str(attempt) + '] - ' + permutation
    errorExit('MD5 Crack esuat.')

#START
if os.name == 'nt' : os.system('cls')
else : os.system('clear')
if sys.version_info.major != 2 or sys.version_info.minor != 7:
    errorExit('Necesita versiunea 2.7 de Python.')
if len(sys.argv) == 2:
    if len(sys.argv[1]) == 32 and sys.argv[1].isalnum():
	bruteForce(sys.argv[1])
    else:
	error('Hash MD5 invalid!')
	errorExit('Utilizare : hashCrack.py [HASH]')
else:
    error('Argumentele necesare scriptului nu au fost gasite.')
    errorExit('Utilizare : hashCrack.py [HASH]')

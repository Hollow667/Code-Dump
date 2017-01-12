# Random Alphabetical Encryption Key Generator
# Zero Davila 2017
import random

characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('1234567890')
symbols = list('~!@#$%^&*()_-+|}{][":?><,./;\'\ ')
total = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_-+|}{][":?><,./;\'\ ')
resultChr = []
resultNum = []
resultSym = []
resultMix = []
resultTtl = []

print 'How many alphabets to generate?'
alphabet_number = raw_input('NUMBER> ')

# METHOD TO STRIP OFF THE "'" OFF OF LIST ELEMENTS
def stripChr(stripMe):
    for char in stripMe:
	char.lstrip('\'')
	char.rstrip('\'')
	print char ,

def writeHeader(filely, header):
    with open(filely, 'a') as f:
        for char in header:
            char.lstrip('\'')
            char.rstrip('\'')
            f.write(str(char) + ' ')
        f.write('\n\n')
        f.close()

# METHOD TO WRITE TO FILE
def writeToFile(writeThis, filely, total):
    for char in writeThis:
        char.lstrip('\'')
        char.rstrip('\'')
        with open(filely, 'a') as f:
            f.write(str(char) + ' ')
            f.close()
    with open(filely, 'a') as f:
        f.write('\n')
        f.close()

def clearFile(filely):
    with open(filely, 'w') as f:
        f.write('')
        f.close()

# METHOD TO RANDOMIZE WITHOUT DUPLICATIONS
def randomize(listerine, colection, length):
    n = 0
    clearFile('key')
    writeHeader('key', total)
    while n < int(alphabet_number):
        while len(listerine) < len(length):
            rand = random.choice(colection)
            if rand in listerine:
                pass
            else:
                listerine.append(rand)
        n = n + 1
        stripChr(listerine)
        writeToFile(listerine, 'key', total)
        print
        listerine = []

# METHOD TO RANDOMIZE WITH DUPLICATIONS
def randomize2(listerine, colection):
    n = 0
    while n < int(alphabet_number):
        while len(listerine) < len(characters):
            rand = random.choice(colection)
	    listerine.append(rand)
        n = n + 1
        stripChr(listerine)
        print
        listerine = []

# METHOD TO RANDOMIZE FROM MULTIPLE COLLECTIONS
def randomize3(listerine, colection1, colection2, colection3):
    n = 0
    while n < int(alphabet_number):
        while len(listerine) < len(characters):
      	    rand1 = random.choice(colection1)
	    rand2 = random.choice(colection2)
	    rand3 = random.choice(colection3)
	    rand4 = rand1 + rand2 + rand3
	    rand = random.choice(rand4)
	    listerine.append(rand)
        n = n + 1
        stripChr(listerine)
        print
        listerine = []

print
print "Alphabet :"
stripChr(characters)
print '\n'
print "Random alphabets :"
# RANDOM ALPHABETS
randomize(resultChr, characters, characters)
print
print 'Random numbers :'
# RANDOM NUMBERS
randomize2(resultNum, numbers)
print
print 'Random symbols :'
# RANDOM symbols
randomize2(resultSym, symbols)
print
print 'Random mix :'
# RANDOM MIX
randomize3(resultMix, characters, numbers, symbols)
print '\n'
print stripChr(total)
print
print 'Random total :'
randomize(resultTtl, total, total)

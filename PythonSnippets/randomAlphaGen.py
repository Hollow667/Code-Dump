# Random Alphabet Generator

import random

characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
result = []

print 'How many alphabets to generate?'
alphabet_number = raw_input('NUMBER> ')
n = 0

print
print "Alphabet :"
for char in characters:
    char.lstrip('\'')
    char.rstrip('\'')
    print char ,
print '\n'
print "Random alphabets :"

while n < int(alphabet_number):
    while len(result) < len(characters):
        rand = random.choice(characters)
        if rand in result:
            pass
        else:
            result.append(rand)
    n = n + 1

    for char in result:
        char.lstrip('\'')
        char.rstrip('\'')
        print char ,
    print

    result = []

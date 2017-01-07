import re
import random

n = 0

def randGen():

    nume = open('nume.txt', 'r')
    prenume = open('prenume.txt', 'r')

    numeafisat = nume.read()
    prenumeafisat = prenume.read()
    numeseparat = re.split('\n',numeafisat)
    prenumeseparat = re.split('\n',prenumeafisat)

    rezultat_initial = list(zip(numeseparat,prenumeseparat))
    rezultat_final = random.choice(rezultat_initial)

    print(rezultat_final[0],rezultat_final[1])

    nume.close()
    prenume.close()

numar = int(input('Numar: '))
print('===================')

while n < numar:
    randGen()
    n = n + 1


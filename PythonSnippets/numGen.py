import random

def function(x):
    for i in range(x):
        nr1 = 720000000
        nr2 = 799999999

        a = random.randint(nr1, nr2)
        b = '0' + str(a)

        print b

function(10)  # introduceti cate numere vreti (acum se genereaza 10 numere de telefon)

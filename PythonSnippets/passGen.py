
import string
import random
def id1(size=3, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for c in range(size))

def id2(size=5, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for c in range(size))

def id3(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for c in range(size))


def id4(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for c in range(size))


print """Welcome to PassCreator v1.0 by Puka
Here u can select how many caracters your password gonna have ex: 5 Char.=1xgf5
--------------------------------------------------------------------------------
1.Password with 3 characters
2.Password with 5 characters
3.Password with 8 characters
4.Password with 12 characters
"""
c = input ("Type your option(1/2/3/4): ")
password = ""
if c == 1:
        password = id1()
        print password
if c == 2:
        password = id2()
        print password
if c == 3:
        password = id3()
        print password
if c == 4:
        password = id4()
        print password

m = raw_input("Do you wish to save the password?(y/n)")
print m
if m == 'y' or m == 'Y':
        with open ("passlog.txt", "a") as file:
                file.write('Your generated password is : ' + str(password) + "\n")

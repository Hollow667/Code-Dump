from itertools import product

chars = '0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for length in range(1, 11):
    to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
        print(''.join(attempt))
        with open('brute.txt', 'a') as f:
            f.write(''.join(attempt) + '\n')

f.close()

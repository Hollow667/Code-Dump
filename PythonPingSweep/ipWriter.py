addr = '192.168.0.'
end = 255


def write(n):
    while n <= end:
        result = addr + str(n)
        n = n + 1
        print result
        with open('hosts.txt', 'a') as f:
            f.write(result + '\n')
            f.close()


write(1)

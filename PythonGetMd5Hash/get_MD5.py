import hashlib
inp = open("inp.txt" , "r")
outputhash  = open("MD5outputhashes.txt", "w")
for line in inp:            # Change this
    eachpwd = line.strip()  # Change this

    # Add this to understand the problem:
    print repr(line)

    md_5 = hashlib.md5()
    md_5.update(eachpwd)
    outputhash.write(md_5.hexdigest())
    outputhash.write("\n")

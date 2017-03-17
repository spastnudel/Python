fname = raw_input("Enter file name: ")
try:
    fh = open('mbox-short.txt')
except:
    print "File cannot be opened:", fname
    exit()
    
inp = fh.read()
count = 0
total = 0

for line in fh:
    line = line.rstrip()
    
    if line.startswith("X-DSPAM-Confidence: ") :   
        count = count + 1
        n = inp[20:]
        n = float(n)
        print n 
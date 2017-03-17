fname = raw_input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if not line.strip().startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find(':')
    num = float(line[pos+1:]) 
    total = float(total + num)
    count = float(count + 1)
print 'Average spam confidence:', float(total/count)
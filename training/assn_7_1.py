# Use words.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
	fname = 'words.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip().upper()
    print line   
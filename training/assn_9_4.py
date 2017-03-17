#open the program and turns the strings into lists
name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = text.split()
    
#creates a dictionary
counts = dict()
i = 0
for word in words:
    i= i + 1
    if word.startswith('From:'):
        counts[words[i]] = counts.get(words[i],0) + 1

#counts the name that appeared more often and how often appears, printing
bigcount = None
email = None
for mail,value in counts.items():
    if bigcount is None or value > bigcount:
        email = mail
        bigcount = value
        
print email, bigcount
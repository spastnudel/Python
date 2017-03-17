name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
text = handle.read()

counts = dict()
for line in text:
    if not line.startswith('From '):
        continue
    words = line.rstrip().lstrip().split()
    word = words[5].split(':')
    counts[word[0]] = counts.get(word[0],0) + 1

lst = list()
for kie, vaal in counts.items():
    newtup = (vaal , kie)
    lst.append(newtup)
    
lst.sort(reverse= True)
for kay, vall in lst[:]:
    print kay, vall
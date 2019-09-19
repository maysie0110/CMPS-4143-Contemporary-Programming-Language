name = input('Enter file: ')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = len(word)
    bigcount = 0
    bigword = 0
for word,count in counts.items():
    if bigcount == 0 or count > bigcount:
       bigword = word
       bigcount = count
print (bigword, bigcount)

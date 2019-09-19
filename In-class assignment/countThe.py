name = input("Enter a file: ")
handle = open(name,"r") #read file
text = handle.read()
text = text.lower()
words = text.split()
count = 0
for i in words:
    if i == 'the':
        count += 1
        

print(count)
handle.close()
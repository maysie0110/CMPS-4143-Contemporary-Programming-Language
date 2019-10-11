import re

with open("alice.txt","r") as inf, open("alice2.txt","w") as outf:
    for line in inf:
        finds = re.findall("^CHAPTER.*$",line)
        questions = re.findall(".*[^\.?]*?",line)
        outf.writelines(questions)
        for text in finds:
            outf.write(text + "\n")
        

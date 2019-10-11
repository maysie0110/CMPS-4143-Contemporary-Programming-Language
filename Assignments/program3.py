# May Trinh
# This program will replace a list of words with a different words in a poem
# It will keep the count of number of replacement for each words
# The program will then print the counter, and the new poem to an output file

import re

# dictionary of words need to be replace
wordDict = {
    'bairns':'children',
    'bairn': 'child',
    'bight': 'bay',
    'float': 'ship',
    'carles':'heroes',
    'carle': 'hero'
}

#dictionary list to keep count the number of words being replaced
countDict = {
    'bairns': 0,
    'bairn': 0,
    'bight': 0,
    'float': 0,
    'carles':0,
    'carle': 0
}

with open("pg16328.txt","r") as inf, open("Beowulf2.txt","w") as outf:
    
    #********************** HEADING *********************************
    outf.write("""May Trinh. 
    CMPS 4143 - CPL
    This program will read input file, omit the front 
    matter of the file,replace a list of words with different words and counts 
    the number of replacement for each given word. It will print to an output file 
    the number of replacement, and the new poem with replaced words. 
        
    Words List Replacement: including capitalization, punctuation,plural (except special cases) and extra ending (-er, -ed) 
    bairn -> child 
    bairns -> children 
    bight -> bay
    float -> ship
    carle -> hero
    carles -> heroes

    """)

    #******************* PPROGRAMS START HERE ************************

    line = inf.read()

    # only use the poem, starting with "BEOWULF."
    text = re.findall("^BEOWULF\.([\s\S]*)",line, re.MULTILINE)
    text = "".join(text)
    for k,v in wordDict.items():
        # count the number of replacement of each words in the replacement words
        countDict[k] += text.count(k)
        #count the capitalize words as well
        countDict[k] += text.count(k.capitalize())

        #replace the key words, with its values (and capilized version)
        text = re.sub(k,v,text)
        text = re.sub(k.capitalize(),v.capitalize(),text)
    
    # print the count before the poem
    outf.write("The number of replacement of each words are: {0} \n \n".format(str(countDict)))
    outf.write(text)





    
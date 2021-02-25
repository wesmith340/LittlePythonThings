import re

def Main():
    filename = "twitter_data.txt"
    global tagDict
    tagDict = {}
    fileInput(filename)
    
    tagDict = list(sorted(tagDict.items(), key=lambda item: item[1], reverse=True))
        
    for i in range(5):
        print(tagDict[i][1], tagDict[i][0])

def fileInput(filename):
    with open(filename,'r',encoding='utf8') as f:
        for line in f.readlines():
            for word in re.findall("#[a-zA-Z0-9_]+", line):
                countHashtag(str.lower(word))

def countHashtag(tag):
    global tagDict
    
    if tag not in tagDict:
        tagDict[tag] = 1
    else:
        tagDict[tag] = tagDict[tag] + 1

Main()
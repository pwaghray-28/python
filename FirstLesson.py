userinput = input("enter a sentence")
wordcount =  0
charactercount = 0
for i in userinput:
    charactercount = charactercount+1
    if(i == " "):
        wordcount = wordcount+1
print(charactercount)
print(wordcount)
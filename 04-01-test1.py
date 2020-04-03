# TEXT READER AND ORDERNATION ACCORDING TO WORDS AND ITS REINCIDENCE
# Cesar Henrique Peinado Moraes
print("*** DEFINITION ZONE ***\nOrganizing the text...\n")
f = open('textToBeDecoded.txt','r')
text = f.read()
f.close()

text = text.replace("\n","")
numberSymbols = len(text)
#print("Number of symbols: " + str(numberSymbols))
temp = text

for i in range(0,numberSymbols-1):
    if temp[i] == "," or temp[i] == "?" or temp[i] == "!" or temp[i] == ".":
        text = text.replace(temp[i],"")

words = text.split(" ")
words.sort()

numberWords = len(words)
listWords = []
times = []
p = 0
recurrency = 1

for i in range(1,numberWords+1):
    if i == 1:
        listWords.insert(p, words[i-1])
        times.insert(p, recurrency)
        p = p + 1
    elif words[i-1] != listWords[p-1]:
        recurrency = 1
        listWords.insert(p, words[i-1])
        times.insert(p, recurrency)
        p = p + 1
    else:
        recurrency = recurrency + 1
        times[p-1] = recurrency

orderType = input("Sort by (1) Alphabetic order or (2) Number of occurences\nUser : ")
print("Ordenance choice : " + orderType + "\n")
result = list(zip(listWords,times))
if orderType == '2':
    size = input("How many words ?\nUser : ")
    if int(size)>len(listWords):
        print("ERROR : Quantity of words invalid.")
    else:
        print("Quantity of words in the set : " + size)
        print("\n*** RESULTS ***")
        result.sort(key = lambda x: x[1], reverse=1)
        for i in range(0,int(size)):
            print ("%s : %d " %(result[i]))
elif orderType == '1':
    print("*** RESULTS ***")
    for wordNumber, occurenceTimes in result:
        print ("%s : %d " %(wordNumber, occurenceTimes))
else:
    print("ERROR : Type of ordenance invalid.")

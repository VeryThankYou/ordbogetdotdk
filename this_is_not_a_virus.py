import docx, random

document = docx.Document("AIESSAY.docx")

fullText = []
text = ""
for paragraph in document.paragraphs:
    fullText.append(paragraph.text)

stringtext = " ".join(fullText)

listOfWords = stringtext.split()
newList = []
for e in listOfWords:
    n=0
    for letter in e:
        if letter.isalpha() == 1:
            n += 1
    if n>0:
        e = ''.join(l for l in e if l.isalpha())
        newList.append(e)
        n=0


for e in newList:
    print(str(e))
#print(text)
numsyn = int(len(newList)/50)

wordchoice = random.choices(newList, k=numsyn)

for e in wordchoice:
    print(str(e))



<<<<<<< HEAD
document.save("Analyse og fortolkning.docx")
=======
document.save("AIESSAY.docx")
>>>>>>> f50649a927e89de1abeb1d7ce6a101c59e9267ba

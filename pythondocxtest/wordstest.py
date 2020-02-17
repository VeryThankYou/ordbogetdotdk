import docx

document = docx.Document("Analyse og fortolkning.docx")

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


document.save("Analyse og fortolkning.docx")
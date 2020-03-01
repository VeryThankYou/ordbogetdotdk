import docx, random
from wordAPI import api



def fuckUpDoc(file):
    document = docx.Document(str(file))
    fullText = []
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


    numsyn = int(len(newList)/50)

    wordchoice = random.choices(newList, k=numsyn)

    for e in wordchoice:
        print(str(e))

    print("\n")

    synonyms = api(wordchoice)
    for e in synonyms:
        print(str(e))

    for i in range(len(wordchoice)):
        for e in range(len(listOfWords)):
            try:
                if wordchoice[i-1] in listOfWords[e-1]:
                    listOfWords[e-1] = synonyms[i-1]
                    break
            except IndexError:
                continue
            

    newText = ' '.join(listOfWords)

    newdoc = docx.Document()
    newdoc.add_paragraph(newText)

    document.save(str(file))
    newdoc.save(str(file))

import requests


def api():
    wList = open("wordsynonym.txt")
    print(wList.readlines())
    wList.close()



#append "wordsynonym.txt" til liste og herefter hent synonymer fra wordapi
#lav synonymer til en liste.
api()

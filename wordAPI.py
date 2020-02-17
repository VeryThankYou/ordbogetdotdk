import requests

listemedord = ["hate", "love", "gluttony"]

def api(list):
 #ord der skal findes synonym for skal sidde mellem words og synynoms
 #eksempel "https://wordsapiv1.p.rapidapi.com/words/lovely/synonyms" her findes synynom til lovely
    url = "https://wordsapiv1.p.rapidapi.com/words/synonyms"


    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "7617a202a7msh9f33d595f3be64ap1c8538jsnbf77c9af8318"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)





api(listemedord)

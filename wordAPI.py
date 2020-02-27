import requests


def api(list):
 #ord der skal findes synonym for skal sidde mellem words og synynoms
 #eksempel "https://wordsapiv1.p.rapidapi.com/words/lovely/synonyms" her findes synynom til lovely
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "7617a202a7msh9f33d595f3be64ap1c8538jsnbf77c9af8318"
        }
    for i in list:
        response = requests.request("GET", "https://wordsapiv1.p.rapidapi.com/words/" + i + "/synonyms", headers=headers)

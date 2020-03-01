import requests, json

def api(liste):
 #ord der skal findes synonym for skal sidde mellem words og synynoms
 #eksempel "https://wordsapiv1.p.rapidapi.com/words/lovely/synonyms" her findes synynom til lovely
    synonyms = []
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "7617a202a7msh9f33d595f3be64ap1c8538jsnbf77c9af8318"
        }
    for i in liste:
        response = requests.request("GET", "https://wordsapiv1.p.rapidapi.com/words/" + str(i) + "/synonyms", headers=headers)
        #laver json om til en dict, så den kan bruges i python
        data = json.loads(response.text)

        try:
#da value nummer 1 er en liste af synonymer, skal vi have fat i value nummer 0
#til listen som ligger i value nummer 1 for at få det første synonym i listen
            fsynonym = list(list(data.values())[1])[0]
#da nogen ord ikke har synonymer har den ikke nogen index nummer 0
#derfor vil programmet stoppe og fortælle der er en fejl. Det ignorer vi.
        except IndexError:
            fsynonym = list(data.values())[0]

            
        synonyms.append(fsynonym)
    return synonyms

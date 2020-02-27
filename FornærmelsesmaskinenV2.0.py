import pyttsx3
import random
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.image import Image

# Loader .kv filen som styrer vores layout
Builder.load_file("kivy.kv")


class Layout(BoxLayout):

    def importList(self, file):
        # Funktionen åbner en fil
        file = open(file)
        # Funktionen læser filen
        wordList = file.read()
        # Funktionen lukker filen (husk altid at lukke filen efter du har gemt hvad du skal bruge)
        file.close()
        for e in wordList:
            # Funktionen tjekker efter alle linjeskift og erstatter dem med mellemrum
            wordList = wordList.replace("\n", " ")
        # Funktionen laver filen om til en liste
        wordList = wordList.split()
        # Funktionen returnere wordList
        return wordList

    def getRandom(self, list):
        # Funktionen henter en liste (som ligger i parameteren) og finder en tilfældig værdi i listen
        list = random.choice(list)
        # Funktionen returnere list
        return list

    def makeInsult(self, template):
        # hvis funktionen har værdien 1 bliver der lavet en liste som er gemt i "counter"
        if template == 1:
            counter = []
            # Vi henter text fra en tekstboks med id'et idEntryNoun fra en screen
            # som hedder customInsultScreen og lægger det ind i listen counter
            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryNoun.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryFM2.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryJob2.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryFM1.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryVerb.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryJob1.text)

            counter.append(TheInsultMachineApp.screenmanager.
                           get_screen("customInsultScreen").ids.idEntryAd.text)

        else:
            # Vi har variablen counterChoice som styrer hvor i listen counter vi er.
            counterChoice = 6
            # Vi har variablen whileCounter som sørger for at vores while-loop kun kører 7 gange
            whileCounter = 7
            # Counter er en liste af tekstdokumenterne.
            counter = ['things.txt', 'family.txt', 'jobs.txt', 'family.txt',
                       'acts.txt', 'jobs.txt', 'adjectives.txt']
            # Imens whileCounter ikke er 0, skal den fortsætte.
            while whileCounter != 0:
                # Vi importer en den første ting i vores liste "counter" fra importList og -
                # Vi bruger som parameter importList(counter[counterChoice]), til at få et random ord,
                # fra den tekst der lige er blevet importeret, og vi gemmer den i vores liste "counter"
                # Man skal have self med, da vi skal have fat i funktioner på skærmen.
                counter[counterChoice] = self.getRandom(
                    self.importList(counter[counterChoice]))
                # Vi bruger "counterChoice" til at styrer hvor i listen vi er f.eks. counter[0], counter[1], ...
                counterChoice -= 1
                whileCounter -= 1
        # Vi indsætter enten de random genererede ord eller brugerens generede ord,
        # hvilket bliver bestemt af template.
        # Derefter bliver det sat i skabelonen via. .format og bruger counter[] i de 7 tuborgklammer
        # og gemmmer det som variablen text
        text = "I don’t want to talk to you no more you {} {}!... I {} in your general direction! Your {} was a {} and your {} smelt of {}!\n".format(
            counter[6], counter[5], counter[4], counter[3], counter[2], counter[1], counter[0])
        # Vi bruger text som parameter i sayInsult
        self.printInsult(text)

    def printInsult(self, text):
        # Vi laver teksten om på et object, der har id'et idPrint til vores gemte variable text
        self.ids.idPrint.text = text

    def sayInsult(self, text):
        # Gemmer "start" på pyttsx3 til engine. Altså hver gang vi bruger engine, starter den pyttsx3
        engine = pyttsx3.init()
        # Computeren læser text højt
        engine.say(text)
        # Man kan ikke stoppe programmet før den er færdig med at læse
        engine.runAndWait()


class TheInsultMachineApp(App):
    # Vi bruger screenmanager til at tilføje 2 skærme.
    #screenmanager = ScreenManager()
    # screenmanager.add_widget(frenchGuardScreen(name="frenchGuardScreen"))
    # screenmanager.add_widget(customInsultScreen(name="customInsultScreen"))

    def build(self):

        layout = Layout()

        # Gør så farven på vinduet er hvidt
        Window.clearcolor = (1, 1, 1, 1)
        return layout


# Starter programmet
if __name__ in ('__main__'):
    TheInsultMachineApp().run()

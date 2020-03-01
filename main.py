import random
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from this_is_not_a_virus import fuckUpDoc


import os

# Loader .kv filen som styrer vores layout
Builder.load_file("kivy.kv")


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    fileText = ObjectProperty(None)

    # Gør så man kan vælge en fil i ens stifinder.

    def dismiss_popup(self):
        self.popupWindow.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self.popupWindow = Popup(title="Load file", content=content,
                                 size_hint=(0.9, 0.9))
        self.popupWindow.open()

    # ------------------------------------------

    # Konvertering af den valgte fil

    def load(self, path, filename):
        # Sørger for at undgå at programmet crasher, hvis der ikke er valgt en fil.
        if(filename == []):
            pass
        else:
            # Gemmer vi path og filnavnet til et label med id'et path.
            self.ids.path.text = os.path.join(path, filename[0])

    def convert(self):
        # Sørger for at undgå at programmet crasher, hvis der ikke er valgt en fil.
        if(self.ids.path.text == ""):
            pass
        else:
            fuckUpDoc(self.ids.path.text)

    # ------------------------------------------


class RandomWordApp(App):
    def build(self):
        root = Root()
        # Gør så farven på vinduet er anderledes
        Window.clearcolor = (239, 236, 221, 1)
        return root


# Starter programmet
if __name__ in ('__main__'):
    RandomWordApp().run()

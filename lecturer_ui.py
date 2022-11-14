from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import os
import json
import time
from playsound import playsound
from converter import convert_to_speech
from credentials import *
from delete_file import *


Builder.load_file("menu.kv")
        

class MyLayout(Screen):
    def selected(self, filename):
        try:   # type of files to select 
            delete_files()
            for entry in filename:
                self.ids.file_label2.text = "converted {} to speech".format(os.path.split(entry)[1])
            for entry in filename:
                f = open("{}".format(entry), "r")
                text = ('''{}'''.format(f.read()))
                file = open("text_files/{}".format(os.path.split(entry)[1]), 'w')
                file.write(text)
                file.close() 
            content = {}
            entries = os.listdir('text_files/')
            for entry in entries:
                f = open("text_files/{}".format(entry), "r")
                text = ('''{}'''.format(f.read()))
                content[entry] = text
            create_apikey()
            for i in range (len(list(content))):
                filename = list(content)[i]
                text = list(content.values())[i]
                #print(text)
                convert_to_speech(text,filename)
            
                
            os.remove("ai-learning-text-to-speech-93061333450a.json")
            
            #os.remove("text_files/{}".format(filename))   
        except:
            pass
class PlayAudio(Screen):

    def play_sound(self,filename):
        for entry in filename:
            self.ids.file_label3.text = "spoke {}".format(os.path.split(entry)[1]) 
            playsound(entry)

class Settings(Screen):
    def __init__(self, **kwargs): 
        super(Settings, self).__init__(**kwargs)
        with open('settings.json', 'r') as f:
                data = json.load(f)
                self.ids.voice.text = data['name']
                self.ids.speed.text = str(data['speaking_rate']) 

    def settings(self):
        voice = self.ids.voice.text
        speed = self.ids.speed.text

        with open('settings.json', 'r') as f:
            data = json.load(f)
            data['name'] = voice
            data['speaking_rate'] = float(speed)

        os.remove('settings.json')
        with open('settings.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(data)



class VoicyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyLayout(name='upload'))
        sm.add_widget(PlayAudio(name='audio'))
        sm.add_widget(Settings(name='settings'))
        return sm


if __name__ == "__main__":
    VoicyApp().run()
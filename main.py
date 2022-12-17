from kivy.app import App
#kivy.require("2.1.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

import re
from functools import reduce
from kivy.core.audio import SoundLoader

from pyobjus import autoclass

# Setting size to resizable
Config.set('graphics', 'resizable', 1)


PREC_E = 0.000000001
ROUND_DIGITS = 9
bSound = 0            
        

# Creating Layout class
class calc():    
    def __init__(self, screenmanager):
           
        self.sm = screenmanager
        
        #self.allClear(False)
        self.memorized = '0'
  
    
    def allClear(self, bSound):
        self.sm.get_screen("main").ids.entry.text = '' 
        self.sm.get_screen("main").ids.buffer.text = '0'

        
    # Function called when equals is pressed
    def calculate(self):
        display_text = self.sm.get_screen("main").ids.entry.text

        alu_result = eval(display_text)    
        self.sm.get_screen("main").ids.entry.text = str(alu_result)
        self.sm.get_screen("main").ids.buffer.text = display_text


        
                
    def composeBuff(self, text):  #左括号，右括号的输入条件：左括号前必须为加减乘除，右括号之前必须有左括号
        display_text = self.sm.get_screen("main").ids.entry.text
        self.sm.get_screen("main").ids.entry.text = display_text + text            
        
               
    def inscMemory(self):  #记忆键M+ 内存与最后的操作数相加
        pass


    def descMemory(self):  #记忆键M- 
        pass
        
            
    def back(self):  
        pass
            
        
    def Nonop(self, text):
        pass
        
    def clearMemory(self):  #记忆键M- 
        pass

        
class MainScreen(Screen): 
    pass    

class Settings(Screen):
    pass
    
class Another(Screen):
    pass



#presentation = 
Builder.load_file("./multi.kv")

class MainApp(App):
    def on_start(self):
        self.banner_ad = autoclass('adSwitch').alloc().init()
    
    def show_banner(self):
        self.banner_ad.show_ads()
    
    def hide_banner(self):
        self.banner_ad.hide_ads()
    
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name = "main"))
        self.sm.add_widget(Another(name = "other"))
        self.sm.add_widget(Settings(name = "setting"))
        self.calc = calc(self.sm)
        return self.sm


if __name__ == "__main__":
    MainApp().run()

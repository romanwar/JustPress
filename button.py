from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from time import strftime
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from time import gmtime, strftime
from kivy.properties import DictProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
import os.path
import datetime
import random
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
import string





class ScreenManagement(ScreenManager):
    sm = ScreenManager()


class MenuScreen(Screen):
    pass

class SubmenuScreen(Screen):
    pass

class FreemodeGameScreen(Screen):
    pass

class OnpressGameScreen(Screen):
    pass

class OntimeGameScreen(Screen):
    pass

class StatiscticScreen(Screen):
    pass

class CollectionScreen(Screen):
    pass

class ButtonApp(App):
    
    #store = JsonStore('C:/Users/ROman/Documents/kivy_app/score_base.json')

    JsonFileName = 'store_current.json'
    store_current = JsonStore(JsonFileName)

    sw_started = False
    main_list = {}

    def pressrandom(b):
        b = random.randrange(100, 200, 1)
        return b

    #def random_time(sw_seconds):
        #sw_seconds = pressrandom()
        #return sw_seconds

    
    

    def on_start(self):
        Clock.schedule_interval(self.update, 0)
        


    def back(self):
        date_current = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.root.current = 'MenuScreen'
        self.main_list.update({date_current : i for i in self.pressgame()}) 
        #print(self.main_list)
        #self.store_current['Score'] = self.store['Score']
        self.store_current[date_current] = {date_current : i for i in self.pressgame()}

        

    def submenu(self):
        self.root.current = 'SubmenuScreen'
    
    def fremodegame(self):
        self.root.current = 'FreemodeGameScreen'
        self.count = 0
        
        self.root.get_screen('FreemodeGameScreen').ids.counttime.text = str(0)

    def ontimeplay(self):
        self.sw_seconds = self.pressrandom() * 0.19
        self.root.current = 'OntimeGameScreen'
        self.count = 0
        self.c = self.pressrandom()
        self.root.get_screen('OntimeGameScreen').ids.counttime.text = str(self.c)

    def onpressplay(self):
        self.root.current = 'OnpressGameScreen'
        self.count = 0
        self.root.get_screen('FreemodeGameScreen').ids.counttime.text = str('0')
        self.root.get_screen('OnpressGameScreen').ids.counttime.text = 'EEEEE!!'
        self.c = self.pressrandom()
        #return c   
        #print(self.c)
        self.root.get_screen('OnpressGameScreen').ids.counttime.text = str(self.c)
        
    


    def statistic(self):
        self.root.current = 'StatiscticScreen'
        dict_score = {}
        for i in self.store_current.keys():
            #i = {i}
            dict_score.update(self.store_current.get(i))
            
        
        print(sorted(dict_score.items(), key=lambda x: x[1], reverse=True))
        dict_score_sorted = sorted(dict_score.items(), key=lambda x: x[1], reverse=True)
        list_stat = []
        for i in dict_score_sorted:
            list_stat.append(str.replace(str.replace(str(i), ')', ''), '(', ''))
            #print(str.replace(str.replace(str(i), ')', ''), '(', ''))
        #print(list_stat)
        list_stat_final = str.replace(str.replace(str('\n'.join(list_stat[:10])), '\'', ''), ',', ' : ')   
        print(list_stat_final)
        self.root.get_screen('StatiscticScreen').ids.ScrollView.text = list_stat_final
        #self.root.get_screen('StatiscticScreen').ids.Label1.text = str(list_stat[0])
        #self.root.get_screen('StatiscticScreen').ids.Label2.text = str(list_stat[1])
        #self.root.get_screen('StatiscticScreen').ids.Label3.text = str(list_stat[2])  
        #self.root.get_screen('StatiscticScreen').ids.Label4.text = str(list_stat[3])  
        #self.root.get_screen('StatiscticScreen').ids.Label5.text = str(list_stat[4])  
        #self.root.get_screen('StatiscticScreen').ids.Label6.text = str(list_stat[5])  
        #self.root.get_screen('StatiscticScreen').ids.Label7.text = str(list_stat[6])    


    def collection(self):
        self.root.current = 'CollectionScreen'
        dict_score_collect = {}
        for i in self.store_current.keys():
            #i = {i}
            dict_score_collect.update(self.store_current.get(i))
        max_dict_score_collect = max(dict_score_collect.values())
        print(max_dict_score_collect)
        
        if max_dict_score_collect > 30:
            self.root.get_screen('CollectionScreen').ids.Label_collect_1.text = '> 30'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_1.text = ''

        if max_dict_score_collect > 50:
            self.root.get_screen('CollectionScreen').ids.Label_collect_2.text = '> 50'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_2.text = ''

        if max_dict_score_collect > 70:
            self.root.get_screen('CollectionScreen').ids.Label_collect_3.text = '> 70'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_3.text = ''
        
        if max_dict_score_collect > 90:
            self.root.get_screen('CollectionScreen').ids.Label_collect_4.text = '> 90'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_4.text = ''

        if max_dict_score_collect > 110:
            self.root.get_screen('CollectionScreen').ids.Label_collect_5.text = '> 110'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_5.text = ''
            
        if max_dict_score_collect > 130:
            self.root.get_screen('CollectionScreen').ids.Label_collect_6.text = '> 130'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_6.text = ''

        if max_dict_score_collect > 150:
            self.root.get_screen('CollectionScreen').ids.Label_collect_7.text = '> 150'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_7.text = ''

        if max_dict_score_collect > 170:
            self.root.get_screen('CollectionScreen').ids.Label_collect_8.text = '> 170'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_8.text = ''
            
        if max_dict_score_collect > 190:
            self.root.get_screen('CollectionScreen').ids.Label_collect_9.text = '> 190'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_9.text = ''

        if max_dict_score_collect > 210:
            self.root.get_screen('CollectionScreen').ids.Label_collect_10.text = '> 210'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_10.text = ''

        if max_dict_score_collect > 230:
            self.root.get_screen('CollectionScreen').ids.Label_collect_11.text = '> 230'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_11.text = ''
            
        if max_dict_score_collect > 260:
            self.root.get_screen('CollectionScreen').ids.Label_collect_12.text = '> 260'
        else:
            self.root.get_screen('CollectionScreen').ids.Label_collect_12.text = ''


    label_text = StringProperty()

    def __init__(self,**kwargs):
        super(ButtonApp,self).__init__(**kwargs)
        self.count = 0
        self.c = self.pressrandom()
        self.sw_seconds = self.pressrandom() * 0.19
 
    def increment(self,*args):
        self.count += 1
        return self.count
    


    def pressgame(self):
        list_value = []
        a = self.increment()
        b = self.c
        #print(b)
        if a == b:
            self.root.get_screen('OnpressGameScreen').ids.counttime.text = 'EEEEE!!'
            #time.sleep(1)
            self.root.current = 'MenuScreen'
        else:
            self.root.get_screen('OnpressGameScreen').ids.counttime.text = str(a) + ' / ' + str(b)    
        list_value.append(a)
        #print(list_value)
        return list_value
    

    def pressfreegame(self):
        list_value = []
        a = self.increment()
        self.root.get_screen('FreemodeGameScreen').ids.counttime.text = str(a)
        list_value.append(a)
        #print(list_value)
        return list_value

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds -= nap
        m, s = divmod(self.sw_seconds, 60)
        self.root.get_screen('OntimeGameScreen').ids.ontime.text = ('%02d:%02d.[size=40]%02d[/size]' % (int(m), int(s), int(s * 100 % 100)))


    def presstimegame(self):
        list_value = []
        a = self.increment()
        b = self.c
        c = self.sw_seconds
        
        #print(c)
        if c < 0 and a < b:
            self.root.get_screen('OntimeGameScreen').ids.counttime.text = 'Time is OVER!!'
            #time.sleep(2)
            self.root.current = 'MenuScreen'
        elif a == b:
            self.root.get_screen('OntimeGameScreen').ids.counttime.text = 'EEEEE!!'
            #time.sleep(1)
            self.root.current = 'MenuScreen'
        else:
            self.root.get_screen('OntimeGameScreen').ids.counttime.text = str(a) + ' / ' + str(b)
        list_value.append(a)
        #print(list_value)
        return list_value

    def start_stop(self):
        self.sw_started = not self.sw_started

        
    def build(self):
       self.root = Builder.load_file('C:/Users/ROman/Documents/kivy_app/button.kv')
   
    

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#ffffcc')
   
    LabelBase.register(name='Roboto',
                       fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')
    Window.size = (550, 650)
    ButtonApp().run()
    

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import FactoryException


pdata = ""
App.title = "Tic Tac Fun "

standx = ["x", "x", "x"]
stando = ["o", "o", "o"]
# 123
lista = []
# 456
listb = []
# 789
listc = []
# 147
listd = []
# 258
liste = []
# 369
listf = []
# 159
listg = []
# 357
listh = []


Builder.load_file("mainlayout.kv")


class MainLayout(BoxLayout):
    player1=True
    player2=False
    bsound = SoundLoader.load("sound/fireEffect.ogg")
    def __init__(self,**kwargs):
        super(MainLayout,self).__init__(**kwargs)

        Window.bind(on_joy_axis=self.on_joy_axis)
        Window.bind(on_joy_button_down=self.on_joy_button_down)

        self.ids.lb.text = "[color=0000ff]Player1[/color]"
        self.ids.resetgame.bind(on_press=self.reset)

        self.ids.click1.bind(on_press=self.on_press1)
        self.ids.click2.bind(on_press=self.on_press2)
        self.ids.click3.bind(on_press=self.on_press3)
        self.ids.click4.bind(on_press=self.on_press4)
        self.ids.click5.bind(on_press=self.on_press5)
        self.ids.click6.bind(on_press=self.on_press6)
        self.ids.click7.bind(on_press=self.on_press7)
        self.ids.click8.bind(on_press=self.on_press8)
        self.ids.click9.bind(on_press=self.on_press9)

    def on_press1(self,obj):

        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text="[color=ff0000]Player2[/color]"
            self.ids.click1.text = "[color=0000ff]X[/color]"
            self.ids.click1.disabled = True
            lista.append("x")
            listd.append("x")
            listg.append("x")

        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click1.text = "[color=ff0000]O[/color]"
            self.ids.click1.disabled = True
            lista.append("o")
            listd.append("o")
            listg.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press2(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click2.text = "[color=0000ff]X[/color]"
            self.ids.click2.disabled = True
            lista.append("x")
            liste.append("x")

        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click2.text = "[color=ff0000]O[/color]"
            self.ids.click2.disabled = True
            lista.append("o")
            liste.append("o")

        Clock.schedule_once(self.winner, 0.1)

    def on_press3(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click3.text = "[color=0000ff]X[/color]"
            self.ids.click3.disabled = True
            lista.append("x")
            listf.append("x")
            listh.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click3.text = "[color=ff0000]O[/color]"
            self.ids.click3.disabled = True
            lista.append("o")
            listf.append("o")
            listh.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press4(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click4.text = "[color=0000ff]X[/color]"
            self.ids.click4.disabled = True
            listb.append("x")
            listd.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click4.text = "[color=ff0000]O[/color]"
            self.ids.click4.disabled = True
            listb.append("o")
            listd.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press5(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click5.text = "[color=0000ff]X[/color]"
            self.ids.click5.disabled = True
            listb.append("x")
            liste.append("x")
            listg.append("x")
            listh.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click5.text = "[color=ff0000]O[/color]"
            self.ids.click5.disabled = True
            listb.append("o")
            liste.append("o")
            listg.append("o")
            listh.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press6(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click6.text = "[color=0000ff]X[/color]"
            self.ids.click6.disabled = True
            listb.append("x")
            listf.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click6.text = "[color=ff0000]O[/color]"
            self.ids.click6.disabled = True
            listb.append("o")
            listf.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press7(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click7.text = "[color=0000ff]X[/color]"
            self.ids.click7.disabled = True
            listc.append("x")
            listd.append("x")
            listh.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click7.text = "[color=ff0000]O[/color]"
            self.ids.click7.disabled = True
            listc.append("o")
            listd.append("o")
            listh.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press8(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click8.text = "[color=0000ff]X[/color]"
            self.ids.click8.disabled = True
            listc.append("x")
            liste.append("x")

        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click8.text = "[color=ff0000]O[/color]"
            self.ids.click8.disabled = True
            listc.append("o")
            liste.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def on_press9(self,obj):
        self.bsound.play()
        if self.player1 == True:
            self.player1 = False
            self.player2 = True
            self.ids.lb.text = "[color=ff0000]Player2[/color]"
            self.ids.click9.text = "[color=0000ff]X[/color]"
            self.ids.click9.disabled = True
            listc.append("x")
            listf.append("x")
            listg.append("x")
        else:
            self.player2 = False
            self.player1 = True
            self.ids.lb.text = "[color=0000ff]Player1[/color]"
            self.ids.click9.text = "[color=ff0000]O[/color]"
            self.ids.click9.disabled = True
            listc.append("o")
            listf.append("o")
            listg.append("o")
        Clock.schedule_once(self.winner, 0.1)

    def reset(self,obj):
        lista.clear(), listb.clear(), listc.clear(), listd.clear(), liste.clear(), listf.clear(), listg.clear(), listh.clear()
        pdata = ""
        self.ids.lb.text = "[color=0000ff]Player1[/color]"

        self.player1 = True
        self.player2 = False
        self.ids.click1.text = ""
        self.ids.click2.text = ""
        self.ids.click3.text = ""
        self.ids.click4.text = ""
        self.ids.click5.text = ""
        self.ids.click6.text = ""
        self.ids.click7.text = ""
        self.ids.click8.text = ""
        self.ids.click9.text = ""
        #enable

        self.ids.click1.disabled = False
        self.ids.click2.disabled = False
        self.ids.click3.disabled = False
        self.ids.click4.disabled = False
        self.ids.click5.disabled = False
        self.ids.click6.disabled = False
        self.ids.click7.disabled = False
        self.ids.click8.disabled = False
        self.ids.click9.disabled = False

        #set Background
        self.ids.click1.background_color = [0, 0, .8, .5]
        self.ids.click2.background_color = [0, 0, .8, .5]
        self.ids.click3.background_color = [0, 0, .8, .5]
        self.ids.click4.background_color = [0, 0, .8, .5]
        self.ids.click5.background_color = [0, 0, .8, .5]
        self.ids.click6.background_color = [0, 0, .8, .5]
        self.ids.click7.background_color = [0, 0, .8, .5]
        self.ids.click8.background_color = [0, 0, .8, .5]
        self.ids.click9.background_color = [0, 0, .8, .5]



    def on_joy_axis(self, win, stickid, axisid, value):
        print(stickid, axisid, value)

    def on_joy_button_down(self, win, stickid, buttonid):
        # player1
        if buttonid == 0 and self.player1 == True and self.ids.click1.disabled == False:
            self.on_press1(win)
        elif buttonid == 1 and self.player1 == True and self.ids.click2.disabled == False:

            self.on_press2(win)

        elif buttonid == 2 and self.player1 == True and self.ids.click3.disabled == False:

            self.on_press3(win)
        elif buttonid == 3 and self.player1 == True and self.ids.click4.disabled == False:
            self.on_press4(win)
        elif buttonid == 4 and self.player1 == True and self.ids.click5.disabled == False:
            self.on_press5(win)
        elif buttonid == 5 and self.player1 == True and self.ids.click6.disabled == False:

            self.on_press6(win)
        elif buttonid == 6 and self.player1 == True and self.ids.click7.disabled == False:

            self.on_press7(win)
        elif buttonid == 7 and self.player1 == True and self.ids.click8.disabled == False:

            self.on_press8(win)
        elif buttonid == 8 and self.player1 == True and self.ids.click9.disabled == False:

            self.on_press9(win)
        elif buttonid == 9 :
            # self.on_press9(win)
            self.reset(win)
            justdismiss = False



        # player2
        elif buttonid == 10 and self.player2 == True and self.ids.click1.disabled == False:

            self.on_press1(win)

        elif buttonid == 11 and self.player2 == True and self.ids.click2.disabled == False:

            self.on_press2(win)
        elif buttonid == 12 and self.player2 == True and self.ids.click3.disabled== False:

            self.on_press3(win)
        elif buttonid == 13 and self.player2 == True and self.ids.click4.disabled == False:

            self.on_press4(win)
        elif buttonid == 14 and self.player2 == True and self.ids.click5.disabled == False:

            self.on_press5(win)
        elif buttonid == 15 and self.player2 == True and self.ids.click6.disabled == False:

            self.on_press6(win)
        elif buttonid == 16 and self.player2 == True and self.ids.click7.disabled == False:

            self.on_press7(win)
        elif buttonid == 17 and self.player2 == True and self.ids.click8.disabled == False:

            self.on_press8(win)
        elif buttonid == 18 and self.player2 == True and self.ids.click9.disabled == False:

            self.on_press9(win)
        elif buttonid == 19 :
            self.reset(win)
        print(buttonid)

    def winner(self,obj):
        pdata = ""
        title = ""

        sound = SoundLoader.load("sound/Sax.ogg")
        box = BoxLayout(orientation="vertical")
        box.add_widget(Image(source='images/gamepad3.png', allow_stretch=False, keep_ratio=False, ))
        if lista == standx or listb == standx or listc == standx or listd == standx or liste == standx or listf == standx or listg == standx or listh == standx:
            pdata = "[color=00ff00]Game over[/color]: [color=0000ff] player 1 win[/color]"
            title = "Congratulations player1"
            lb1 = Label(text=pdata, markup=True, font_size=25)
            lb1.font_name = "fonts/DroidSans-Bold.ttf"
            lb1.bold = True
            butt1 = Button(text="Play Again")
            box.add_widget(lb1)
            box.add_widget(butt1)
            content2 = box
            popup = Popup(title=title,
                          content=content2,
                          size_hint=(None, None), size=(400, 400))

            popup.background = "images/au.jpg"
            popup.title_size = 30

            popup.title_color = [1, 1, 0, 1]
            popup.title_font = "fonts/actionis.ttf"
            butt1.background_color = [1, 1, 0, 1]
            butt1.bind(on_release=self.reset)
            butt1.bind(on_release=popup.dismiss)

            popup.open()
            anim = Animation(x=50) + Animation(size=(300, 300), duration=2.)
            anim.start(popup)

            sound.play()
            Clock.unschedule(self.winner, .1)
            lista.clear(), listb.clear(), listc.clear(), listd.clear(), liste.clear(), listf.clear(), listg.clear(), listh.clear()



        elif lista == stando or listb == stando or listc == stando or listd == stando or liste == stando or listf == stando or listg == stando or listh == stando:
            pdata = "[color=00ff00]Game over[/color]:[color=ff0000] player 2 win[/color]"
            title = "Congratulations player2"
            lb1 = Label(text=pdata, markup=True, font_size=25)
            lb1.font_name = "fonts/DroidSans-Bold.ttf"
            lb1.bold = True
            butt1 = Button(text="Play Again")
            box.add_widget(lb1)
            box.add_widget(butt1)
            content2 = box
            popup = Popup(title=title,
                          content=content2,
                          size_hint=(None, None), size=(400, 400))

            popup.background = "images/au.jpg"
            popup.title_size = 30

            popup.title_color = [1, 1, 0, 1]
            popup.title_font = "fonts/actionis.ttf"
            butt1.background_color = [1, 1, 0, 1]

            butt1.bind(on_release=self.reset)
            butt1.bind(on_release=popup.dismiss)

            popup.open()
            anim = Animation(x=50) + Animation(size=(300, 300), duration=2.)
            anim.start(popup)

            sound.play()
            lista.clear(), listb.clear(), listc.clear(), listd.clear(), liste.clear(), listf.clear(), listg.clear(), listh.clear()




        elif self.ids.click1.disabled == True and self.ids.click2.disabled == True and self.ids.click3.disabled == True and self.ids.click4.disabled == True and self.ids.click5.disabled == True and self.ids.click6.disabled == True and self.ids.click7.disabled == True and self.ids.click8.disabled == True and self.ids.click9.disabled == True:

            pdata = "[color=00ff00]Game over[/color]: [color=f0ff00] Drwa [/color]"
            title = "No Winner"
            lb1 = Label(text=pdata, markup=True, font_size=25)
            lb1.font_name = "fonts/DroidSans-Bold.ttf"
            lb1.bold = True
            butt1 = Button(text="Play Again")
            box.add_widget(lb1)
            box.add_widget(butt1)
            content2 = box
            popup = Popup(title=title,
                          content=content2,
                          size_hint=(None, None), size=(400, 400))

            popup.background = "images/au.jpg"
            popup.title_size = 30

            popup.title_color = [1, 1, 0, 1]
            popup.title_font = "fonts/actionis.ttf"
            butt1.background_color = [1, 1, 0, 1]

            butt1.bind(on_release=self.reset)
            butt1.bind(on_release=popup.dismiss)

            popup.open()
            anim = Animation(x=50) + Animation(size=(300, 300), duration=2.)
            anim.start(popup)

            sound.play()
            lista.clear(), listb.clear(), listc.clear(), listd.clear(), liste.clear(), listf.clear(), listg.clear(), listh.clear()

        #print(pdata)
        #print(lista,listb,listc,listd,liste,listf,listg,listh)

    def keyspop(self):
        box = BoxLayout(orientation="vertical")
        # box.add_widget(Image(source='images/appic.png', allow_stretch=False, keep_ratio=False, ))
        keysdata = "[color=f000ff]F11[/color]: \n" \
                   "[color=00ff00]Rotate the Window through 0, 90, 180 and 270 degrees[/color]\n\n" \
                   "[color=f000ff]Shift + F11[/color]: \n" \
                   "[color=00ff00]Switches between portrait and landscape on desktops[/color]\n\n" \
                   "[color=f000ff]F12[/color]: \n[color=00ff00]Take a screenshot[/color]\n\n"
        lb1 = Label(text=keysdata, markup=True)
        lb1.font_name = "fonts/DroidSans-Bold.ttf"
        lb1.bold = True
        box.add_widget(lb1)
        content2 = box
        self.popup = Popup(title="Special Keys",
                           content=content2,
                           size_hint=(None, None), size=(500, 300))

        self.popup.background = "images/im2.png"
        self.popup.title_size = 30

        self.popup.title_color = [1, 1, 0, 1]
        self.popup.title_font = "fonts/actionis.ttf"
        self.popup.open()


    def author(self):
        box = BoxLayout(orientation="vertical")
        box.add_widget(Image(source='images/author.jpg', allow_stretch=False, keep_ratio=False, ))
        data = "Author :[color=ffff00]Ahmed Mohmed[/color]\nVersion :[color=ffff00]1.0[/color]"
        lb2 = Label(text=data, markup=True, font_size=30)
        lb2.font_name = "fonts/DancingScript-Bold.ttf"
        box.add_widget(lb2)
        content3 = box
        title = "About Tic Tac Toc"

        popup = Popup(title="About Tic Tac Toc",
                      content=content3,
                      size_hint=(None, None), size=(400, 400))
        # popup.background_color=[0,1,1,1]
        popup.background = "images/au.jpg"
        popup.title_size = 30
        popup.title_color = [1, 1, 0, 1]
        popup.title_font = "fonts/actionis.ttf"
        popup.open()


    def control(self):
        box = BoxLayout(orientation="vertical")
        box.add_widget(Image(source='images/gamepad.jpg', allow_stretch=False, keep_ratio=False, ))
        content3 = box

        popup = Popup(title="Controlling",
                      content=content3,
                      size_hint=(None, None), size=(500, 500))
        # popup.background_color=[0,1,1,1]
        popup.background = "images/au.jpg"
        popup.title_size = 30
        popup.title_color = [1, 1, 0, 1]
        popup.title_font = "fonts/actionis.ttf"
        popup.open()

class MyAppGame(App):
    def resetactionbarbutton(self):
        ob=MainLayout()
        ob.reset()

    def build(self):
        root = FloatLayout()
        root.add_widget(Image(source='images/bk2.jpg', allow_stretch=True, keep_ratio=False))
        root.add_widget(MainLayout())
        return root

if __name__ == '__main__':
    MyAppGame().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class ButtonScr(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction 
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name=name)
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        label = Label(text = "Инструкция к тесту")
        box.add_widget(label)
        btn = ButtonScr(screen = self, direction = 'right', goal = 'first',text="Начать тест твоего сердечка")
        box.add_widget(btn)
        self.add_widget(box)


class FirstScr(Screen):
    def __init__(self, name='first'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, direction = 'right', goal = 'two',text="Отдохни несколько минут и измерь свой пульс в течение 15 сек.")
        ti = TextInput(text = 'Hello', halign = 'left',focus=True, multiline=False)
        box.add_widget(btn)
        box.add_widget(ti)
        self.add_widget(box)

class TwoScr(Screen):
    def __init__(self, name='two'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, direction = 'right', goal = 'thri',text="Сделай 30 приседаний за 45 сек.")
        box.add_widget(btn)
        self.add_widget(box)


class ThriScr(Screen):
    def __init__(self, name='thri'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, direction = 'right', goal = 'frour',text="Начать тест твоего сердечка")
        box.add_widget(btn)
        self.add_widget(box)


class FrourScr(Screen):
    def __init__(self, name='frour'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, direction = 'right', goal = 'Five',text="Начать тест твоего сердечка")
        box.add_widget(btn)
        self.add_widget(box)

class FiveScr(Screen):
    def __init__(self, name='Five'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen


class MyApp(App):
   def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(TwoScr())
        sm.add_widget(ThriScr())
        sm.add_widget(FrourScr())
        sm.add_widget(FiveScr())
        return sm


app = MyApp()
app.run()
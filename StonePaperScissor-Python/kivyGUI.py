from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from TerminalMode import main

class MainGUI(BoxLayout):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.orientation = 'vertical'

        self.mainLabel = Label(font_size='140sp',text="START")
        self.add_widget(self.mainLabel)

        SecondRow = BoxLayout()
        self.HumanLabel = Label(font_size='70sp',text="YOU")
        SecondRow.add_widget(self.HumanLabel)
        SecondRow.add_widget(Label(font_size='100sp',text="  VS  "))
        self.CompLabel = Label(font_size='70sp',text="CPU")
        SecondRow.add_widget(self.CompLabel)
        self.add_widget(SecondRow)

        ThirdRow = BoxLayout()
        StoneButton = Button(text="STONE")
        ThirdRow.add_widget(StoneButton)
        PaperButton = Button(text="PAPER")
        ThirdRow.add_widget(PaperButton)
        CompButton = Button(text="SCISSOR")
        ThirdRow.add_widget(CompButton)
        self.add_widget(ThirdRow)

        StoneButton.bind(on_press=lambda x:self.guimain("STONE"))
        PaperButton.bind(on_press=lambda x:self.guimain("PAPER"))
        CompButton.bind(on_press=lambda x:self.guimain("SCISSOR"))

    def guimain(self,H_C):
        C_C,Result = main(H_C)
        self.HumanLabel.text = H_C
        self.CompLabel.text = C_C
        self.mainLabel.text=Result

class MainWin(App):
    def build(self):
        re = MainGUI()
        return re

MainWin().run()

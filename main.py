from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class App(MDApp):
    def build(self):
        return MDLabel(text="Пошел нахуй", halign="center")



App().run()
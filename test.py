#!/usr/bin/python3

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

class App(MDApp):

    def build(self):
        screen = Screen()

        file = open('test.txt','r')
        str = file.read()

        label = MDLabel(text=str,halign='center')
        screen.add_widget(label)

        return screen

if __name__ == '__main__':
    App().run()
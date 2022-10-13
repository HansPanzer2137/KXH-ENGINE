from asyncore import read
import sys
import os
import configparser
from tkinter import * 
from tkinter.ttk import *

root = Tk()

def create_config():
    if (os.path.exists('config.ini') == False):
        open('config.ini', 'a').close()
        config = configparser.ConfigParser()
        config['CONFIG-EDITOR'] = {
            'GUI-height': '287',
            'GUI-width': '917',
            'GUI-drone': 'class-K',

            'ENGINE-HEIGHT': str(root.winfo_screenheight()),
            'ENGINE-WIDTH': str(root.winfo_screenwidth())
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


import sys
import os
import configparser

def create_config():
    if (os.path.exists('config.ini') == False):
        open('config.ini', 'a').close()
        config = configparser.ConfigParser()
        config['CONFIG-EDITOR'] = {
            'GUI-height': '287',
            'GUI-width': '917',
            'GUI-drone': 'class-K'
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

def engine_config():
    if(os.path.exists('config.ini') == False):
        open('config.ini', 'a').close()
        config = configparser.ConfigParser()
        config['CONFIG-ENGINE'] ={
            'ENGINE-HEIGHT': 
            ''
        }

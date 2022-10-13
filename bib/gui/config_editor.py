import sys
import os
import configparser

def create_config():
    if (os.path.exists('config.ini') == False):
        open('config.ini', 'a').close()
        config = configparser.ConfigParser()
        config['CONFIG-EDITOR'] = {
            'GUI-height': '600',
            'GUI-width': '800',
            'GUI-drone': 'class-K'
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

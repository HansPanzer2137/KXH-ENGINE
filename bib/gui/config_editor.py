import sys
import os
import configparser

def create_config():
    if (os.path.exists('config.txt') == False):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'GUI-height': '600',
            'GUI-width': '800',
            'GUI-drone': 'class-K'
        }
        with open('config.txt', 'w') as configfile:
            config.write(configfile)

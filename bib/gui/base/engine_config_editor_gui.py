from pickletools import read_bytes8
import pygame
import os
import sys
import configparser

config = configparser.ConfigParser()
config.sections()

config.read('../config.txt')

class config_gui():
    read_width = config['CONFIG-EDITOR']['GUI-width']
    read_height = config['CONFIG-EDITOR']['GUI-height']

(width, height) = (config_gui.read_width, config_gui.read_height)

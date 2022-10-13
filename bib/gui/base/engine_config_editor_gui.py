from distutils.command.config import config
from pickletools import read_bytes8
import pygame
import os
import sys
import configparser

class config_gui():
        read_width = 0
        read_height = 0
        read_drone = '0'

class app_debug():
    engine_run = False
    config_engine_run = False

def engine_config_get():
    global config_gui
    config = configparser.ConfigParser()
    config.read('config.ini')

    config_gui.read_width = int(config['CONFIG-EDITOR']['gui-width'])
    config_gui.read_height = int(config['CONFIG-EDITOR']['gui-height'])
    config_gui.read_drone = str(config['CONFIG-EDITOR']['gui-drone'])

def engine_run():
    global config_gui, app_debug

    screen = pygame.display.set_mode((config_gui.read_width, config_gui.read_height))
    pygame.display.flip()

    app_debug.config_engine_run = True
    while app_debug.config_engine_run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        app_debug.config_engine_run=False
    

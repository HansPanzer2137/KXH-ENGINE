import pygame as pg
import numpy as np


import time
import sys
import os
import configparser

import win32api



class Engine2D():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.WIDTH = config['CONFIG-EDITOR']['ENGINE2D-WIDTH']
        self.HEIGHT = config['CONFIG-EDITOR']['ENGINE2D-HEIGHT']

        self.RES = self.WIDTH, self.HEIGHT
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH //2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES, pg.FULLSCREEN)

        self.clock = pg.time.Clock()
        


    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT or i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE]
            self.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
from distutils.command.config import config
import os
import sys
import pygame as pg

import configparser
import tkinter as TK


from bib.GUI.engine3D.object3d import *
from bib.GUI.engine3D.camera import *
from bib.GUI.engine3D.projection import *



class SoftwareRender3D:
    def __init__(self):
        pg.init()
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.RES = self.WIDTH, self.HEIGHT = (int(config['CONFIG-EDITOR']['ENGINE-WIDTH'])), (int(config['CONFIG-EDITOR']['ENGINE-HEIGHT'] ))
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2 , self.HEIGHT // 2
        self.FPS = 60
        #if config['CONFIG-EDITOR']['engine-fullscreen'] == '1':
        self.screen = pg.display.set_mode(self.RES, pg.FULLSCREEN)
        #else:
            #self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_object()

    def create_object(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('darkslategrey'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT or i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


class SoftwareRender2D:
    def __init__(self):
        pg.init()
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.RES = self.WIDTH, self.HEIGHT = (int(config['CONFIG-EDITOR']['ENGINE-WIDTH'])), (int(config['CONFIG-EDITOR']['ENGINE-HEIGHT'] ))
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2 , self.HEIGHT // 2
        self.FPS = 60
        #if config['CONFIG-EDITOR']['engine-fullscreen'] == '1':
        self.screen = pg.display.set_mode(self.RES, pg.FULLSCREEN)
        #else:
            #self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        

    def draw(self):
        self.screen.fill(pg.Color('darkslategrey'))

    
    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT or i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

    

def engine3DRun():
    app = SoftwareRender3D()
    app.run()

def engine2DRun():
    app = SoftwareRender2D()
    app.run()


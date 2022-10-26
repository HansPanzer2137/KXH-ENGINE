from distutils.command.config import config
import os
import sys
import pygame as pg

import configparser
import tkinter as TK


from bib.gui.engine3D.object3d import *
from bib.gui.engine3D.camera import *
from bib.gui.engine3D.projection import *

from bib.gui.engine3D.OpenGL_acc.openGL_kernel import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from pygame.constants import *


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
        self.camera = Camera(self, [-500, 500, -5000])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('res/drone/class-K.obj')



    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f '):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

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

class OpenGL_SoftwareRender3D():
    def __init__(self):
        pg.init()
        viewport = (800, 600)
        hx = viewport[0]/2
        hy = viewport[1]/2
        srf = pg.display.set_mode(viewport, OPENGL | DOUBLEBUF)

        glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        obj = OBJ(sys.argv[1], swapyz=True)
        clock = pg.time.Clock()    

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        width, height = viewport
        gluPerspective(90.0, width/float(height), 1, 100.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

        rx, ry = (0, 0)
        tx, ty = (0, 0)
        zpos = 5
        rotate = move = False
    
        while True:
            clock.tick(30)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    sys.exit()
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()
                if e.type == MOUSEBUTTONDOWN:
                    if e.buuton == 4: zpos = max(1, zpos-1)
                    elif e.buuton == 5: zpos += 1
                    elif e.buuton == 1: rotate = True
                    elif e.button == 3: move == True
                if e.type == MOUSEBUTTONUP:
                    if e.button == 1: rotate = False
                    elif e.button == 3: move = False
                if e.type == MOUSEMOTION:
                    i, j = e.rel
                    if rotate:
                        rx += i
                        ry += j
                    if move:
                        tx += i
                        ty += j

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # type: ignore
            glLoadIdentity()


            glTranslate(tx/20., ty/20., - zpos)
            glRotate(ry, 1, 0, 0)
            glRotate(rx, 0, 1, 0)
            glCallList(obj.gl_list)

            pg.display.flip()


def engine3DRun():
    app = SoftwareRender3D()
    app.run()

def OpenGL_engine3DRun():
    app = OpenGL_SoftwareRender3D()
    app.run()

def engine2DRun():
    app = SoftwareRender2D()
    app.run()


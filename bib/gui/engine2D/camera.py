import pygame as pg
from bib.gui.engine2D.matrixFunctions import *


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])
        self.up = np.array([1, 0, 1])
        self.right = np.array([0, 1, 1])
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)
        self.near_plane = 0.1
        self.far_plane = 100
        self.moving_speed = 20

    def control(self):
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += self.up * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.up * self.moving_speed

        

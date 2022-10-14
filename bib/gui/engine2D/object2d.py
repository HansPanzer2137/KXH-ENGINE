import pygame as pg
import numpy as np

class Object3D:
        def __init__(self, render):
            self.render = render
            self.vertexes = np.array ([(0, 0, 0, 1), (0, 1, 0, 1), 
                                        (0, 0, 1, 1), (0, 1, 1, 1)])
            
            self.faces = np.array([(0, 1, 2, 3)])

        def draw(self):
            self.screen_projection()

        def screen_projection(self):
            vertexes = self.vertexes @ self.render.camera.camera_matrix()
            vertexes = vertexes @ self.render.projection.projection_matrix
            vertexes /= vertexes[:, -1].reshape(-1, 1)
            vertexes[(vertexes > 2) | (vertexes < -2)] = 0
            vertexes = vertexes @ self.render.projection.to_screen_matrix
            vertexes = vertexes[:, :2]

            for face in self.faces:
                polygon = vertexes[face]
                if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                    pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)

            for vertex in vertexes:
                if not np.any((vertexes == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

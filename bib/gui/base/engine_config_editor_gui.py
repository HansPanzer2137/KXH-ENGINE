from distutils.command.config import config
from pickletools import read_bytes8
import pygame
import os
import sys
import configparser
from PIL import Image
import time
FORMAT = "RGBA"


def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)

# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

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
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((config_gui.read_width, config_gui.read_height), pygame.NOFRAME)
    color = (255,255,255)
    pygame.display.set_caption('Save')

    

    pygame.display.flip()

    gif_img = Image.open('res/img/loading.gif')
    if not getattr(gif_img, "is_animated", False):
        print(f"Error, missing loading screen image")
        return
    current_frame = 0
    clock = pygame.time.Clock()

    app_debug.config_engine_run = True
    start = time.time()
    while app_debug.config_engine_run:
        frame = pil_to_game(get_gif_frame(gif_img, current_frame))
        screen.blit(frame, (0, 0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        app_debug.config_engine_run=False
        pygame.display.update()
        current_frame = (current_frame + 1) % gif_img.n_frames
        clock.tick(10)
        counter = time.time() - start
        print(counter)
        if counter >= 10:
            app_debug.config_engine_run=False
    
    return

    


       

                  
    

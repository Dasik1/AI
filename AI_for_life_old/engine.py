# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Thu Mar 30 13:21:42 2023
in Tims II Lab

@author: Stark
"""

import pygame as pg
from errors import *
import sys
from time import sleep


class WINDOW():
    def __init__(self, name = None, width = 1200, height = 800, fps = 45):
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        
        if name is not None:
            self.NAME = name
        else:
            raise NoDefinitionError("Window name")
        
        pg.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(name)
        self.clock = pg.time.Clock()


    def tick(self,time = 0.1):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
        self.clock.tick(self.FPS)
        pg.display.flip()
        sleep(time)
    
    
    def draw(self,figure,color = None, center = None, r = None,
                                       start_pos = None, end_pos = None,
                                       message = ''):
        if figure == "circle":
            pg.draw.circle(self.screen, color=color, center=center,radius=r)
        elif figure == "line":
            pg.draw.line(self.screen, color=color, start_pos=start_pos, end_pos=end_pos)
        elif figure in ["bg", "fill", "back"]:
            self.screen.fill(color=color)
        elif figure in ["rect", "sqare"]:
            pg.draw.rect(self.screen, color, start_pos)
        elif figure == "text":
            font = pg.font.SysFont(None, r)
            img = font.render(message, True, color)
            self.screen.blit(img,start_pos)
        
        
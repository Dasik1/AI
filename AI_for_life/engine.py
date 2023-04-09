# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Thu Feb  2 13:10:45 2023
in Tims II Lab

@author: Stark
"""

"""its an engine file, but its ther engine to only life game\
    so different AI prototypes can be displayed on similar engines"""



"""engine file ll have field and drawing"""
from errors import *
import pygame as pg
import sys
import random as rd
from random import randint as ri
from math import sqrt



class Field():
    def __init__(self,randcore = 73, spc = 5, sizeof_field = (10,10),maping = "random"):
        self.randcore = randcore
        self.spc = spc
        
        self.sizeof_field = sizeof_field
        
        
        rd.seed(randcore)
        self.fieldt = [[0]*sizeof_field[0] for x in range(sizeof_field[1])]
        self.fieldf = [[0]*sizeof_field[0] for x in range(sizeof_field[1])]
        
        
        if maping == "random":
            for i in range(sizeof_field[0]):
                for o in range(sizeof_field[1]):
                    self.fieldt[i][o] = [ri(-50,50)/10]
        if maping == "round":
            for i in range(sizeof_field[0]):
                for o in range(sizeof_field[1]):
                    self.fieldt[i][o] = (1-sqrt((i+1-sizeof_field[0]/2)**2+(
                                                    o+1-sizeof_field[1]/2)**2))+1
                    
                    if self.fieldt[i][o]>0:self.fieldt[i][o]*3
                    
                    self.fieldf[i][o] = 3.5-(sqrt((sizeof_field[0]/2)**2+(sizeof_field[1]/2)**2
                                )-sqrt((i+1-sizeof_field[0]/2)**2+(
                                                    o+1-sizeof_field[1]/2)**2))
 #                   self.fieldf[i][o]*=2
        
        
    def get_fieldt(self):
        return self.fieldt
    def get_fieldf(self):
        return self.fieldf
    
    def draw(self,win):
        win.draw("bg",color = (50,50,50))
        
        t = min([min(x) for x in self.fieldt])
        tm = max([max(x)-t for x in self.fieldt])
        f = min([min(x) for x in self.fieldf])
        fm = max([max(x)-f for x in self.fieldf])
        
        for i in range(len(self.fieldf)):
            for o in range(len(self.fieldf[0])):
                #print(i,o)
                win.draw("rect",
                        int(255*(-f+self.fieldf[i][o])/fm), 0, int(255*(-t+self.fieldt[i][o])/tm),
                        [i*80, o*80 , (i+1)*80 , (o+1)*80])
        
        
    




class Window():
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


    def tick(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
        self.clock.tick(self.FPS)
        pg.display.flip()
    
    
    def draw(self,figure,color = None, center = None, r = None,
                                       start_pos = None, end_pos = None):
        if figure == "circle":
            pg.draw.circle(self.screen, color=color, center=center,radius=r)
        elif figure == "line":
            pg.draw.line(self.screen, color=color, start_pos=start_pos, end_pos=end_pos)
        elif figure in ["bg", "fill", "back"]:
            self.screen.fill(color=color)
        elif figure == "rect":
            pg.draw.rect(self.screen, color, start_pos)
            
            
























if __name__ == "__main__":
    q = Field(maping = "round")
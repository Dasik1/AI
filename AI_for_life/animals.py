# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Feb  5 13:14:09 2023
in Tims II Lab

@author: Stark
"""


'''

Genes



'''

from errors import *


class GenEntity():
    
    def __init__(self, pos = [0,0], parent1 = None, parent2 = None):
        self.pos = pos
        self.genes = ''



from tensorflow import keras
import numpy as np

global xx,yy
xx = []
yy = []

class NetEntity():
    
    def __init__(self,temp_price, food_price, pos = [0,0], maxfood = 100, deadt = -50):
        
        
        
        self.pos = pos
        
        self.maxfood = maxfood
        self.food = maxfood
        
        self.maxtemp = 36
        self.temp = 0
        self.deadt = deadt
        
        self.temp_price = temp_price
        self.food_price = food_price
        self.deadtype = None
        
        self.temp_val = 15
        self.food_val = 2
        self.step = 0
        
        
        
        self.alive = True
        
    def move(self, f, key):
        key = key.tolist()
        print("wasd/pass", key,"    t ",self.temp,'    f',self.food)
        key = key.index(max(key))##as it numpy array
        if key == 0:
            self.pos[0] = min(max(0,self.pos[0]-1),f.sizeof_field[0]-1)
            
        if key == 2:
            self.pos[0] = min(max(0,self.pos[0]+1),f.sizeof_field[0]-1)
        
        if key == 1:
            self.pos[1] = min(max(0,self.pos[1]-1),f.sizeof_field[1]-1)
            
        if key == 3:
            self.pos[1] = min(max(0,self.pos[1]+1),f.sizeof_field[1]-1)
        
        
        self.temp = min((self.temp+f.get_fieldt()[self.pos[0]][self.pos[1]]),self.maxtemp)
        self.food = min((self.food+f.get_fieldf()[self.pos[0]][self.pos[1]]),self.maxfood)
        self.step +=0.1
        
    
    
    def init_model(self, model):
        self.model = model
    
    def predict(self, idata):
        return self.model.predict([idata])
        
    def fit(self, idata, revard):
        if len([idata])!=len([revard]):
            raise NotMatchingError("Data and reward")
        self.model.fit([idata],[revard],epochs=1, verbose=0)
    
    def get_pos(self):
        return self.pos
    
    def get_price(self,field):
        
        if self.temp<self.deadt:
            self.alive = False
            self.deadtype = "temp"
            return self.temp_price
        
        if self.food<0:
            self.alive = False
            self.deadtype = "food"
            return self.food_price
        
        
        '''
        1 try according to a field
        mi = []
        ma = []
        for i in field.get_fieldf():
            mi.append(min(i))
            ma.append(max(i))
        fmi = min(mi)
        fma = max(ma)
        mi = []
        ma = []
        for i in field.get_fieldt():
            mi.append(min(i))
            ma.append(max(i))
        tmi = min(mi)
        tma = max(ma)
        del mi,ma
        
        p = field.get_fieldt()[self.pos[0]][self.pos[1]]
        fn = p/fmi if p<0 else p/fma
        p = field.get_fieldf()[self.pos[0]][self.pos[1]]
        tn = p/tmi if p<0 else p/tma
        '''
        
        fn = -(100-self.food)/(self.maxfood)
        tn = -(self.temp)/(self.deadt)
        
        
        if fn>abs(tn):
            tn*=5
        else:
            tn*=5
        
        
        print("\n\n",tn,fn,"     ",int(self.temp),'  ', int(self.food
            ),"     ",int(self.temp_price),'  ', int(self.food_price),"\n\n")
        return self.temp_val*tn+self.food_val*fn+self.step*5
        
    
    def draw(self, win):
        k = 80
        win.draw("circle", color=(255,10,10),
                 center = [self.pos[0]*k+40,self.pos[1]*k+40], r=30)
        
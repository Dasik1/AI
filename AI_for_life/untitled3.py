# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Feb  5 18:51:34 2023
in Tims II Lab

@author: Stark
"""

from engine import Field, Window
from brains import Game
from animals import NetEntity

import numpy as np
from tqdm import tqdm as __

population = 10

f = Field(maping="round")
g = Game()

win = Window(name="RL bugs")




#
from tensorflow import keras
from keras.layers import InputLayer, Dense


for i in __(range(population),desc="initing"):
    entity = NetEntity()

    model = keras.Sequential()
    model.add(InputLayer(input_shape = (None, 1)))
    model.add(Dense(4,activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(5, activation='sigmoid'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])

    entity.init_model(model)
    
    g.add_entity(entity)

del entity

print("In game")
while g.are_living():
    
    entities = g.get_entities()
    
    #predict
    inp = []
    for entity in entities:
        inp.append(entity.predict(entity.get_pos().copy())[0])
        entity.move(inp[-1])
    
    
    #generate fit inp
    inp = []
    for entity in entities:
        inp.append(entity.get_pos().copy())
        inp[-1].append(f.get_fieldt()[inp[-1][0]][inp[-1][1]])
        inp[-1].append(f.get_fieldf()[inp[-1][0]][inp[-1][1]])
    
    
    #generate fit outp
    outp = []
    for entity in entities:
        outp.append(1)
    
    
    #fit
    for entity in entities:
        entity.fit(inp,outp)
    
    
    #draw
    f.draw()
    g.draw()
    
    
    win.tick()
# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Feb  5 18:51:34 2023
in Tims II Lab

@author: Stark
"""

global xx,yy
xx = []
yy = []



from engine import Field, Window
from brains import Game
from animals import NetEntity
from time import sleep as ZZZzzz

import numpy as np
from tqdm import tqdm as __

population = 1

f = Field(maping="round")
g = Game()

w = Window(name="RL bugs", width=800)




#
from tensorflow import keras
from keras.layers import InputLayer, Dense


for i in __(range(population),desc="initing"):
    entity = NetEntity(-200, -100)

    model = keras.Sequential()
    model.add(InputLayer(input_shape = (None, 1)))
    model.add(Dense(4,activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(10, activation='tanh'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(5, activation='sigmoid'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])

    entity.init_model(model)
    
    g.add_entity(entity)

del entity

#third leg

print("In game")
while True:
    
    while g.are_living():
#        g.print()
    
        entities = g.get_entities()
        
        #predict
        inp = []
        for entity in entities:
            inp.append(entity.predict(entity.get_pos().copy())[0][0])
            entity.move(f, inp[-1])
    
    
        #generate fit inp
        inp = []
        for entity in entities:
            inp.append(entity.get_pos().copy())
            inp[-1].append(f.get_fieldt()[inp[-1][0]][inp[-1][1]])
            inp[-1].append(f.get_fieldf()[inp[-1][0]][inp[-1][1]])
        
        
        #generate fit outp
        outp = []
        for entity in entities:
            outp.append(entity.get_price(f))
        
        
        #fit
        for i in range(len(entities)):
            #print(inp,outp,'\n')
            entities[i].fit(inp[i],outp[i])
        
        
        #draw
        f.draw(w)
        g.draw(w)
    
    
        w.tick()
        print("\n\n")
    
    g.respawn()
    entities = g.get_entities()
    for entity in entities:
        fm = entity.food_val
        tm = entity.temp_val
        if entity.deadtype == "food":
            fm -=1
        if entity.deadtype == "temp":
            tm -=1
        entity.__init__(tm, fm, pos = [4,4])
        
    print("ewryone died")
#    ZZZzzz(5)
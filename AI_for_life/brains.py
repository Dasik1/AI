# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Feb  4 23:48:29 2023
in Tims II Lab

@author: Stark
"""
from time import sleep

class Game():
    
    def __init__(self):
        self.entities = []
        self.dead_entities = []
    
    def add_entity(self,entity):
        self.entities.append(entity)
    
    def rem_entity(self,entity):
        del self.entities[entity]
        
    
    def get_entities(self):
        #check if living else remove
        return self.entities
    
    def respawn(self):
        self.entities = self.dead_entities.copy()
        self.dead_entities = []
    
    
    def are_living(self):
        
        while(any([not self.entities[x].alive for x in range(len(self.entities))])):
            for i in range(len(self.entities)):
                if self.entities[i].alive == False:
                    self.dead_entities.append(self.entities[i])
                    del self.entities[i]
                    break
        
        return True if len(self.entities)>0 else False
        
    
    def draw(self,win):
        for entity in self.entities:
            entity.draw(win)
    
    def print(self):
        print(self.entities)
        
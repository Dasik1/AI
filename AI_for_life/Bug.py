# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Thu Jul  6 12:56:42 2023
in Tims II Lab

@author: Stark
"""
from AI import ENTITY

class BUG(ENTITY):
    '''Entity son))
    used for adding main functions
    
    all nesessary was inited in Entity'''
    def __init__(self, Field):
        super().__init__(Field)
        
        
        self.packed_data = {
            'food' : 100,
            'energy' : 100,
            'pos' : [1,1]}
    
    def eat(self):
        if self.packed_data["pos"] == [0,0]:
            self.packed_data["food"] += 10
    def charge(self):
        if self.packed_data["pos"] == [5,5]:
            self.packed_data["energy"] += 10
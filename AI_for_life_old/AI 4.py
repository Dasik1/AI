# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:41:47 2023

@author: Stark
"""

class Entity:
    """5x5 field where u have food and energy points
    
    Entity have 2 params food and energy
    It knows the field
        where to go to increase one of params
        
    Desigion is taken acording to entities` needs
        ex.
        i am near pos = 
        {energy : low
         food : high}
        
        i need to go to eat
        
        so we need to make path to place and go there
    """
    
    def __init__(self):
        """on init we say that we know some paterns
        and functions"""
        
        self.patterns = {}
        self.functions = {}
        self.abilities = {}
        
    
    def set_pattern(self, name, dict_pattern):
        """add pattern to a list #no override safety
        ex (1, {energy: 1, food: 100})"""
        self.patterns[name] = dict_pattern
    
    def set_main_functions(self, name, dict_func):
        """add func to a list #no override safety
        func is 
        {from: id, to: id, func: f}"""
        if (not any([x not in ['from','to','func'] for x in dict_func.keys()])
            ) and (not any([x not in dict_func.keys() for x in ['from','to','func']])):
            self.patterns[name] = dict_func
        
    def set_abilities(self, name, func):
        self.abilities[name] = func







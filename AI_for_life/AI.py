# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:41:47 2023

@author: Stark
"""
from optims import mse
import numpy as np

class ENTITY:
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
    
    def __init__(self, Field = None):
        """on init we say that we know some paterns
        and functions"""
        
        self.patterns = {}
        self.functions = {}
        self.abilities = {}
        self.Field = Field
        
    
    def set_pattern(self, name, dict_pattern):
        """add pattern to a list #no override safety
        ex (1, {energy: 1, food: 100})"""
        self.patterns[name] = dict_pattern
    
    def set_main_functions(self, name, dict_func):
        """add func to a list #no override safety
        func is 
        {from: id, to: id, func: f}"""
        if (not any([x not in ['from','to','func','pos'] for x in dict_func.keys()])
            ) and (not any([x not in dict_func.keys() for x in ['from','to','func','pos']])):
            self.patterns[name] = dict_func
        
    def set_abilities(self, name, func):
        self.abilities[name] = func
    
    def set_target(self, key):
        self.target = key
    
    
    def think(self, mse_passing):
        """main callable func, where all logic has been written"""
        
        self.pattern_pos = self.match_pattern(mse_passing)
        self.wanted_pos = self.plan()
        self.decide(self.create_tree(self.pattern_pos, self.wanted_pos))
        
    
    
    
    
    def match_pattern(self, mse_passing):
        """"""
        self.pattern_weight = []
        for key in self.patterns.keys():
            self.pattern_weight.append([key,mse(self.packed_data, self.patterns[key],
                      mse_passing)])
            
        return self.pattern_weight[np.argmin(self.pattern_weight)]
    
    def plan(self):return self.target
    
    
    def create_tree(self, _from, _to, path = [], depth_limit = 15):
        
        if _from == _to:
            
            path.append(_to)
            
            self.tree_path.append(path.copy())
            if len(path) == 1:
                self.tree_path[-1].append(_to)
            del path[-1]

            return
        
        if len(path)==depth_limit:
            return
        
        for bench in self.tree:
            if bench[0] == _from:
                path.append(bench[0])
                self.find_path(bench[1],_to, path)
                del path[-1]
        
        
        #look for next
        
        
        pass
    
    def decide(self, tree):pass







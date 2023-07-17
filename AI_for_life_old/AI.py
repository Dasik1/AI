# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Mar 29 19:43:31 2023
in Tims II Lab

@author: Stark
"""
_ = float("inf")

def mse(q,w):
    if any([type(x) != type({}) for x in [q,w]]):
        return _
    
    mse_val = 0
    
    for key in q.keys():
        if key in w.keys():
            mse_val += (q[key]-w[key])**2
        else:
            mse_val += (q[key])**2
    
    for key in (set(w.keys())-set(q.keys())):
        mse_val += (w[key])**2
    
    return mse_val

class AI:
    
    def __init__(self,entity):
        pass
        
        #now we have a tree with one connection and loop
        #to think we dont have a chance to make two simmilar connections
    
    def get_tree(self, tree):
        self.tree = tree
        
    def get_vector(self, end):
        self.destination = end
    
    
    
    
    def find_path(self, _from, _to, path = [], depth_limit = 15):
        #рекурсивный алг. поиска 
        #прямой шаг до исчерпания глубины
        #если глубина то выход с кодом 0
        
        
        
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
                self.find_path(bench[1],_to, path,depth_limit=depth_limit)
                del path[-1]
        
        
    
    
    def think(self,now_env):
        
        weights = []
        for env in self.points:
            weights.append(mse(env["data"],now_env))
        
        
        position = self.points[weights.index(min(weights))]#take most similar point in the tree
        self.tree_path = []
        self.find_path(position["id"], self.destination["id"])
        
        return self.tree_path
    
    def decide(self, move):
        funcs = []
        for bench in self.tree:
            if list(bench[:2]) == move[:2]:
                funcs.append(bench[2])
        return funcs
    
# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Mar 29 20:07:54 2023
in Tims II Lab

@author: Stark
"""

'''

now we need to solve smth that called 

MOVEMENT


перемещение обеспечивает сложность если не невозможность решения

возможно появление петель и надо бороться....

будем считать что ход в более холодное место это плохо


'''

from optims import mse


class ENTITY_2:
    def __init__(self):
        self.energy = 100
        self.field = [4,-1,-1,-1,-2]
        self.pos = 2
        
    def live(self):
        self.energy +=self.field[self.pos]
    
    def left(self):
        print("left")
        self.pos = max(0,self.pos-1)
    
    def right(self):
        print('right')
        self.pos = min(4,self.pos+1)
    
    def default(self):
        print("sleep")
    
    def get_env(self):
        return {"energy":self.energy,"pos":self.pos}


class AI_2:
    '''
simple method for one par.
    '''
    def __init__(self,entity):
        #this par ll be energy
        
        llowenergy = {'id':11,
                     "data":{"energy":5,
                             "pos":0}
                     }
        rlowenergy = {'id':12,
                     "data":{"energy":5,
                             "pos":4}
                     }
        
        lhighenergy = {'id':21,
                     "data":{"energy":100,
                             "pos":0}
                     }
        rhighenergy = {'id':22,
                     "data":{"energy":100,
                             "pos":4}
                     }
        
        
        self.destination = rhighenergy
        
        self.points = [llowenergy,rlowenergy,lhighenergy,rhighenergy]
        
        
        self.tree = [    #from              #to              #weight
                     ( llowenergy["id"], lhighenergy["id"], entity.left,0),
                     ( llowenergy["id"], rlowenergy["id"], entity.right,2),
                     ( rlowenergy["id"], llowenergy["id"], entity.left,1),
                     ( lhighenergy["id"], rhighenergy["id"], entity.right,1),
                     ( rhighenergy["id"], lhighenergy["id"], entity.left,1),
                     ( rhighenergy["id"], rhighenergy["id"], entity.default,0)
                     ]
        
        #now we have a tree with one connection and loop
        #to think we dont have a chance to make two simmilar connections
    
    
    def find_path(self, _from, _to, path = [], depth_limit = 15):
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
                self.find_path(bench[1],_to, path)
                del path[-1]
        
        
        #look for next
        
        
        pass
    
    
    def think(self,now_env):
        
        weights = []
        for env in self.points:
            weights.append(mse(env["data"],now_env))
            
        
        position = self.points[weights.index(min(weights))]#take most similar point in the tree
        self.tree_path = []
        self.find_path(position["id"], self.destination["id"])
        
        print(self.tree_path)
        
        return self.tree_path
    
    def decide(self, move):
        funcs = []
        for bench in self.tree:
            if list(bench[:2]) == move[:2]:
                funcs.append(bench[2])
        
        return funcs
    
    
    
Entity = ENTITY_2()
AI = AI_2(Entity)
q = AI

from time import sleep
from random import choice as ch



while True:
    Entity.live()
    
    moves = AI.think(Entity.get_env())# <-- набор возможных ходов
    print(moves[0])
    
        

    
    #выбрали ребро, выберем функцию но изза 
    func = ch(
                AI.decide(moves[0])
            )
    
    func()
    
    print(Entity.energy, Entity.pos,'\n\n')
    sleep(0.1)
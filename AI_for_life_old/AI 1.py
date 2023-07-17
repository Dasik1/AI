# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Tue Mar 28 23:04:16 2023
in Tims II Lab

@author: Stark
"""

"""

есть n параметров

=> сущ. 2**n сред где каждый параметр представлен хорошо/смертельно плохо 
(иначе получим немного бесконечное число сред)

среды связанны между собой функциями перехода


например:

среда1 - голодный
среда2 - наевся

граф:

    1 -(поесть)- 2


сопоставим каждому положению из бесконечного - среде коеффициент схожести с конечными заданными 

выполним наиболее подходящее действие и запомним, что его мы делали
потом это пригодится для разноображивания (except OrthoepicInsult)


немного костылей, если мрога попадает в цикл то мы стучим ей по голове и выкидываем наименее важное действие
пусть она умрет уверенной в завтрашнем дне

##тут надо нашакалить оптимизацией и логикой



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


class ENTITY_1:
    def __init__(self):
        self.energy = 100
        
    def live(self):
        self.energy -=1
    
    def charge(self):
        print("recharge")
        self.energy = 100
    
    def default(self):
        print("sleep")
    
    def get_env(self):
        return {"energy":self.energy}


class AI_1:
    '''
simple method for one par.
    '''
    def __init__(self,entity):
        #this par ll be energy
        
        lowenergy = {'id':1,
                     "data":{"energy":5}
                     }
        
        highenergy = {'id':2,
                     "data":{"energy":100}
                     }
        midenergy = {'id':3,
                     "data":{"energy":50}
                     }
        
        self.destination = highenergy
        
        self.points = [lowenergy,highenergy]
        
        
        self.tree = [    #from              #to              #weight
                     ( lowenergy["id"], highenergy["id"], entity.charge),
                     ( lowenergy["id"], midenergy["id"], entity.charge),
                     ( midenergy["id"], highenergy["id"], entity.charge),
                     (highenergy["id"], highenergy["id"], entity.default)]
        
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
        
        return self.tree_path
    
    def decide(self, move):
        funcs = []
        for bench in self.tree:
            if list(bench[:2]) == move[:2]:
                funcs.append(bench[2])
        return funcs
        

    

Entity = ENTITY_1()
AI = AI_1(Entity)
q = AI

from time import sleep
from random import choice as ch



while True:
    Entity.live()
    
    move = ch(
                AI.think(Entity.get_env())# <-- набор возможных ходов
               )
    
    #выбрали ребро, выберем функцию
    func = ch(
                AI.decide(move)
                )
    
    func()
    
    print(Entity.energy)
    sleep(0.1)
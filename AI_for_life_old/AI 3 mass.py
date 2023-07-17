# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Thu Mar 30 12:41:16 2023
in Tims II Lab

@author: Stark
"""


"""

in ex 2 we had a problem
he didnt understand where he is in betwined situations

lets save where he wannna go




"""




from optims import mse


class ENTITY_3:
    def __init__(self):
        self.energy = 100
        self.field = [4,-1,-1,-1,-2]
        self.pos = 4
        
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


class AI_3:
    '''
simple method for one par.
    '''
    def __init__(self,entity,accuracy = 100):
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
        
        self.accuracy = accuracy
        self.vector = 1  #inputed by hands
    
    
    def find_path(self, _from, _to, path = [], depth_limit = 15):
        
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
    
    
    def think(self,now_env,
              activation_func = lambda x:x[0]):
        
        weights = []
        for env in self.points:
            weights.append(mse(env["data"],now_env))
            
        
        if self.vector is None:
            pos = weights.index(min(weights))
            self.vector = pos
        
        else:
            for i in range(len(weights)):
                if weights[i] <self.accuracy:
                    self.vector = i
            pos = self.vector
            
        
        
        
        
        
        
        
        
        position = self.points[pos]#take most similar point in the tree
        self.tree_path = []
        self.find_path(position["id"], self.destination["id"])
        desided_path = activation_func(self.tree_path)
        
        
        print(weights)
        print(self.tree_path)
        
        
        
        return desided_path
    
    def decide(self, move):
        funcs = []
        for bench in self.tree:
            if list(bench[:2]) == move[:2]:
                funcs.append(bench[2])
        
        return funcs
    
    
    
Entity = ENTITY_3()
AI = AI_3(Entity,accuracy=300)
q = AI #third leg for spyder


from random import choice as ch
from engine import WINDOW

Window = WINDOW(name="v3",width=900,height = 400)




while True:
    Entity.live()
    
    moves = AI.think(Entity.get_env())# <-- набор возможных ходов
    
    
        

    
    #выбрали направление, выберем какое из ребер если их несколько
    func = ch(
                AI.decide(moves)
            )
    
    func()
    
    Window.draw("bg",(30,30,30))
    Window.draw("sqare",(255,150,150),start_pos=(101,101,148,148))
    Window.draw("sqare",(150,150,150),start_pos=(251,101,148,148))
    Window.draw("sqare",(150,150,150),start_pos=(401,101,148,148))
    Window.draw("sqare",(150,150,150),start_pos=(551,101,148,148))
    Window.draw("sqare",(150,150,255),start_pos=(701,101,148,148))
    
    env = Entity.get_env()
    en = env['energy']
    pos = env['pos']
    
    Window.draw("text",(255,255,255),r=20,start_pos=(10,10),
                message=f"energy - {en}")
    Window.draw("text",(255,255,255),r=20,start_pos=(10,23),
                message=f"decided pos - {AI.vector}")
    
    #find name
    information = "None"
    information = AI.points[AI.vector]["data"]

    
    
    Window.draw("text",(255,255,255),r=20,start_pos=(10,36),
                message=f"decided pos - {information}")
    Window.draw("circle",(10,255,10),center=(175+pos*150,175),r=60)
    
    
    
    Window.tick(0.5)
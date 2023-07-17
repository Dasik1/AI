# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Thu Jul  6 12:26:05 2023
in Tims II Lab

@author: Stark
"""

from Bug import BUG


Bug = BUG(1)

Bug.set_pattern("starving", {"energy":5,"food":5})
Bug.set_pattern("hungry", {"energy":100,"food":5})
Bug.set_pattern("tired", {"energy":5,"food":100})
Bug.set_pattern("happy", {"energy":100,"food":100})


Bug.set_main_functions('eat_low', {"from":"starving", "to":"tired", "func":Bug.eat,
                                   "pos":[0,0]})
Bug.set_main_functions('eat_high', {"from":"hungty", "to":"happy", "func":Bug.eat,
                                    "pos":[0,0]})

Bug.set_main_functions('charge_low', {"from":"starving", "to":"hungry", "func":Bug.charge,
                                      "pos":[5,5]})
Bug.set_main_functions('charge_high', {"from":"tired", "to":"happy", "func":Bug.charge,
                                       "pos":[5,5]})




while True:
    
    action = Bug.think(mse_passing = True)
    break
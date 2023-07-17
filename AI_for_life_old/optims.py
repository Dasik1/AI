# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Mar 29 21:00:18 2023
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
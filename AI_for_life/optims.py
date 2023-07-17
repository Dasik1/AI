# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Mar 29 21:00:18 2023
in Tims II Lab

@author: Stark
"""
_ = float("inf")
def mse(q,w, passing = True, alpha = 2):
    if any([type(x) != type({}) for x in [q,w]]):
        return _
    
    mse_val = 0
    
    for key in q.keys():
        
        if key in w.keys():
            if type(q[key]) in [list, dict]:
                
                for i in range(len(q[key])):
                    mse_val += (q[key][i]-w[key][i])**alpha
            else:
                mse_val += (q[key]-w[key])**alpha
        elif not passing:
            if type(q[key]) in [list, dict]:
                for i in range(len(q[key])):
                    mse_val += (q[key][i])**alpha
            else:
                mse_val += (q[key])**alpha
    
    if not passing:
        for key in (set(w.keys())-set(q.keys())):
            if type(q[key]) in [list, dict]:
                for i in range(len(q[key])):
                    mse_val += (w[key][i])**alpha
            else:
                mse_val += (w[key])**alpha
    
    return mse_val
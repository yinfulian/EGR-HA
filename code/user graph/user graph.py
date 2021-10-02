# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:26:21 2020

@author: 18404
"""

import networkx as nx
import dgl


import torch as th
import numpy as np
import scipy.sparse as spp


import os
os.chdir('D:/推荐实验/5-推荐/4-增强知识推荐/code/用户和用户图/')
u_1=[]
v_1=[]

with open('user_user_relations_201506.txt','r',encoding='utf-8') as f:
    context=f.readlines()
    for i in context:
        i_split=i.split('|')
        u_1.append(int(i_split[0]))
        v_1.append(int(i_split[1]))
        
# Create a star graph from a pair of arrays (using ``numpy.array`` works too).
u = th.tensor(u_1)
v = th.tensor(v_1)
start1 = dgl.DGLGraph((u, v))


nx.draw(start1.to_networkx(), with_labels=True)


#提取编号为0的用户
u_1=[]
v_1=[]

with open('user_user_relations_201506.txt','r',encoding='utf-8') as f:
    context=f.readlines()
    for i in context:
        i_split=i.split('|')
        if str(0) in i_split:
            u_1.append(int(i_split[0]))
            v_1.append(int(i_split[1]))
            
u = th.tensor(u_1)
v = th.tensor(v_1)
start1 = dgl.DGLGraph((u, v))


nx.draw(start1.to_networkx(), with_labels=True)
len(u)
        

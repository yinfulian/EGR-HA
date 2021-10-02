# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:05:59 2020
构造数据
@author: 10460
"""
import os
os.chdir('D:/work/5-推荐/4-增强知识推荐/data/month5')
data=[]
userid=[]
itemid=[]
with open('u10000_p2422_interesing_label_glabel_201505.txt') as f:
    for line in f.readlines():
        line_splits=[i.strip() for i in line.split('|')]
        userid.append(line_splits[0])
        itemid.append(line_splits[1])
        if float(line_splits[2])>0.5:
            data.append(line_splits)
        else:pass
print(data[0])
print(len(data))
userid=list(set(userid))
itemid=list(set(itemid))
print(len(userid))
print(len(itemid))
#user_program=[]
train_data=[]
val_data=[]
test_data=[]

for index in range(10000):
    
    items=[int(d[1]) for d in data if d[0]==str(index)]
    #user_program[uid]=items
    train_index=int(6*(len(items)/10))
    val_index=int(2*len(items)/10)
    
    
    train_data.append([[int(index)]+items[:train_index]])
    val_data.append([[int(index)]+items[train_index:train_index+val_index]])
    test_data.append([[int(index)]+items[train_index+val_index:]])
    
    
with open('test.txt','w',encoding='utf-8') as f:
    for t in test_data:
        #print(t[0])
        new=[str(i) for i in t[0]]
        f.write(' '.join(new)+'\n')
        
    





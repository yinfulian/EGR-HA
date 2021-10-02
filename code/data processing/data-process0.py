# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:36:10 2020

@author: 10460
"""

import os
os.chdir("F:/222.31.102.30备份/收视数据（只允许读）/歌华201408-201604/")
def read_txt(x):
    broot=x+'/0101/'

    file_names = os.listdir(broot) #读取11文件夹下所有的（520个）txt的文件名
    file_content = []   #定义一个列表，用来存放刚才读取的520个txt文件名
    for file_name in file_names:  #循环地给这520个文件名加上它前面的路径，以得到它的具体路径
        fileob = broot + file_name #文件夹路径加上\\ 再加上具体要读的的txt的文件名就定位到了这个txt
        with open(fileob, encoding='utf-8') as fileread:
            file_content=fileread.readlines()+file_content
    new_content=[]
    for line in file_content:
        line_split=line.split('|')
        if len(line_split)>6:
            if int(line_split[5])>300:
                new_content.append(line_split)
        else:continue
            
    #print(len(new_content))
    
    return new_content,len(new_content)
    
def save_txt(context):
    with open("F:/222.31.102.30备份/收视数据（只允许读）/歌华数据说明/all_orignal_data/201408.txt","w") as f:
        for line in context[:]:            
            f.write('|'.join(line))
    f.close()
            
root='F:/222.31.102.30备份/收视数据（只允许读）/歌华201408-201604/'

file_names = os.listdir(root)[:] #读取11文件夹下所有的（520个）txt的文件名
context= []   #定义一个列表，用来存放刚才读取的520个txt文件名
for x in file_names[:]:  #循环地给这520个文件名加上它前面的路径，以得到它的具体路径

    per_context,len_data=read_txt(x)
    context=per_context+context #文件夹路径加上\\ 再加上具体要读的的txt的文件名就定位到了这个txt  
    print(x+' '+str(len_data))
print(len(context))
#save_txt(context)


            

    
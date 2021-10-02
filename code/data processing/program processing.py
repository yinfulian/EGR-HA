# -*- coding: utf-8 -*-
"""
Spyder Editor
节目单数据处理
This is a temporary script file.
"""

import os
import csv
import pandas as pd

os.chdir('D:/推荐实验/歌华数据说明/')

def read_excel(excel_name):
    
    with open(excel_name, 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        programs_list = list(reader)
        
    new_programs_dict={}
    for line in programs_list:
        
        p=line[8]
        label=[line[12],line[13],line[14]]

        if '、' in label[2]:
            l3=label[2].split('、')
        else:l3=[label[2]]
        if '/' in label[0]:
            l1=label[0].split('/')
        else:l1=[label[0]]
        if '/' in label[1]:
            l2=label[1].split('/')
        else:l2=[label[1]]
        new_labels=l1+l2+l3
        new_labels=[i.strip() for i in new_labels if len(i)!=0 and i!=' ' and i!='NULL']
        new_programs_dict[p]=list(set(new_labels))
        

    return new_programs_dict
    
def mix_program():
    program_dict=new_programs_dict5
    for i in new_programs_dict6:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict6[i]))
        else:program_dict[i]=new_programs_dict6[i]
    for i in new_programs_dict7:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict7[i]))
        else:program_dict[i]=new_programs_dict7[i]    
    for i in new_programs_dict8:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict8[i]))
        else:program_dict[i]=new_programs_dict8[i]
    for i in new_programs_dict9:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict9[i]))
        else:program_dict[i]=new_programs_dict9[i]        
    for i in new_programs_dict10:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict10[i]))
        else:program_dict[i]=new_programs_dict10[i]        
    for i in new_programs_dict11:
        if i in program_dict:
            program_dict[i]=list(set(program_dict[i]+new_programs_dict11[i]))
        else:program_dict[i]=new_programs_dict11[i]   
    return program_dict

def read_exist_program_data(inputfile):
    with open(inputfile, 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        programs_list = list(reader)
    exist_program_dict={}
    for line in programs_list[1:]:
        p=line[0]
        label=line[1:]
        new_labels=[]
        for l in label:
            if l!='0':
                new_labels.append(l)
        exist_program_dict[p]=list(set(new_labels))
    return exist_program_dict
                
                
def mix_programs_dict():
    
    for i in program_dict:
        if i in exist_program_dict:
            program_dict[i]=list(set(program_dict[i]+exist_program_dict[i]))
        else:pass
    return program_dict
        
        
        
def save_txt(program_dict):
    with open("新节目单201505-11月.txt","w",encoding='utf-8') as f:
        for line in program_dict:
            write_str=str(line)+'|'+'|'.join(program_dict[line])
            
            f.write(write_str+'\n')
    f.close()
        
excel_name05='节目单数据/201505-ok.csv' 
new_programs_dict5=read_excel(excel_name05)
excel_name06='节目单数据/201506-ok.csv' 
new_programs_dict6=read_excel(excel_name06)
excel_name07='节目单数据/201507-ok.csv' 
new_programs_dict7=read_excel(excel_name07)
excel_name08='节目单数据/201508-ok.csv' 
new_programs_dict8=read_excel(excel_name08)
excel_name09='节目单数据/201509.csv' 
new_programs_dict9=read_excel(excel_name09)
excel_name10='节目单数据/201510.csv' 
new_programs_dict10=read_excel(excel_name10)
excel_name11='节目单数据/201511.csv' 
new_programs_dict11=read_excel(excel_name11)

program_dict=mix_program()
print(len(list(program_dict.keys())))


#读入已有的节目单数据
inputfile = "节目单.csv"

exist_program_dict=read_exist_program_data(inputfile)


program_dict=mix_programs_dict()
save_txt(program_dict)


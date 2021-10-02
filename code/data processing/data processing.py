# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:08:33 2020
读入直播数据
进行处理解析
连接
@author: 18404
"""
import os
import csv
import time, datetime

os.chdir('F:/222.31.102.30备份/收视数据（只允许读）/歌华数据说明/')

def read_txt(fileob):
    #读入每一个月的数据
    
    with open(fileob, encoding='utf-8') as fileread:
        per_month_context=fileread.readlines()
    
    new_per_month_context=[]  
    for line in per_month_context:
        line_split=line.split('|')
        if len(line_split)>6:
            if int(line_split[6])==257 and line_split[-1]!='1!0!0\n':
                start_seconds,end_seconds=user_time(line_split[4],line_split[5])
                line_split[4]=start_seconds
                line_split[5]=end_seconds
                line_split[-1]=line_split[-1][:-5]
                new_per_month_context.append(line_split[1:])
        else:continue
    return new_per_month_context
    
def kua_zero_time_process(start_seconds,end_seconds):

    s1=start_seconds
    e1=86400
    s2=0
    e2=end_seconds
    return 

        

        
def read_excel(excel_name):
    
    with open(excel_name, 'r') as f:
        reader = csv.reader(f)
        #print(type(reader))
        programs_list = list(reader)
        
    new_programs_list=[]
    for line in programs_list:
        new_line=line[3:-3]
        nnew_line=new_line[:7]+new_line[9:]
        s_h, s_m, s_s = nnew_line[3].strip().split(':')
        start_seconds=int(s_h)*3600 + int(s_m)*60 + int(s_s)
        e_h, e_m, e_s = nnew_line[4].strip().split(':')
        end_seconds=int(e_h)*3600 + int(e_m)*60 + int(e_s)

        if start_seconds>end_seconds:
            nnew_line[3]=start_seconds
            nnew_line[4]=86400                        
            new_programs_list.append(nnew_line)
            nnew_line[3]=0
            nnew_line[4]=end_seconds
            nnew_line[2]=nnew_line[2].split('/')[0]+'/'+nnew_line[2].split('/')[1]+'/'+str(int(nnew_line[2].split('/')[-1])+1)           
            new_programs_list.append(nnew_line) 
        else:
            nnew_line[3]=start_seconds
            nnew_line[4]=end_seconds
            new_programs_list.append(nnew_line)

    return new_programs_list

#时间都转成秒处理
def user_time(start_time,duration):
    s_h=start_time[:2]
    s_m=start_time[2:4]
    s_s=start_time[4:]
    start_seconds=int(s_h)*3600 + int(s_m)*60 + int(s_s)
    end_seconds=start_seconds+int(duration)
    return start_seconds,end_seconds


#    
def combine_user_and_program(new_per_month_context,new_programs_list):
    user_program_records=[]
    for i in new_per_month_context[:]:
        
        pd_id=i[-1]
        date=i[0][6:]
        if date[0]=='0':
            date=date[1]
        start_seconds,end_seconds=i[3],i[4]
        user_records=[j for j in new_programs_list if pd_id in j and j[2].split('/')[-1]==date]
        
        for ii in user_records:
            #print(ii)
            p_s,p_e=ii[3],ii[4]
            if start_seconds>=p_s and end_seconds>=p_e and p_e>=start_seconds:
                u_watch_p_s,u_watch_p_e=start_seconds,p_e
            elif start_seconds>=p_s and end_seconds<=p_e:
                u_watch_p_s,u_watch_p_e=start_seconds,end_seconds            
            elif start_seconds<=p_s and end_seconds>=p_e:
                u_watch_p_s,u_watch_p_e=p_s,p_e             
            elif start_seconds<=p_s and end_seconds<=p_e and p_s<=end_seconds:
                u_watch_p_s,u_watch_p_e=p_s,end_seconds
            else:u_watch_p_s,u_watch_p_e=0,0
            
            if u_watch_p_s!=u_watch_p_e:
                user_program_records_line=[i[2],i[0],u_watch_p_s,u_watch_p_e,p_s,p_e,pd_id,ii[1],ii[5],ii[6],ii[7],ii[8]]
                if user_program_records_line[-1]!='广告':
                    user_program_records.append(user_program_records_line)
            else:pass
        
    return user_program_records
            
        
            
    
        
fileob='all_orignal_data/201408.txt'       
new_per_month_context=read_txt(fileob)  

excel_name='节目单数据/201408.csv' 
new_programs_list=read_excel(excel_name)
     
        

    
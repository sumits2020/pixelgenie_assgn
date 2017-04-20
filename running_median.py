# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:48:20 2017

@author: Sumit Saurabh
"""
import os
    #RUNNING MEDIAN CODE
def start():
    os.chdir(os.getcwd()+'\\wc_output')
    ip = open("result.txt","r").read().splitlines()
    #ip = ip.read()
    #print(ip)


    num_words =0  
    count=[] 
    j=0
    for i in ip:
        words = i.split(' ')
        num_words+= len(words)
        count.append(num_words)
        #print(count[j])
        num_words=0
        j=j+1
        
        



        temp= []
    median=0

    for i in range(0, len(count)):
        temp.append(count[i])
        sort_numbers(temp)
        #print(temp)
        #print(len(temp)%2)
        if(len(temp)%2 == 0):
            k1=int((len(temp))/2)
            k2=int(((len(temp))/2)+1)
            median= float((temp[k1-1]+temp[k2-1])/2)
        else:
            k3=int((len(temp)+1)/2)
            median= float(temp[k3-1])
        print(median)
    
def sort_numbers(count):

    for i in range(1, len(count)):
        val = count[i]
        j = i - 1
        while (j >= 0) and (count[j] > val):
            count[j+1] = count[j]
            j = j - 1
        count[j+1] = val
   
if __name__ == "__main__":
    start()
    
   
      

    
        

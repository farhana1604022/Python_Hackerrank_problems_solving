# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:04:04 2020

@author: ASUS
"""

graph={
       'a':['b','c'],
       'b':['d','e'],
       'c':['f'],
       'd':[],
       'e':['f'],
       'f':[]
       
       }
visited=[]
def ids(start,final):
    if start==final:
        print(start)
    
    else:
        for i in range(int(final)):
           
            def dfs(visited,graph,start):
                 if start not in visited:
                     print(start)
                     visited.append(start)
                     for neighbour in graph[start]:
                         dfs(visited,graph,neighbour)
                    
ids('a','c')                    
            
        
         
            
            
               
                    
                    
                         
             
                                      
                
    
        
        
        
            
        
    
        
        
        
        
        

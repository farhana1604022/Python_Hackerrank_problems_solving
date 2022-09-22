# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:19:14 2020

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
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
bfs(visited,graph,'a')       
        
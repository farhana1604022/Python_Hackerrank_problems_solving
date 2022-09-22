# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:27:47 2020

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

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'a')            
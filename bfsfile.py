# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:47:27 2020

@author: ASUS
"""

myfile=open('bfsinput.txt','w')
myfile.write(  

graph={
       'a':['b','c'],
       'b':['d','e'],
       'c':['f'],
       'd':[],
       'e':['f'],
       'f':[]
        
       }
)
myfile.close()
visited=[]
queue=[]
n=open('bfsinput.txt','r+')
def bfs(visited,n,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        
        for neighbour in n[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
bfs(visited,n,'a')       
        
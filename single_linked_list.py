# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:53:51 2020

@author: ASUS
"""
class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None
        #self.tail=None
    def printlist(self):
        node=self.head
        while (node):
            print(node.val)
            node=node.next
    def __str__(self):
        list1=[]
        temp=self.head
        while temp is not None:
            list1.append(temp.val)
            temp=temp.next
        return f"[{','.join(str(val) for val in list1)}]"
    def push(self,valu):
        new_node=Node(valu)
        new_node.next=self.head
        self.head=new_node
    def middle_insert(self,prev_node,new_node):
        new_node=Node(new_node)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def last_insert(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            return
        tail=self.head
        while tail.next is not None:
            tail=tail.next
        tail.next=new_node
        
            
        
        
my_list= Singlelinkedlist()
my_list.head=Node(1)
node2=Node(2)
node3=Node(3)

my_list.head.next=node2
node2.next=node3

print(my_list.printlist())
my_list.push(4)
print(my_list)

my_list.middle_insert(my_list.head.next.next,9)
print(my_list)
my_list.last_insert(10)
print(my_list)





            
            
        
     
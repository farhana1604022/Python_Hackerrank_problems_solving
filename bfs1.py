graph={ 'a':['b','c','e'],
        'b':['a','d','e'],
        'c':['a','f','g'],
        'd':['b'],
        'e':['a','b','d'],
        'f':['c'],
        'g':['c']
       
       }



visited = []

def dfs(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

dfs(graph,'a')
print(visited) 

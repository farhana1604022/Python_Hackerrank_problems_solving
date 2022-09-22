
graph={ 'a':['b','c','e'],
        'b':['a','d','e'],
        'c':['a','f','g'],
        'd':['b'],
        'e':['a','b','d'],
        'f':['c'],
        'g':['c']
       
       }


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'a')
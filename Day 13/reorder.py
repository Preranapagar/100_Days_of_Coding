# Reorder routes to make all paths lead to the city Zero
'''you will be given an array of connections between cities in pairs of integers. Each connection will show a one-way route from one 
city to another. for example [1,0] means that there is a one-way road from city 1 to city 0. your task is to reorder the connections such
that each city can be reached from city 0, directly or indirectly. The ouput value should return minimum number of edges changed'''

#ex. Input: n = 5, connections=[[1,0],[1,2],[3,2],[3,4]], output: 2

from collections import defaultdict

def Reorder(n,connection):
    graph = defaultdict(list)
    for u,v in connection:
        graph[u].append((v,1))
        graph[v].append((u,0))

    def dfs(node):
        nonlocal total
        visited.add(node)

        for neighbor , cost in graph[node]:
            if neighbor not in visited:
                total +=cost
                dfs(neighbor)

    total = 0
    visited = set()
    dfs(0)
    return total

def main():

    n = int(input())
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

    print(Reorder(n,connections))

if __name__=="__main__":
    main()
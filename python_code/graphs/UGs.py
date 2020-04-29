#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Amit Jain
# @Date:   2020-04-29
# @Email:  amit.hpepc@gmail.com

"""
Undirected Graph - adjacency list representation
"""
class UGraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._adj = [[] for v in range(V)]

    # v -> w
    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._E += 1

    def print_graph(self):
        print ('GRAPH ')
        for v in range (self._V):
            print ('Vertex ', v)
            for w in self._adj[v]:
                print('Edges ', w)
    
    @property
    def V(self):
        return self._V


    def reach(self, x, y):
        visited = [False for _ in range(self.V)]
        visited = self.dfs(visited, x)
        return visited[x] and visited[y]

    def dfs(self, visited, x):
        for v in self._adj[x]:
            if not visited[v]:
                visited[v] = True
                self.dfs(visited, v)
        return visited

    def number_of_components(self):
        visited = [False for _ in range(self.V)]
        count = 0
        for v in range(self.V):
            if not visited[v]:
                visited = self.dfs(visited, v)
                count += 1

        return count

if __name__ == '__main__':

    # Path from one vertext to another
    ug = UGraph(5)
    ug.add_edge(1, 2)
    ug.add_edge(3, 2)
    ug.add_edge(4, 3)
    ug.add_edge(1, 4)
    # ug.print_graph()
    print(ug.reach(1, 4))
    print(ug.reach(1, 3))
    print(ug.reach(0, 3))

    ug2 = UGraph(5  )
    ug2.add_edge(1, 2)
    ug2.add_edge(3, 2)
    print(ug2.reach(1, 4))

    # Connected components
    print('Graph 1  ', ug.number_of_components())
    print('Graph 1 ', ug2.number_of_components())



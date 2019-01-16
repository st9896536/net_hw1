#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:26:58 2017

@author: Rong
"""

import numpy as np
import math
import collections
import math
 
"""
class Graph:
	
  def __init__(self):
      self.vertices = set()
 
      # makes the default value for all vertices an empty list
      self.edges = collections.defaultdict(list)
      self.weights = {}
 
  def add_vertex(self, value):
    self.vertices.add(value)
 
  def add_edge(self, from_vertex, to_vertex, distance):
    if from_vertex == to_vertex: pass  # no cycles allowed
    self.edges[from_vertex].append(to_vertex)
    self.weights[(from_vertex, to_vertex)] = distance
 
  def __str__(self):
    string = "Vertices: " + str(self.vertices) + "\n"
    string += "Edges: " + str(self.edges) + "\n"
    string += "Weights: " + str(self.weights)
    return string
 
 
 
 
def dijkstra(graph, start):
  # initializations
  S = set()
 
  # delta represents the length shortest distance paths from start -> v, for v in delta. 
  # We initialize it so that every vertex has a path of infinity (this line will break if you run python 2)
  delta = dict.fromkeys(list(graph.vertices), math.inf)
  previous = dict.fromkeys(list(graph.vertices), None)
 
  # then we set the path length of the start vertex to 0
  delta[start] = 0
 
  # while there exists a vertex v not in S
  while S != graph.vertices:
    # let v be the closest vertex that has not been visited...it will begin at 'start'
    v = min((set(delta.keys()) - S), key=delta.get)
 
    # for each neighbor of v not in S
    for neighbor in set(graph.edges[v]) - S:
      new_path = delta[v] + graph.weights[v,neighbor]
 
      # is the new path from neighbor through 
      if new_path < delta[neighbor]:
        # since it's optimal, update the shortest path for neighbor
        delta[neighbor] = new_path
 
        # set the previous vertex of neighbor to v
        previous[neighbor] = v
    S.add(v)
		
  return (delta, previous)
 
 
 
def shortest_path(graph, start, end):	
  delta, previous = dijkstra(graph, start)
  
  path = []
  vertex = end
 
  while vertex is not None:
    path.append(vertex)
    vertex = previous[vertex]
 
  path.reverse()
  return path


G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')
 
G.add_edge('a', 'b', 2)
G.add_edge('a', 'c', 8)
G.add_edge('a', 'd', 5)
G.add_edge('b', 'c', 1)
G.add_edge('c', 'e', 3)
G.add_edge('d', 'e', 4)
 
#print(G) 
 
print(dijkstra(G, 'a'))
print(shortest_path(G, 'a', 'e'))
"""


"""
w = np.zeros((5,5)) # 一張有權重的圖：adjacency matrix
dist = np.zeros(5)  # 紀錄起點到圖上各個點的最短路徑長度
parent = np.zeros(5) # 記錄各個點在最短路徑樹上的父親是誰
visit = np.zeros(5) # 記錄各個點是不是已在最短路徑樹之中 是個boolean值

def dijkestra(source):
    for i in range(5):
        dist[i] = math.inf  # inf表無限大
        visit[i] = 0 # 初始值設0
    
    dist[source] = 0
    parent[source] = source
    
    for k in range(5):
        a,b = -1,-1
        min = math.inf
        if visit[k] !=0 and dist[k] < min :
            a = k
            min = dist[k]
        if a == -1: break; # 起點有連通的最短路徑都已找完
        visit[a] = 1 #表示已經找過了
    
        for b in range(5):
            if visit[b] !=0 and dist[a] + w[a][b] < dist[b]:
                dist[b] = dist[a] + w[a][b]
                parent[b] = a
        
def find_path(x):
    if x != parent[x]:
        find_path(parent[x])
        print('x',end='')

"""
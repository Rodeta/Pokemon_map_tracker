"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""
"""
    WIP:
    Dijkstra algorithm.
"""
from collections import deque
import sys
from edge import Edge
from node import Node
from graph import Graph

class Dijkstra:
   
    def dijkstra(self, g: Graph, start_node_name, end_node_name):
        index_start = None
        index_end = None
        for n in g.nodes:
            if n.file_name == start_node_name:
                index_start = g.nodes.index(n)
            if n.file_name == end_node_name:
                index_end = g.nodes.index(n)
        

        distance = [float("inf")] * g.graph_size()
        distance[index_start] = 0
        parent = [None]*g.graph_size()
        parent[index_start] = index_start

        pq = deque()
        pq.append(index_start)

        while pq:  
            current = min(pq, key=lambda node : distance[node])
            pq.remove(current)

            if distance[current] == sys.maxsize or current == index_end:
                break

            for idx in range(g.begin(current), g.end(current)):

                # edge relaxation
                if distance[current] + g.weight(idx) < distance[g.head(idx)]:
                    distance[g.head(idx)] = distance[current] + g.weight(idx)
                    parent[g.head(idx)] = current

                    pq.append(g.head(idx))


        # build result path from parent list
        path = deque()
        current = index_end
        while parent[current] != None and current != index_start:
            path.appendleft(current)
            current = parent[current]
        path.appendleft(current)
            
        return distance[index_end], list(path)
   
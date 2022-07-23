"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""

import glob
import string
from edge import Edge
from node import Node


class Graph:
    def __init__(self):
        self.nodes = self.load_all_nodes()
        self.edges = list()
        self.create_section_edges()

    """
        Load all nodes from the file names of pictures.
    """
    def load_all_nodes(self):
        nodes = list()
        files = []
        for file in glob.glob("pictures/*.png"):
            files.append(file)
        place_png = []
        for i in files:
            t = i.split( "\\")
            place_png.append(t[1])
        place = []
        for k in place_png:
            p = k.split(".")
            place.append(p[0])

        for node in place:
            nodes.append(Node(node))
        return nodes

    """
        Checks if an egde with these node already exists.
    """
    def check_if_edge_exists(self, node1: Node, node2: Node, weight):
        for e in self.edges:
            if (e.connection1.file_name == node1.file_name and e.connection2.file_name == node2.file_name and e.weight == weight) or (e.connection2.file_name == node1.file_name and  e.connection1.file_name == node2.file_name and e.weight == weight):
                return True
        return False

    """
        Creates an edge for two nodes.
    """
    def connect_nodes_with_same_section(self, node_name1: string, node_name2: string):
        index1 = None
        index2 = None
        for n in self.nodes:
            if n.file_name == node_name1:
                index1 = self.nodes.index(n)
            if n.file_name == node_name2:
                index2 = self.nodes.index(n)
        if index1 == None:
            raise Exception(f"Node with name: {node_name1} does not exist.")
        if index2 == None:
            raise Exception(f"Node with name: {node_name2} does not exist.")    
        if self.check_if_edge_exists(self.nodes[index1],self.nodes[index2], 0):
            raise Exception("Edge already exists")
        else:
            self.edges.append(Edge(self.nodes[index1],self.nodes[index2],0))

    """
        Creates an edge for two nodes.
    """
    def connect_nodes(self, node_name1: string, node_name2: string):
        index1 = None
        index2 = None
        for n in self.nodes:
            if n.file_name == node_name1:
                index1 = self.nodes.index(n)
            if n.file_name == node_name2:
                index2 = self.nodes.index(n)
        if index1 == None:
            raise Exception(f"Node with name: {node_name1} does not exist.")
        if index2 == None:
            raise Exception(f"Node with name: {node_name2} does not exist.")    
        if self.check_if_edge_exists(self.nodes[index1],self.nodes[index2], 1):
            raise Exception("Edge already exists")
        else:
            self.edges.append(Edge(self.nodes[index1],self.nodes[index2],1))

    """
        Creates edges from nodes which belongs to the same section.
    """
    def create_section_edges(self):
        for n in self.nodes:
            for nn in self.nodes:
                if n.file_name != nn.file_name:
                    if n.section == nn.section and not self.check_if_edge_exists(n, nn, 0):
                        self.connect_nodes_with_same_section(n.file_name,nn.file_name)

    """
        Choose node and mark as dead end.
    """
    def mark_as_dead_end(self,node_name: string):
        for n in self.nodes:
            if node_name == n.file_name:
                index = self.nodes.index(n)
                self.nodes[index].dead_end = True

    """
        Console based describtion of the graph.
    """
    def show_graph(self):
        nodes = []
        for n in self.nodes:
            nodes.append(n.file_name)
        print(nodes)
        for e in self.edges:
            print(e.show_connections())

    """
        Shows the amount of all nodes.
    """
    def graph_size(self):
        return len(self.nodes)
        
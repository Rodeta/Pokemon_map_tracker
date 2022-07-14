"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""
from edge import Edge
from node import Node
import glob
"""
    Tracks the connections between nodes
"""
class Node_Tracker:
    def __init__(self):
        self.available_nodes = list()
        self.unconnected_nodes = list()
        self.connected_nodes = list()
        self.edges = list()
    
    """
        Load all nodes from the file names of pictures
    """
    def load_all_nodes(self):
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
            self.available_nodes.append(Node(node))
        
    
    """
        WIP:
        Adds connections between two nodes
    """
    def add_connection(self, node_name1, node_name2):
        try:
            index_node1 = self.available_nodes.index(node_name1)
            index_node2 = self.available_nodes.index(node_name2)
            node1 = self.available_nodes[index_node1]
            node2 = self.available_nodes[index_node2]
            for e in self.edges:
                if e.connection1.file_name == node1.file_name and e.connection2.file_name == node2.file_name or e.connection1.file_name == node2.file_name and e.connection2.file_name == node1.file_name:
                    raise Exception("Connection already exists.")
     
            new_edge = Edge(self.available_nodes[index_node1],self.available_nodes[index_node2])
            self.edges.append(new_edge)
            self.available_nodes[index_node1].add_connection(node2)
            self.available_nodes[index_node2].add_connection(node1)


        except Exception:
            print("That item does not exist")
    
    """
        Adds a dead end mark to a node
    """
    def add_dead_end(self, node_name):
        index_node = self.available_nodes.index(node_name)
        self.available_nodes[index_node].dead_end = True

    """
        WIP:
        Findes the fastest way between two nodes
        Returns a list of nodes ( at least two nodes (Start and End node))
    """
    def find_connection(self,star_node_name,end_node_name):
        index_node1 = self.available_nodes.index(star_node_name)
        index_node2 = self.available_nodes.index(end_node_name)
        start_node = self.available_nodes[index_node1]
        end_node = self.available_nodes[index_node2]

        
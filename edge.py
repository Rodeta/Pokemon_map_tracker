"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""

from node import Node


"""
    Describes a connection between two nodes.
"""
class Edge:
    def __init__(self, node1: Node, node2:Node, weight: float):
        self.connection1 = node1
        self.connection2 = node2
        self.weight = weight
        self.summary = {"Node1": node1.file_name, "Node2": node2.file_name,"Edge weight": self.weight}
    
    """
        Shows the nodes and the weight from the edge.
    """
    def show_connections(self):
        return self.summary
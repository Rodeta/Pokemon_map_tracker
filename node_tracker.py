"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rood95/Pokemon_map_tracker
"""
from node import Node
"""
    Tracks the connections between nodes
"""
class Node_Tracker:
    def __init__(self):
        self.available_nodes = list()
        self.unconnected_nodes = list()
        self.connected_nodes = list()
    
    """
        WIP:
        Load all nodes from the file names of pictures
    """
    def load_all_nodes(self,file_path):
        self.available_nodes.append(Node(file_path))
    
    """
        Adds connections between two nodes
    """
    def add_connection(self, node_name1, node_name2):
        try:
            index_node1 = self.available_nodes.index(node_name1)
            index_node2 = self.available_nodes.index(node_name2)
            node1 = self.available_nodes[index_node1]
            node2 = self.available_nodes[index_node2]
            if(node1.check_connection(node2) == False and node2.check_connection(node1) == False):
                self.available_nodes[index_node1].add_connection(node2)
                self.available_nodes[index_node2].add_connection(node1)
                if(self.available_nodes[index_node1] in self.unconnected_nodes and self.available_nodes[index_node1] not in self.connected_nodes):
                    self.unconnected_nodes.remove(self.available_nodes[index_node1])
                    self.connected_nodes.append(self.available_nodes[index_node1])
                if(self.available_nodes[index_node2] in self.unconnected_nodes and self.available_nodes[index_node2] not in self.connected_nodes):
                    self.unconnected_nodes.remove(self.available_nodes[index_node2])
                    self.connected_nodes.append(self.available_nodes[index_node2])

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
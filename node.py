"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""

class Node:
    def __init__(self,file_name):
        self.file_name = file_name
        self.connected_list = list()
        self.section = self.file_name.split("_")[0]
        self.dead_end = False
    
    """
        Adds a new connection to the node
    """
    def add_connection(self, node):
        if(self.check_connection(node)):
            raise Exception("Node is already in the list of connected nodes.")
        else:
            self.connected_list.append({"place": node.file_name, "section": node.section})
    
    """
        Checks if a node is already in the list of connected nodes
    """
    def check_connection(self,node):
        for n in self.connected_list:
            if node.file_name in n.values() or node.section in n.values():
                return True
        return False
    
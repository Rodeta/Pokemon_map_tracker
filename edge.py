"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""

"""
    Describes a connection between two nodes
"""
class Edge:
    def __init__(self, node1, node2):
        self.connection1 = node1
        self.connection2 = node2
        if node1.section == node2.section:
            self.weight = 0
        else:
            self.weight = 1
    
    """
        Shows the nodes from the edge
    """
    def show_connections(self):
        return [self.connection1,self.connection2]
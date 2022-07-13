class Node:
    def __init__(self,file_name):
        self.file_name = file_name
        self.connected_list = list()
        self.dead_end = False
    
    """
        Adds a new connection to the node
    """
    def add_connection(self, node):
        if(self.check_connection(node)):
            raise Exception("Node is already in the list of connected nodes.")
        else:
            self.connected_list.append(node)
    
    """
        Checks if a node is already in the list of connected nodes
    """
    def check_connection(self,node):
        return node in self.connected_list
    
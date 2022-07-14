"""
    @Author: Rodeta | Rodion Kraft
    @Credit: 
    @Links: https://github.com/Rodeta/Pokemon_map_tracker
"""
"""
    WIP:
    Dijkstra algorithm
"""
class Dijkstra:
    def __init__(self,node_list, edge_list):
        self.nodes = node_list
        self.edges = edge_list
        self.distances = list()
        for n in self.nodes:
            for nn in self.nodes:
                if nn.file_name != n.file_name:
                    self.distances.append(self.calculate_distance(n,nn))

    """
        Calculate the distance between nodes
    """    
    def calculate_distance(self,start_node_name, end_node_name):
        start_index = self.nodes.index(start_node_name)
        end_index = self.nodes.index(end_node_name)
        

        if self.nodes[start_index].section == self.nodes[end_index].section:
            return {"Node-name1": self.nodes[start_index].file_name, "Node-name2": self.nodes[end_index].file_name, "distance": 0 }

        else:
            for n in self.nodes[start_index].connected_list:
                if self.nodes[end_index].file_name in n.values():
                    return {"Node-name1": self.nodes[start_index].file_name, "Node-name2": self.nodes[end_index].file_name, "distance": 1 }
                 
            return {"Node-name1": self.nodes[start_index].file_name, "Node-name2": self.nodes[end_index].file_name, "distance": float("inf") }
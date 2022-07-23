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
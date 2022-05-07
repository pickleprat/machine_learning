from pyparsing import null_debug_action
import statistics as st 


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self, value):
        self.root = Node(value)
        
    
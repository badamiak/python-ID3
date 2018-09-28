class Node(object):
    def __init__(self, name:str):
        self.child_nodes = list()
        self.name = name

    def append(self, child_node):
        self.child_nodes.append(child_node)
    
    def draw(self, depth:int = 0):
        # tree = self.name
        # for child in self.child_nodes:
        #     tree+='\n{}.{}'.format(self.name,child.draw)
        # return tree
        tree = '{}{}'.format(('|'*depth) + '+->', self.name)
        for child in self.child_nodes:
            tree += '\n{}'.format(child.draw(depth+1))
        return tree
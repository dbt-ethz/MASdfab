class Face:
    def __init__(self,nodes):
        self.nodes = nodes
        self.color=color(255)
        
    def display(self):
        beginShape()
        for node in self.nodes:
            vertex(node.x,node.y,node.z)
        endShape(CLOSE)

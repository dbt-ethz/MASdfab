class Face:
    def __init__(self,nodes):
        self.nodes = nodes
        self.color=color(255)
        
    def display(self):
        beginShape()
        for node in self.nodes:
            vertex(node.x,node.y,node.z)
        endShape(CLOSE)
    
    def getNormal(self):
        # returns the normal of a face
        v = PVector.sub(self.nodes[1], self.nodes[0])
        u = PVector.sub(self.nodes[2], self.nodes[0])
        return v.cross(u).normalize()
    
    def getCenter(self):
        # return the average of all boundarypoints
        center=PVector()
        for p in self.nodes:
            center.add(p)
        center.div(len(self.nodes))
        return center
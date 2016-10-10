class Mesh:
    def __init__(self):
        self.nodes = []
        self.faces = []
        
    def addFace(self, indices):
        f = Face([ self.nodes[i] for i in indices ])
        
        # above line is short for:
        # nodes = []
        # for i in indices:
        #     n = self.nodes[i]
        #     nodes.append(n)
        # f = Face(nodes)
        
        self.faces.append(f)
        
    def applyTransform(self, mtx):
        for n in self.nodes:
            mtx.mult(n,n)

class Face:
    def __init__(self,nodes):
        self.nodes = nodes
        self.color=color(255)
    
    def display(self):
        n=len(self.nodes)
        if (n==3):
            beginShape(TRIANGLES)
        elif (n==4):
            beginShape(QUADS)
        else:
            beginShape()
        for p in self.nodes:
            vertex(p.x,p.y,p.z)
        if (n>4):
            endShape(CLOSE)
        else:
            endShape()
            
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
    
    def getPerimeter(self):
        perimeter=0
        for i in range(len(self.nodes)):
            n1=self.nodes[i]
            n2=self.nodes[(i+1)%len(self.nodes)]
            perimeter=perimeter+n1.dist(n2)
        return perimeter
    
    def getMaxDistToCenter(self):
        center=self.getCenter()
        maxDist=0
        for n in self.nodes:
            if n.dist(center)>maxDist:
                maxDist=n.dist(center)
        return maxDist
        
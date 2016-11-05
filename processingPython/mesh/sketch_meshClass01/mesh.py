class Mesh:
    def __init__(self,_nodes=[],_faces=[]):
        self.nodes = _nodes
        self.faces = _faces
        
    def addFace(self, indices):
        f = Face([ self.nodes[i] for i in indices ])
        self.faces.append(f)
        
    def addNode(self,x,y,z):
        self.nodes.append(PVector(x,y,z))
        
    def createBox(self,dimX,dimY,dimZ):
        dX=dimX/2
        dY=dimY/2
        dZ=dimZ/2
        self.nodes = []
        self.faces = []
        self.addNode(-dX,-dY,-dZ)
        self.addNode(+dX,-dY,-dZ)
        self.addNode(+dX,+dY,-dZ)
        self.addNode(-dX,+dY,-dZ)
        self.addNode(-dX,-dY,+dZ)
        self.addNode(+dX,-dY,+dZ)
        self.addNode(+dX,+dY,+dZ)
        self.addNode(-dX,+dY,+dZ)
        
        self.addFace([0,3,7,4])
        self.addFace([1,5,6,2])
        self.addFace([0,1,5,4])
        self.addFace([2,6,7,3])
        self.addFace([0,1,2,3])
        self.addFace([7,6,5,4])
    
class Face:
    def __init__(self,_nodes,_color=color(255)):
        self.nodes = _nodes
        self.color=_color
    
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
        
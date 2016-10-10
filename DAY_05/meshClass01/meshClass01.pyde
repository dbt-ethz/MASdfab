add_library('peasycam')
from mesh import Face
from mesh import Mesh

def setup():
    size(800,450,P3D)
    noStroke()
    fill(255,100)
    cam= PeasyCam(this,400)
    
    global mymesh
    
    mymesh = createCube(100)
    
    stonehenge = []
    for i in range(10):
        m = createCube(100 + i*10)
        stonehenge.append(m)
    
    '''
    mymesh = Mesh()
    s = 100
    mymesh.nodes.append(PVector(-s,-s,-s))
    mymesh.nodes.append(PVector(+s,-s,-s))
    mymesh.nodes.append(PVector(+s,+s,-s))
    mymesh.nodes.append(PVector(-s,+s,-s))
    
    mymesh.nodes.append(PVector(-s,-s,+s))
    mymesh.nodes.append(PVector(+s,-s,+s))
    mymesh.nodes.append(PVector(+s,+s,+s))
    mymesh.nodes.append(PVector(-s,+s,+s))
    
    mymesh.addFace([0,3,7,4])
    mymesh.addFace([1,5,6,2])
    mymesh.addFace([0,1,5,4])
    mymesh.addFace([2,6,7,3])
    mymesh.addFace([0,1,2,3])
    mymesh.addFace([7,6,5,4])
    '''
    
def draw():
    background(0)
    lights()
    
    '''
    for i,n in enumerate(mymesh.nodes):
        pushMatrix()
        translate(n.x,n.y,n.z)
        sphere(10)
        text(str(i),20,0)
        popMatrix()
    '''
      
    for m in stonehenge:
        for f in m.faces:
            f.display()
        
def createCube(s):
    cube = Mesh()
    cube.nodes.append(PVector(-s,-s,-s))
    cube.nodes.append(PVector(+s,-s,-s))
    cube.nodes.append(PVector(+s,+s,-s))
    cube.nodes.append(PVector(-s,+s,-s))
    
    cube.nodes.append(PVector(-s,-s,+s))
    cube.nodes.append(PVector(+s,-s,+s))
    cube.nodes.append(PVector(+s,+s,+s))
    cube.nodes.append(PVector(-s,+s,+s))
    
    cube.addFace([0,3,7,4])
    cube.addFace([1,5,6,2])
    cube.addFace([0,1,5,4])
    cube.addFace([2,6,7,3])
    cube.addFace([0,1,2,3])
    cube.addFace([7,6,5,4])
    
    return cube
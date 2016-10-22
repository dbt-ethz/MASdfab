add_library('peasycam')
from mesh import Face

def setup():
    size(800,450,P3D)
    #noStroke()
    cam= PeasyCam(this,400)
    
    global faces, fltRad, fltLayerHeight
    fltRad = 100
    fltLayerHeight = 50
    faces = []
    lstLayerLists = []
    
    intNumSides = 7
    intNumLayers = 4
    
    # generation of all the nodes
    for i in range(intNumLayers):
        lstNdsLayer = []
        for j in range(intNumSides):
            a = j * TWO_PI/intNumSides
            x = (fltRad + i*20) * cos(a)
            y = (fltRad + i*20) * sin(a)
            z = i * fltLayerHeight
            n = PVector(x,y,z)
            lstNdsLayer.append(n)
        lstLayerLists.append(lstNdsLayer)
        
    # connecting the nodes into faces
    for i in range(intNumLayers - 1):
        l1 = lstLayerLists[i]
        l2 = lstLayerLists[i+1]
        for j in range(intNumSides):
            n1 = l1[j]
            n2 = l1[(j+1) % len(l1)]
            n3 = l2[j]
            n4 = l2[(j+1) % len(l2)]
            faces.append(Face([n1,n2,n4,n3]))
            
  
    # add bottom face
    bottomFace = Face(lstLayerLists[0])
    bottomFace.nodes.reverse()
    faces.append(bottomFace)
    
    # add top face
    faces.append(Face(lstLayerLists[-1]))
        
def draw():
    background(100)
    lights()

    for face in faces:
        fill(face.color, 120)
        face.display()
        
def splitFace(face):
    newFaces=[]
    center=face.getCenter()
    normal=face.getNormal()
    normal.mult(20)
    center.add(normal)
    for i in range(len(face.nodes)):
        n1=face.nodes[i]
        n2=face.nodes[(i+1)%len(face.nodes)]
        newFaces.append(Face([center,n1,n2]))
    return newFaces

def keyPressed():
    global faces
    if key=='r':
        newFaces=[]
        for face in faces:
            newFaces.extend(splitFace(face))
        faces=newFaces
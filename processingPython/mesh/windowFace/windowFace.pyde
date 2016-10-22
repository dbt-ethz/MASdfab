add_library('peasycam')
from mesh import Face
from obj import OBJExporter
from obj import importOBJ
import utils

def setup():
    size(800,450,P3D)
    cam= PeasyCam(this,400)
    
    global faces,generation
    generation=0
    #faces = importOBJ("test3.obj")
    faces=[]
    n1=PVector(-100,-100,0)
    n2=PVector(-100,100,0)
    n3=PVector(100,100,100)
    n4=PVector(100,-100,0)
    faces.append(Face([n4,n3,n2,n1]))

def draw():
    background(100)
    lights()
    #noStroke()
    for face in faces:
        normal=face.getNormal()
        face.color=color(normal.x*255+100,normal.y*255+100,normal.z*255+100)
        fill(face.color)
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

def windowFace(face):
    newFaces=[]
    center = face.getCenter()
    normal = face.getNormal()
    normal.mult(20)
    lstWinNodes = []
    for i in range(len(face.nodes)):
        n1=face.nodes[i]
        ray1 = PVector.sub(center,n1)
        ray1.mult(0.5)
        winNode = PVector.add(n1,ray1)
        winNode.add(normal)
        lstWinNodes.append(winNode)
    # create frame faces
    for i in range(len(face.nodes)):
        n1=face.nodes[i]
        n2=face.nodes[(i+1)%len(face.nodes)]
        n3 = lstWinNodes[i]
        n4 = lstWinNodes[(i+1)%len(face.nodes)]
        newFaces.append(Face([n1,n2,n4,n3]))
    newFaces.append(Face(lstWinNodes))
    
    return newFaces

def keyPressed():
    global faces,generation
    if key=='r':
        generation=generation+1
        println("generation: "+str(generation))
        newFaces=[]
        for face in faces:
            newFaces.extend(splitFace(face))
        faces=newFaces
    if key=='w':
        generation=generation+1
        println("generation: "+str(generation))
        newFaces=[]
        for face in faces:
            newFaces.extend(windowFace(face))
        faces=newFaces
        
    if key=='a':
        newFaces=[]
        for i,face in enumerate(faces):
            if i%2==0:
                newFaces.extend(splitFace(face))
            else:
                newFaces.extend(windowFace(face))
        faces=newFaces
    elif key=='e':
        myObjExporter=OBJExporter(sketchPath(""),utils.timeStamp()+".obj")
        myObjExporter.exportFacesWithColors(faces)
        
    
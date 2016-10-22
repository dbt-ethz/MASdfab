add_library('peasycam')
from mesh import Face
from obj import OBJExporter
import obj

def setup():
    size(800,450,P3D)
    global faces,generation
    generation=0
    faces=[]
    n1=PVector(-100,-100,0)
    n2=PVector(-100,100,0)
    n3=PVector(100,100,100)
    n4=PVector(100,-100,0)
    faces.append(Face([n4,n3,n2,n1]))
    faces=obj.importOBJ(sketchPath("")+"test3.obj")
    cam= PeasyCam(this,400)

def draw():
    background(100)
    lights()
    noStroke()
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

def keyPressed():
    global faces,generation
    if key=='r':
        generation=generation+1
        println("generation: "+str(generation))
        newFaces=[]
        for face in faces:
            newFaces.extend(splitFace(face))
        faces=newFaces
    elif key=='e':
        myObjExporter=OBJExporter(sketchPath(""),obj.timeStamp()+".obj")
        myObjExporter.exportFacesWithColors(faces)
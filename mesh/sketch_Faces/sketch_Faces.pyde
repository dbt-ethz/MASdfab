add_library('peasycam') #import library
from face import Face

def setup():
    size(800,450,P3D)
    cam=PeasyCam(this,300)
    nodes=[]#declare variable called nodes and define it as list
    nodes.append(PVector(-100,-100,0))
    nodes.append(PVector(100,-100,0))
    nodes.append(PVector(100,100,0))
    nodes.append(PVector(-100,100,0))
    nodes.append(PVector(-100,-100,100))
    nodes.append(PVector(100,-100,100))
    nodes.append(PVector(100,100,100))
    nodes.append(PVector(-100,100,100))
    global faces
    faces=[]
    faces.append(Face([nodes[3],nodes[2],nodes[1],nodes[0]]))
    faces.append(Face([nodes[4],nodes[5],nodes[6],nodes[7]]))
    faces.append(Face([nodes[0],nodes[1],nodes[5],nodes[4]]))
    faces.append(Face([nodes[1],nodes[2],nodes[6],nodes[5]]))
    faces.append(Face([nodes[2],nodes[3],nodes[7],nodes[6]]))
    faces.append(Face([nodes[3],nodes[0],nodes[4],nodes[7]]))

def draw():
    background(0) # draw a black background
    for face in faces:
        face.display()

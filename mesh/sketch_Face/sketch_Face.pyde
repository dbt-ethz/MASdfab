add_library('peasycam') #import library
from face import Face

def setup():
    size(800,450,P3D)
    cam=PeasyCam(this,300)
    global myFace #declare a variable called face with a global scope
    nodes=[]#declare variable called nodes and define it as list
    nodes.append(PVector(-100,-100,0))
    nodes.append(PVector(100,-100,0))
    nodes.append(PVector(100,100,0))
    nodes.append(PVector(-100,100,0))
    myFace=Face(nodes)# instantiate class Face and save it under myFace
    myFace.color=color(0,255,0)# set the color of the face
    
def draw():
    background(0)
    fill(myFace.color)
    beginShape()
    for p in myFace.nodes:
        vertex(p.x,p.y,p.z)
    endShape(CLOSE)
  
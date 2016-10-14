add_library('peasycam') #import library
from face import Face

def setup():
    size(800,450,P3D)
    cam=PeasyCam(this,300)
    global myFace,yourFace #declare a variable called myFace with a global scope
    nodes=[]#declare variable called nodes and define it as list
    nodes.append(PVector(-100,-100,0))
    nodes.append(PVector(100,-100,0))
    nodes.append(PVector(100,100,0))
    nodes.append(PVector(-100,100,0))
    myFace=Face(nodes)# instantiate class Face and save it under myFace
    myFace.color=color(0,255,0)# set the color of the face
    nodes=[]#declare variable called nodes and define it as list
    nodes.append(PVector(-100,-100,100))
    nodes.append(PVector(100,-100,100))
    nodes.append(PVector(100,100,100))
    nodes.append(PVector(-100,100,100))
    yourFace=Face(nodes)# instantiate class Face and save it under myFace
    yourFace.color=color(0,0,255)# set the color of the face
    
def draw():
    background(0) # draw a black background
    fill(myFace.color) 
    beginShape()
    for myNode in myFace.nodes:
        vertex(myNode.x,myNode.y,myNode.z)
    endShape(CLOSE)
    
  
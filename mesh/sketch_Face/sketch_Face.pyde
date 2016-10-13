add_library('peasycam') #import library
from Face import Face

def setup():
    size(800,450,P3D)
    cam=PeasyCam(this,300)
    global face
    record=False
    nodes=[]
    nodes.append(PVector(-100,-100,0))
    nodes.append(PVector(100,-100,0))
    nodes.append(PVector(100,100,0))
    nodes.append(PVector(-100,100,0))
    face=Face(nodes)
    face.color=color(0,255,0)
    
def draw():
    background(0)
    fill(face.color)
    beginShape()
    for p in face.nodes:
        vertex(p.x,p.y,p.z)
    endShape(CLOSE)
  
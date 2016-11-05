add_library('peasycam')
from mesh import Face
from mesh import Mesh

def setup():
    global stonehenge
    size(800,450,P3D)
    noStroke()
    fill(255,100)
    cam= PeasyCam(this,400)
    stonehenge = []
    for i in range(10):
        m=Mesh()
        m.createBox(100 + i*10,100 + i*10,100 + i*10)
        stonehenge.append(m)

def draw():
    background(0)
    lights()
    for m in stonehenge:
        for f in m.faces:
            f.display()
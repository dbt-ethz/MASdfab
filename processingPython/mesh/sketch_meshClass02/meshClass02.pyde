add_library('peasycam')
from mesh import Face
from mesh import Mesh
from obj import OBJExporter

def setup():
    size(800,450,P3D)
    noStroke()
    fill(255,100)
    cam= PeasyCam(this,400)

    global stonehenge

    stonehenge = []
    for i in range(10):
        m = createCube(100 + i*10)

        mtx = PMatrix3D()
        mtx.rotate(i*TWO_PI/10,0,0,1)
        mtx.translate(500,0,0)
        #mtx.shearX(i/3.0)

        m.applyTransform(mtx)

        stonehenge.append(m)

def draw():
    background(0)
    lights()

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

    cube.addFace([0,4,7,3])
    cube.addFace([1,2,6,5])
    cube.addFace([0,1,5,4])
    cube.addFace([2,3,7,6])
    cube.addFace([0,3,2,1])
    cube.addFace([7,4,5,6])

    return cube

def keyPressed():
    if key=='e':
        faces = []
        for m in stonehenge:
            faces.extend(m.faces)

        myObjExporter = OBJExporter(sketchPath(""),"mesh.obj")
        myObjExporter.exportFacesWithColors(faces)

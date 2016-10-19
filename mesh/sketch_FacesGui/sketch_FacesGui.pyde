add_library('controlP5')
add_library('peasycam') #import library

from face import Face

def setup():
    size(800,450,P3D)
    global cp5, cam, sliderDimX, sliderDimY,sliderDimZ
    cam=PeasyCam(this,1000)
    cp5 = ControlP5(this)
    cp5.setAutoDraw(False)
    sliderDimX = cp5.addSlider("dim x").setPosition(10,10).setRange(100,500)
    sliderDimY = cp5.addSlider("dim y").setPosition(10,30).setRange(100,500)
    sliderDimZ = cp5.addSlider("dim z").setPosition(10,50).setRange(100,500)

def draw():
    faces=createHouse(sliderDimX.getValue(),sliderDimY.getValue(),sliderDimZ.getValue())
    if mouseX<150:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(0) # draw a black background
    lights()
    for face in faces:
        fill(face.color)
        face.display()
    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()

def createHouse(dimX,dimY,dimZ):
    nodes=[]#declare variable called nodes and define it as list
    nodes.append(PVector(-dimX,-dimY,0))
    nodes.append(PVector(dimX,-dimY,0))
    nodes.append(PVector(dimX,dimY,0))
    nodes.append(PVector(-dimX,dimY,0))
    nodes.append(PVector(-dimX,-dimY,dimZ))
    nodes.append(PVector(dimX,-dimY,dimZ))
    nodes.append(PVector(dimX,dimY,dimZ))
    nodes.append(PVector(-dimX,dimY,dimZ))
    nodes.append(PVector(0,-dimY,dimZ+dimX/2))
    nodes.append(PVector(0,dimY,dimZ+dimX/2))

    faces=[]
    faces.append(Face([nodes[3],nodes[2],nodes[1],nodes[0]]))
    faces.append(Face([nodes[0],nodes[1],nodes[5],nodes[8],nodes[4]]))
    faces.append(Face([nodes[1],nodes[2],nodes[6],nodes[5]]))
    faces.append(Face([nodes[2],nodes[3],nodes[7],nodes[9],nodes[6]]))
    faces.append(Face([nodes[3],nodes[0],nodes[4],nodes[7]]))
    faces.append(Face([nodes[5],nodes[6],nodes[9],nodes[8]]))
    faces.append(Face([nodes[7],nodes[4],nodes[8],nodes[9]]))
    faces[5].color=color(255,0,0)
    faces[6].color=color(255,0,0)
    return faces

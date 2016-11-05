add_library('controlP5')
add_library('peasycam') #import library

from face import Face
from obj import importOBJ

def setup():
    size(1000,600,P3D)
    global cp5, cam, sliderExtrude,sliderIterate, sliderDimX, sliderDimY, sliderDimZ
    cam=PeasyCam(this,500)
    cp5 = ControlP5(this)
    cp5.setAutoDraw(False)
    sliderExtrude = cp5.addSlider("extrude").setPosition(10,10).setRange(0,200)
    sliderIterate=cp5.addSlider("iterate").setPosition(10,30).setRange(1,6).setNumberOfTickMarks(6)
    
    #sliderDimX = cp5.addSlider("dim x").setPosition(10,60).setRange(100,500)
    #sliderDimY = cp5.addSlider("dim y").setPosition(10,80).setRange(100,500)
    #sliderDimZ = cp5.addSlider("dim z").setPosition(10,100).setRange(100,500)
    restart()
    
def draw():
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

def subdivide(faces):
    newFaces=[]
    for face in faces:
        center =face.getCenter()
        extrusion =center.z*0.01*sliderExtrude.getValue()
        newFaces.extend(subdivideFace(face,extrusion))
#newFaces.extend(subdivideFace(face,sliderExtrude.getValue()))        
    return newFaces

def subdivideFace(face,extrude):
    newFaces=[]
    center=face.getCenter()
    normal=face.getNormal()
    normal.mult(extrude)
    center.add(normal)
    for i in xrange(len(face.nodes)):
        n1=face.nodes[i]
        n2=face.nodes[(i+1)%len(face.nodes)]
        lastFace=Face([n1,n2,center])
        newFaces.append(lastFace)
        if i%3==0:
            lastFace.color=color(255,0,0)
        if i%3==1:
            lastFace.color=color(0,255,255)
    return newFaces


def restart():
    global faces 
    faces = importOBJ("manta3.obj")      

def keyPressed():
    global faces
    if key=='s':
        faces = subdivide(faces)
    if key=='r':
        restart()
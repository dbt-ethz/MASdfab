add_library('controlP5')
add_library('peasycam') #import library

from face import Face

def setup():
    size(800,450,P3D)
    global cp5, cam, sliderExtrude, sliderIterate
    cam=PeasyCam(this,1000)
    cp5 = ControlP5(this)
    cp5.setAutoDraw(False)
    sliderExtrude = cp5.addSlider("extrude").setPosition(10,10).setRange(0,200)
    sliderIterate=cp5.addSlider("iterations").setPosition(10,30).setRange(1,6).setNumberOfTickMarks(6)
def draw():
    # initialise the geometry
    faces=[Face([PVector(-100,-100),PVector(+100,-100),PVector(+100,+100),PVector(-100,+100)])]
    # subdivide all faces 5 times
    for i in xrange(sliderIterate.getValue()):
        faces=subdivide(faces)

    # drawing
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
        newFaces.extend(subdivideFace(face,sliderExtrude.getValue()))
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
        if i%3==0:
            lastFace.color=color(255,0,0)
        if i%3==1:
            lastFace.color=color(0,255,255)
        newFaces.append(lastFace)
    return newFaces
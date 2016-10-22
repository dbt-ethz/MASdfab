add_library('peasycam')
add_library('controlP5')

from myclasses import Face

def setup():
    size(800,450,P3D)
    noStroke()
    global cam, cp5,lstNodes, lstFaces
    cam=PeasyCam(this,100)
    cp5 = ControlP5(this)
    sldXY = cp5.addSlider("my slider")
    cp5.setAutoDraw(False)
    
    lstNodes = [PVector(random(-50,50),random(-50,50),random(-50,50)) for _ in range(20)]
    
    lstFaces = []
    for i in range(18):
        nds = lstNodes[i:i+3]
        face = Face(nds)
        lstFaces.append(face)

def draw():
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(0)
    lights()
    
    #box(50)
    fill(255)
    for i,p in enumerate(lstNodes):
        pushMatrix()
        translate(p.x,p.y,p.z)
        box(2)
        popMatrix()
        p.add(PVector.random3D())
    
    for f in lstFaces:
        fill(f.facecolor)
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape()

    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
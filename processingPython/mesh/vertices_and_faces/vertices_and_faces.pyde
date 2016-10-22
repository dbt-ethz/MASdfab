add_library('peasycam')
add_library('controlP5')

from myclasses import Face

def setup():
    size(800,450,P3D)
    global cam, cp5
    cam=PeasyCam(this,100)
    cp5 = ControlP5(this)
    sldXY = cp5.addSlider("my slider")
    cp5.setAutoDraw(False)
    
    global lstVertices, lstFaces
    lstVertices = []
    for i in range(20):
        v = PVector(random(-100,100),random(-100,100),random(-100,100))
        lstVertices.append(v)
        
    lstFaces = []
    nodes = [lstVertices[0], lstVertices[1], lstVertices[2]]
    face = Face(nodes)
    lstFaces.append(face)

def draw():
    if mouseX<150:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(0)
    lights()
    
    fill(255)
    for v in lstVertices:
        pushMatrix()
        translate(v.x,v.y,v.z)
        box(8)
        popMatrix()
        
    for f in lstFaces:
        fill(f.facecolor)
        beginShape()
        for n in f.nodes:
            vertex(n.x, n.y, n.z)
        endShape()

    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
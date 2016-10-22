add_library('peasycam')
add_library('controlP5')

def setup():
    size(800,450,P3D)
    global cam, cp5
    cam=PeasyCam(this,100)
    cp5 = ControlP5(this)
    sldXY = cp5.addSlider("my slider")
    cp5.setAutoDraw(False)

def draw():
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(0)
    lights()
    
    box(50)

    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
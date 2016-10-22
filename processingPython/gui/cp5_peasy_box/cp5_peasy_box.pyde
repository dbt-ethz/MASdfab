add_library('peasycam')
add_library('controlP5')

def setup():
    size(800,450, P3D)
    rectMode(CENTER)
    
    global cp5, sldXDim, sldYDim, sldZDim, cam
    cp5 = ControlP5(this)
    cp5.setAutoDraw(False)
    cam = PeasyCam(this,600)
    
    sldXDim = cp5.addSlider("width").setPosition(10,10).setRange(50,500)
    
    sldYDim = cp5.addSlider("height")
    sldYDim.setPosition(10,40)
    sldYDim.setRange(50,500)
    
    sldZDim = cp5.addSlider("depth")
    sldZDim.setPosition(10,70)
    sldZDim.setRange(50,500)
    
def draw():
    if mouseX<150:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(100)
    #rect(0,0,sldXDim.getValue(),sldYDim.getValue())
    box(sldXDim.getValue(),sldYDim.getValue(),sldZDim.getValue())
    #box(sldXDim.getValue())
    
    cam.beginHUD()
    cp5.draw()
    cam.endHUD()
add_library('controlP5')

def setup():
    size(800,450)
    rectMode(CENTER)
    
    global cp5, sldXDim, sldYDim
    cp5 = ControlP5(this)
    
    sldXDim = cp5.addSlider("width").setPosition(10,10).setRange(50,width)
    
    sldYDim = cp5.addSlider("height")
    sldYDim.setPosition(10,40)
    sldYDim.setRange(50,height)
    
def draw():
    background(0)
    rect(width/2, height/2,sldXDim.getValue(),sldYDim.getValue())
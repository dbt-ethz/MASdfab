add_library('controlP5')

# this program demonstrates how to use a Slider with ControlP%
def setup():
    global sliderDimX
    size(800,450)
    cp5=ControlP5(this)
    sliderDimX=cp5.addSlider("dimX").setPosition(20,20).setRange(50,500)
    
def draw():
    background(0)
    rectMode(CENTER)
    rect(width/2,height/2,sliderDimX.getValue(),300)
    
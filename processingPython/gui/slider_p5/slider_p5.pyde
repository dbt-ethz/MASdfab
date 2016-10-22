add_library('controlP5')

def setup():
    size(800,450)
    global hSlider,wSlider
    cp5 = ControlP5(this)
    wSlider = cp5.addSlider('width')
    wSlider.setPosition(20,20)
    hSlider = cp5.addSlider('height')
    hSlider.setPosition(20,60)

def draw():
    background(0)
    rect(250,50,wSlider.getValue(),hSlider.getValue())
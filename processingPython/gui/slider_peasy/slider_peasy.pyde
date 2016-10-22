add_library('peasycam')
add_library('controlP5')

# this program demonstrates how to combine ControlP5 and PeasyCam
def setup():
    global cam,cp5,sliderDimX
    size(800,450,P3D)
    cam=PeasyCam(this,400)
    cp5=ControlP5(this)
    sliderDimX=cp5.addSlider("dimX").setPosition(20,20).setRange(50,500)
    cp5.setAutoDraw(False)
    
def draw():
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)
    # drawing content in 3D
    hint(ENABLE_DEPTH_TEST)
    lights()
    background(0)
    box(sliderDimX.getValue(),200,100)
    # drawing GUI in 2D
    hint(DISABLE_DEPTH_TEST)
    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
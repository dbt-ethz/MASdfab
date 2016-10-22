add_library('peasycam')
add_library('controlP5')

fltSize = 10

def setup():
    size(800,450,P3D)
    noStroke()
    global cam, cp5, sldX, sldY, sldPX, sldPY
    cam=PeasyCam(this,100)
    cp5 = ControlP5(this)
    sldX = cp5.addSlider("div x").setRange(1.0,10.0).setValue(3.0).setPosition(10,10)
    sldPX = cp5.addSlider("phase x").setRange(-HALF_PI,HALF_PI).setPosition(10,40)
    sldY = cp5.addSlider("div y").setRange(1.0,10.0).setValue(3.0).setPosition(10,70)
    sldPY = cp5.addSlider("phase y").setRange(-HALF_PI,HALF_PI).setPosition(10,100)
    cp5.setAutoDraw(False)

def draw():
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(0)
    #lights()
    directionalLight(255,200,200,1,0,-0.5)
    directionalLight(200,200,255,-1,0,-0.5)
    translate(-7.5*fltSize,-4*fltSize)
    for i in range(16):
        for j in range(9):
            pushMatrix()
            translate(i*fltSize,j*fltSize)
            rotateY(sin(sldPX.getValue()+i/sldX.getValue())*cos(sldPY.getValue()+j/sldY.getValue()))
            box(fltSize*0.9)
            popMatrix()
            
    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
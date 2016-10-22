add_library('peasycam')
add_library('controlP5')

fltSizeX = 13.0
fltSizeY = 7
fltSizeZ = 5

def setup():
    size(800,450, P3D)
    #noStroke()
    
    global cp5, cam, sldXRot, sldYRot
    cp5 = ControlP5(this)
    cp5.setAutoDraw(False)
    cam = PeasyCam(this,100)
    
    sldXRot = cp5.addSlider("rot x").setPosition(10,10).setRange(1,10)
    sldYRot = cp5.addSlider("rot y").setPosition(10,30).setRange(1,10)

def draw():
    if mouseX<150:
        cam.setActive(False)
    else:
        cam.setActive(True)
    background(100)
    #lights()
    directionalLight(255,200,200, 1,0,-0.5)
    directionalLight(200,200,255, -1,0,-0.5)
    
    translate(-7.5 * fltSizeX, -4 * fltSizeY, 0)
    for i in range(16):
        for j in range(9):
            if j%2 == 0:
                k = fltSizeX * 0.5
            else:
                k = 0
            pushMatrix()
            val = sin(i/sldXRot.getValue()) * cos(j/sldYRot.getValue())
            translate(k+i*fltSizeX,j*fltSizeY,0)
            rotateY(val)
            box(fltSizeX,fltSizeY,fltSizeZ)
            popMatrix()
    
    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()
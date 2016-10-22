def setup():
    size(800,450)
    noStroke()
    fill(255)
    rectMode(CENTER)
    global fltPosX, fltPosY, fltSpdX, fltSpdY, fltRad
    fltPosX = 400
    fltPosY = 225
    fltSpdX = random(-10,10)
    fltSpdY = random(-10,10)
    fltRad = 15
    background(0)

def draw():
    # drawing
    global fltPosX, fltPosY, fltSpdX, fltSpdY,fltRad
    background(0)
    ellipse(fltPosX,fltPosY,2*fltRad,2*fltRad)

    # calculation
    # fltRad = mouseX*100./width+5
    fltPosX = fltPosX + fltSpdX
    fltPosY = fltPosY + fltSpdY
    if fltPosX>width-fltRad or fltPosX<fltRad:
        fltSpdX = fltSpdX*-1
    if fltPosY>height-fltRad or fltPosY<fltRad:
        fltSpdY = fltSpdY*-1

def setup():
    size(800,450)
    background(255)
    strokeWeight(0.5)
    
    global pic
    pic = loadImage('turing2.jpg')
    global fltPosX,fltPosY
    fltPosX = width/2
    fltPosY = height/2
    
def draw():
    global fltPosX,fltPosY
    fltBright = brightness(pic.get(int(fltPosX),int(fltPosY)))
    fltBright = (fltBright/255.0)
    fltBright = 10 + fltBright*100
    fltAng = random(TWO_PI)
    dx = fltBright * cos(fltAng)
    dy = fltBright * sin(fltAng)
    line(fltPosX,fltPosY,fltPosX+dx,fltPosY+dy)
    fltPosX = constrain(fltPosX+dx,10,width-10)
    fltPosY = constrain(fltPosY+dy,10,height-10)
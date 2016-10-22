fltPosX, fltPosY = 0,0
fltPad1,fltPad2 = 0,0
intScore1, intScore2 = 0,0
blnP1up, blnP1dwn, blnP2up, blnP2dwn = 0, 0, 0, 0
speed = 3

def setup():
    size(800,450)
    rectMode(CENTER)
    noStroke()
    
def draw():
    background(0)
    translate(width/2,height/2)
    
    ellipse(fltPosX,fltPosY,20,20)
    
    global fltPad1, fltPad2
    fltPad1 = fltPad1 + (blnP1up - blnP1dwn)*3
    fltPad2 = fltPad2 + (blnP2up - blnP2dwn)*3
    
    rect(-width/2+20,fltPad1,20,80)
    rect(width/2-20,fltPad2,20,80)
                
def keyPressed():
    setMove(key, 1)
    
def keyReleased():
    setMove(key, 0)
    
def setMove(k, b):
    global blnP1up, blnP1dwn, blnP2up, blnP2dwn
    if k=='q':
        blnP1up = b
        return b
    if k=='a':
        blnP1dwn = b
        return b
    if k=='o':
        blnP2up = b
        return b
    if k=='l':
        blnP2dwn = b
        return b
    return b
def setup():
    size(800,450)
    noStroke()
    fill(255)
    rectMode(CENTER)
    global vecPos, vecSpd, fltRad
    vecPos = PVector(width/2,height/2)
    vecSpd = PVector(random(-10,10),random(-10,10))
    fltRad = 15
    background(0)

def draw():
    # drawing
    global vecPos, vecSpd, fltRad
    background(0)
    ellipse(vecPos.x, vecPos.y, 2*fltRad,2*fltRad)
    
    rect(20,mouseY,20,80)
    
    # calculation
    vecPos = vecPos + vecSpd
    
    if vecPos.x>width-fltRad:
        vecSpd.x = vecSpd.x * -1
    if vecPos.y>height-fltRad or vecPos.y<fltRad:
        vecSpd.y = vecSpd.y * -1
        
    # check if ball hits paddle
    if vecPos.x < 30+fltRad and abs(vecPos.y-mouseY)<40:
        vecSpd.x = vecSpd.x * -1
    if vecPos.x<0:
        print "YOU MISSED, HIT 'r' TO RESTART"
        noLoop()
        #exit()
        
def keyPressed():
    if key=='r':
        global vecPos, vecSpd
        vecPos = PVector(width/2,height/2)
        vecSpd = PVector(random(-10,10),random(-10,10))
        loop()
    



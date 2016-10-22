fltPosX, fltPosY = 0,0
fltPad1,fltPad2 = 0,0
intScore1, intScore2 = 0,0
speed = 3

def setup():
    size(800,450)
    rectMode(CENTER)
    noStroke()
    
def draw():
    background(0)
    translate(width/2,height/2)
    ellipse(fltPosX,fltPosY,20,20)
    
    rect(-width/2+20,fltPad1,20,80)
    rect(width/2-20,fltPad2,20,80)
    
    if keyPressed:
        global fltPad1,fltPad2
        if key=='a':
            fltPad1 += 2
            
        if key=='q':
            fltPad1 -= 2
            
        if key=='l':
            fltPad2 += 2
            
        if key=='o':
            fltPad2 -= 2
            
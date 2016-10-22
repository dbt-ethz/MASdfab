def setup():
    size(800,450)
    background(0)
    
    stroke(255,0,0)
    strokeWeight(10)
    line(100,20,100,430)
    
    intDist = 50

    stroke(0,0,255)
    strokeWeight(10)
    line(100+intDist,20,100+intDist,430)
    
    strokeCap(SQUARE)
    stroke(0,255,0)
    strokeWeight(20)
    line(100+2*intDist,20,100+2*intDist,430)
    

def draw():
    pass
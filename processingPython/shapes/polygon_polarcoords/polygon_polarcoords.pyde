def setup():
    size(800,450)
    
def draw():
    background(50,150,255)
    
    fill(255,255,0)
    beginShape()
    for i in range(7):
        x = width/2 + cos(i*TWO_PI/7) * 100
        y = height/2 + sin(i*TWO_PI/7) * 100
        vertex(x,y)
    endShape(CLOSE)
    
    fill(0,255,0)
    beginShape()
    for i in range(5):
        x = width/2 + cos(i*TWO_PI/5) * 100
        y = height/2 + sin(i*TWO_PI/5) * 100
        vertex(x,y)
    endShape(CLOSE)
x=0
y=0
def setup():
    size(800,450)
    global x,y
    x = width/2
    y = height/2
    background(255)

def draw():
    dx = random(-10,10)
    dy = random(-10,10)
    global x,y
    line(x,y,x+dx,y+dy)
    x = x+dx
    y = y+dy

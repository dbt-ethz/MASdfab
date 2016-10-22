def setup():
    global production,drawLength,theta
    size(800,450)
    drawLength=100.0
    theta=radians(120)
    production="F-FF"
    
def replace():
    global production,drawLength
    production=production.replace("F", "F+FF-F")
    print production
    drawLength=drawLength*0.6

def draw():
    global production
    background(0)
    stroke(255)
    translate(width/2,height/2)
    scale(1,-1)
    for step in production:
        if step == 'F':
            rect(0, 0, -drawLength, -drawLength)
            noFill()
            translate(0, -drawLength)
        elif step == '+':
            rotate(theta)
        elif step == '-':
            rotate(-theta)
        elif step == '[':
            pushMatrix()
        elif step == ']':
            popMatrix()

def keyPressed():
    replace()
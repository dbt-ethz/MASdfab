def setup():
    size(800,450)
    global px,py,sx,sy
    px = width/2
    py = height/2
    sx = random(-10,10)
    sy = random(-10,10)
def draw():
    background(255)
    global px,py,sx,sy
    ellipse(px,py,20,20)
    px+=sx
    py+=sy
    if px>width:
        sx *= -1
    if px<0 and abs(py-mouseY)<50:
        sx *= -1
    if py>height or py<0:
        sy *= -1
    rect(0,mouseY-50,20,100)

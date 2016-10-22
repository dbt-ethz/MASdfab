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
    if px>width or px<0:
        sx *= -1
    if py>height or py<0:
        sy *= -1

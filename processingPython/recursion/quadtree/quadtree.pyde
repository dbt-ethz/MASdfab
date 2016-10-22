t = 512
def setup():
    size(512,512)
    noFill()
    #stroke(255)
    global img
    img = loadImage('data/elefant.png')

def draw():
    background(255)
    #image(img,0,0,width,height)

    subdiv(0,0,width,height)

def subdiv(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    rect(x1,y1,dx,dy)
    if dx>t:
        tmp = img.get(x1,y1,dx,dy)
        tmp.loadPixels()
        found = False
        for p in tmp.pixels:
            if brightness(p)<100:
                found = True
                break
        #if med>30:
        #    found = True

        if found:
            subdiv(x1,y1,x1+dx/2,y1+dy/2)
            subdiv(x1+dx/2,y1,x2,y1+dy/2)
            subdiv(x1,y1+dy/2,x1+dx/2,y2)
            subdiv(x1+dx/2,y1+dy/2,x2,y2)

def keyPressed():
    global t
    save('%s.png' % t)
    t = t/2

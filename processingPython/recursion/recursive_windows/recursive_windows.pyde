def setup():
    size(1600,900)
    stroke(0)
    strokeWeight(0.1)
    #noStroke()
    fill(255)
    global t,u,v,w
    t = PVector(10,10)
    u = PVector(width-10,10)
    v = PVector(10,height-10)
    w = PVector(width-10,height-10)

    noLoop()

def draw():
    # change test
    background(200)
    ladder(t,u,v,w,7)

def ladder(a,b,c,d,l):
    lb = 0.1
    ub = 1-lb
    n = 5
    v1 = PVector.sub(b,a)
    v2 = PVector.sub(d,c)
    #strokeWeight(l/3)
    line(a.x,a.y,b.x,b.y)
    line(c.x,c.y,d.x,d.y)

    l = l-1
    #if l>0:
    if v1.mag()>50 and v2.mag()>50:
        iva = sorted([random(lb,ub) for _ in range(n)])
        iva.insert(0,0)
        iva.append(1)
        ivb = sorted([random(lb,ub) for _ in range(n)])
        ivb.insert(0,0)
        ivb.append(1)
        for i in range(n+1):
            p1 = a+PVector.mult(v1,iva[i])
            p2 = c+PVector.mult(v2,ivb[i])
            p3 = a+PVector.mult(v1,iva[i+1])
            p4 = c+PVector.mult(v2,ivb[i+1])
            ladder(p1,p2,p3,p4,l)
#    else:
#        m = 0
#        beginShape()
#        vertex(a.x+random(-m,m),a.y+random(-m,m))
#        vertex(b.x+random(-m,m),b.y+random(-m,m))
#        vertex(d.x+random(-m,m),d.y+random(-m,m))
#        vertex(c.x+random(-m,m),c.y+random(-m,m))
#        endShape(CLOSE)


def mousePressed():
    redraw()

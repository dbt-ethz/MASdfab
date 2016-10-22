add_library('peasycam')

def setup():
    global positions,positions2
    positions=[]
    positions2=[]
    global production,drawLength,theta,theta2
    size(800,450,P3D)
    drawLength=100.0
    theta=radians(120)
    theta2=radians(120)
    production="F+FF-rF"
    cam=PeasyCam(this,300)
def replace():
    global production,drawLength
    production=production.replace("F", "F+[-F+FF-]F")
    print production
    drawLength=drawLength*0.6

def draw():
    global production,theta,theta2
    theta=mouseX*PI/width
    theta2=mouseY*PI/height
    background(0)
    stroke(255)
    #rtranslate(width/2,height/2)
    #scale(1,-1)
    # noStroke()
    fill(255)
    lights()
    pushMatrix()
    positions=[]
    positions2=[]
    for step in production:
        if step == 'F':
            translate(0, -drawLength)
            fill(255)
            box(drawLength,5,5)
        elif step == '+':
            rotateX(theta)
        elif step == '-':
            rotateY(-theta)
        elif step == '[':
            positions.append(PVector(modelX(0,0,0),modelY(0,0,0),modelZ(0,0,0)))
            fill(255,0,0)
            box(5,10,20)
            pushMatrix()
        elif step == ']':
            fill(0,255,0)
            box(5,10,50)
            positions2.append(PVector(modelX(0,0,0),modelY(0,0,0),modelZ(0,0,0)))
            popMatrix()
    popMatrix()
    for v,v2 in zip(positions,positions2):
        drawEdge(v,v2)
        dX=v.dist(v2)
        translate(dX/2.,0,0)
        box(dX,2,2)
        popMatrix()
        line(v2.x,v2.y,v2.z,v.x,v.y,v.z)
def drawEdge(p1,p2):
    s=PVector(0,0,1)
    tangent=PVector.sub(p2,p1).normalize()
    a=acos(s.dot(tangent))
    r=s.cross(tangent)
    
    pushMatrix()
    translate(p1.x,p1.y,p1.z)
    rotate(a,r.x,r.y,r.z)    
    
def keyPressed():
    replace()
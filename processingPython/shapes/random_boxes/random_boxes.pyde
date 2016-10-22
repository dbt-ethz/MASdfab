add_library('peasycam')

def setup():
    size(800,450,P3D)
    noStroke()
    global lstVec,cam
    cam = PeasyCam(this,500)
    lstVec = [PVector(random(-400,400),random(-210,210),random(-100,100)) for _ in range(20)]
    #lstVec = [PVector(0,0,100),PVector(100,0,0),PVector(0,100,0),PVector(0,0,0)]
    
def draw():
    background(0)
    global lstVec
    for i,p in enumerate(lstVec):
        pushMatrix()
        translate(p.x,p.y,p.z)
        box(4)
        x = screenX(p.x,p.y,p.z)
        y = screenY(p.x,p.y,p.z)
        x = width/2 + (x-width/2)*0.4
        y = height/2 + (y-height/2)*0.4
        popMatrix()
        cam.beginHUD()
        text(str(i),x,y)
        cam.endHUD()

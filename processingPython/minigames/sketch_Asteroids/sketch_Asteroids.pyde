def setup():
    global shipPos,shipAngle,shipSpeed
    global bulletPos,bulletMove
    global listAsteroidsPos,listAsteroidsMove
    size(800,450)
    listAsteroidsPos=[]
    listAsteroidsMove=[]
    bulletPos=None
    shipAngle=0
    shipPos=PVector(width/2,height/2)
    shipSpeed=PVector(1,0)
    for i in xrange(10):
        listAsteroidsPos.append(PVector(random(0,width),random(0,height)))
        listAsteroidsMove.append(PVector(random(-5,5),random(-5,5)))
    
def draw():
    global shipPos,shipAngle,shipSpeed
    global bulletPos,bulletAngle,bulletSpeed
    global listAsteroidsPos,listAsteroidsMove
        
    # move ship
    shipPos.add(shipSpeed)
    if shipPos.x>width:
        shipPos.x=0
    if shipPos.x<0:
        shipPos.x=width
    if shipPos.y>height:
        shipPos.y=0
    if shipPos.y<0:
        shipPos.y=height
        
    # move of bullet
    if bulletPos!= None:
         # check bullet
        for asteroidPos in listAsteroidsPos[:]:
            if (asteroidPos.dist(bulletPos)<10):
                listAsteroidsPos.remove(asteroidPos)
        bulletPos.add(bulletMove)
        if bulletPos.x>width or bulletPos.x<0 or bulletPos.y>height or bulletPos.y<0:
            bulletPos=None
       
    # move of asteroids
    for asteroidPos,asteroidMove in zip(listAsteroidsPos,listAsteroidsMove):
        asteroidPos.add(asteroidMove)
        if (asteroidPos.x>width):
            asteroidPos.x=0
        if (asteroidPos.x<0):
            asteroidPos.x=width
        if (asteroidPos.y>height):
            asteroidPos.y=0
        if (asteroidPos.y<0):
            asteroidPos.y=height
            
   
    
    fill(0,40)
    filter(BLUR,1)
    noStroke()
    rect(0,0,width,height)
    stroke(255)
    noFill()
    
    # draw ship
    pushMatrix()
    translate(shipPos.x,shipPos.y)
    rotate(shipAngle)
    triangle(0,-5,20,0,0,5)
    popMatrix()
    
    # draw asteroids
    for asteroidPos in listAsteroidsPos:
        ellipse(asteroidPos.x,asteroidPos.y,20,20)
        
    # draw bullet
    if bulletPos!= None:
        ellipse(bulletPos.x,bulletPos.y,5,5)
        

def keyPressed():
    global shipAngle, shipSpeed,bulletPos,bulletMove
    if key=='a':
        shipAngle+=0.2
    if key=='s':
        shipAngle-=0.2
    if key=='w':
        shipSpeed.x+=cos(shipAngle)*3
        shipSpeed.y+=sin(shipAngle)*3
        shipSpeed.limit(10)
    if (key=='x'):
        bulletPos=PVector(shipPos.x,shipPos.y)
        bulletMove=PVector(cos(shipAngle)*3+shipSpeed.x,sin(shipAngle)*3+shipSpeed.y)
    
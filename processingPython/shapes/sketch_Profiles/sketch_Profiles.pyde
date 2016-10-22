add_library('peasycam')

def setup():
    global nLayers
    nLayers=50
    size(800, 450, P3D)
    cam=PeasyCam(this,200)
    
def draw():
  # here we draw for each layer a new profile
  # we connect the previous layer with the current layer as Quadstrip to a mesh.
  noStroke()
  lights()
  background(0)
  pointsOld=[]
  for j in range(nLayers):
    points=profileRecursive(j)
    if j>0:
      beginShape(QUAD_STRIP)
      for i in xrange(len(points)):
        point=points[i%len(points)]
        pointOld=pointsOld[i%len(points)]
        vertex(pointOld.x, pointOld.y, pointOld.z*4)
        vertex(point.x, point.y, point.z*4)
      endShape()
    pointsOld=points

# returns an ArrayList of PVectors as a polygon with changing shape depending on z
# in each iteration, a new point in each segment between two points is inserted
# this point is shifted with a certaing factor orthogonal to this segment.
# this splitting happens in the method splitLines
def profileRecursive(z):
    points=profileCircle(20, 7, z);
    points=splitLines(points, sin(z/5.0)*10)
    points=splitLines(points, 40-z)
    points=splitLines(points, -2)
    points=splitLines(points, 4)
    points=splitLines(points, -1)
    # points=splitLines(points, 2)
    # points=splitLines(points, 1)
    # points=splitLines(points, 2)
    # points=splitLines(points, -0.5f);
    return points

# returns an ArrayList of PVectors of a regular sphere
def profileCircle(radius,nSegments,z):
    points=[]
    for i in range(nSegments):
        angle=2*PI*i/nSegments
        points.append(PVector(radius*cos(angle), radius*sin(angle), z))
    return points

# returns a new List of PVectors
# each segment between two points is splitted at the center
# this splitpoint is shifted by shift along the the normal of the segment

def splitLines(inputPoints, shift):
    newpoints=[]
    nP=len(inputPoints)
    for i in xrange(nP):
        p0=inputPoints[i]
        p1=inputPoints[(i+1)%nP]
        d=p0.dist(p1)
        n=PVector((p1.y-p0.y)/d, (p0.x-p1.x)/d)
        n.mult(shift)
        newpoints.append(p0.get())
        center=PVector((p1.x+p0.x)*0.5+n.x, (p1.y+p0.y)*0.5+n.y, (p1.z+p0.z)*0.5)
        newpoints.append(center)
    return newpoints

def profileSinus(z):
    points=profileCircle(20, 512, z)
    applySinusWave(points, 3, 8, z/5.0)
    applySinusWave(points, 8, 2, z/5.0)
    applySinusWave(points, 32, 2, z/5.0-PI)
    return points

def applySinusWave(inputPoints,freq,amp,phase):
    biSectors=[]
    nP=len(inputPoints)
    for i in range(nP):
        iPrev=i-1
        if iPrev<0:
            iPrev=nP-1
        p0=inputPoints[iPrev]
        p1=inputPoints[i]
        p2=inputPoints[(i+1)%nP]
        biSectors.append(getBisector(p0, p1, p2))
    for i in range(nP):
        p1=inputPoints[i]
        bi=biSectors[i]
        angle=2*PI*i/nP
        r=sin(angle*freq+phase)*amp
        bi.mult(r)
        p1.add(bi)

def getNormal(v0,v1):
    d=p0.dist(p1)
    return PVector((p1.y-p0.y)/d, (p0.x-p1.x)/d)

#returns the bisector between three points
def getBisector(v0,v1,v2):
    dX1=v0.x-v1.x
    dY1=v0.y-v1.y
    n1=PVector(-dY1, dX1)
    n1.mult(1.0/n1.mag())
    dX2=v2.x-v1.x
    dY2=v2.y-v1.y
    n2=PVector(dY2, -dX2)
    n2.mult(1.0/n2.mag())
    bi=PVector((n1.x+n2.x)*0.5, (n1.y+n2.y)*0.5)
    mag=bi.mag();
    if (bi.mag()<0.0001):
        bi.mult(1.0/mag)
        return bi
    return n1
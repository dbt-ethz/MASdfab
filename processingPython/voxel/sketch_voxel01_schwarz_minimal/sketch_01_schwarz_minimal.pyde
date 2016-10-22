add_library('controlP5')
add_library('peasycam')
add_library('hdgeom')

def setup():
    size(1200,900, P3D)
    global isovalue, isoslider, cam, cp5
    cam = PeasyCam(this,200)
    noStroke()

    cp5 = ControlP5(this)
    isoslider = cp5.addSlider("ISO").setRange(-3,3)
    cp5.setAutoDraw(False)

    construct()

def draw():
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)

    background(0)
    lights()

    scale(10)
    translate(-nx/2,-ny/2,-nz/2)

    global voxelShape
    voxelShape = voxelSpace.getPShape(this,isoslider.getValue())
    shape(voxelShape)
    '''
    for i in range(nx*ny*nz):
        x = voxelSpace.getX(i)
        y = voxelSpace.getY(i)
        z = voxelSpace.getZ(i)
        v = voxelSpace.get(i)
        v = (v+3)/6
        stroke(v*255)
        point(x,y,z)
    '''

    cam.beginHUD()
    noLights()
    cp5.draw()
    cam.endHUD()

def construct():
    global voxelSpace, voxelShape, nx, ny, nz
    nx = 100
    ny = 70
    nz = 20
    voxelSpace = VoxelSpace(nx,ny,nz)

    for i in range(nx*ny*nz):
        x = voxelSpace.getX(i)
        y = voxelSpace.getY(i)
        z = voxelSpace.getZ(i)
        fx = float(x)/nx
        fy = float(y)/ny
        fz = float(z)/nz
        v = cos(fx*TWO_PI)+cos(fy*TWO_PI)+cos(fz*TWO_PI)
        voxelSpace.set(i, v)

    print voxelSpace.getMin(),voxelSpace.getMax()
    voxelShape = voxelSpace.getPShape(this,0)

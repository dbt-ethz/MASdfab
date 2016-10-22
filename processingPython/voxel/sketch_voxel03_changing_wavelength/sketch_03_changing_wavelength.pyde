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

    #global voxelShape
    #voxelShape = voxelSpace.getPShape(this,isoslider.getValue())
    shape(voxelShape)

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

        fact = (z+1)/20.0
        v = cos(fx*TWO_PI*fact)+cos(fy*TWO_PI*fact)+cos(fz*TWO_PI*fact)
        #v = v+sin(fx*TWO_PI*8)/3 + sin(fy*TWO_PI*9)/3 + sin(fz*TWO_PI*10)/3
        #v = 3*(cos(fx*TWO_PI) + cos(fy*TWO_PI) + cos(fz*TWO_PI)) + 4* cos(fx*TWO_PI) * cos(fy*TWO_PI) * cos(fz*TWO_PI)
        voxelSpace.set(i, v)
    #voxelSpace.setValueToBorders(4)

    print voxelSpace.getMin(),voxelSpace.getMax()
    voxelShape = voxelSpace.getPShape(this,0)

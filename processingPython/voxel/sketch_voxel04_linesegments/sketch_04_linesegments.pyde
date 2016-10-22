add_library('controlP5')
add_library('peasycam')
add_library('hdgeom')

def setup():
    size(1200,900, P3D)
    global isovalue, isoslider, cam, cp5
    cam = PeasyCam(this,200)
    #noStroke()
    stroke(255)
    fill(0)

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
    for i in range(20):
        vs = VoxelSpace(nx,ny,nz)
        vs.distSegment(random(nx),random(ny),random(nz),random(nx),random(ny),random(nz),4)
        for j in range(nx*ny*nz):
            v1 = vs.get(j)
            v2 = voxelSpace.get(j)
            voxelSpace.set(j,max(v1,v2))

    print voxelSpace.getMin(),voxelSpace.getMax()
    voxelShape = voxelSpace.getPShape(this,1)

def keyPressed():
    if key=='b':
        global voxelSpace, voxelShape
        blur = VoxelBlur()
        blur.blur(voxelSpace,4)
        voxelShape = voxelSpace.getPShape(this,1)

    if key=='e':
        mc = voxelSpace.getMarchinCubeMesh(1)
        mc.saveObj(sketchPath("")+"filename.obj")

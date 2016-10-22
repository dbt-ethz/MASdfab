def setup():
    size(800,450)
    global pic
    # image file must be in <sketchfolder>/data
    pic = loadImage("ball.png")
    imageMode(CENTER)
    
def draw():
    # different method to specify a color, hexadecimal code
    background("#65A234")
    # display image at mouse position
    image(pic,mouseX,mouseY,100,100)
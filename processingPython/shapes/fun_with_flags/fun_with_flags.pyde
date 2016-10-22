import os

def setup():
    size(1216,672)
    background(255)
    
    path = '/Users/bernham/Documents/CAAD/Experiments/flags/flags/flags/flat/64/'
    fns = os.listdir(path)
    dx = 64
    dy = 48

    cnt = 1
    for j in range(14):
        for i in range(19):
            if cnt>=260:
                break
            pic = loadImage(path+fns[cnt])
            pic = pic.get(0,8,64,48)
            image(pic,i*dx,j*dy)
            cnt += 1
    
def draw():
    pass
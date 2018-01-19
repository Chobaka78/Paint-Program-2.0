from pygame import * 
size=(800,600)
screen = display.set_mode(size) 

picnames = ["brick.png","rock.png","sky.png","grass.png"]
textures = []

for name in picnames:
    pic = image.load(name) ## actual picture 
    textures.append(pic)     


######################### at this point the textures list has 4 images 

canvasRect = Rect(10,50,600,500)
screen.fill((255,170,200))
draw.rect(screen,(255,255,255), canvasRect)

pos = 0 
screen.blit(textures[0].subsurface((0,0,50,50)),(25,50))   
omx = 0
omy = 0

running = True
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False

        if evt.type == MOUSEBUTTONDOWN:

            n = len(textures)
            if evt.button == 4:
                pos = (pos+1)%n
            if evt.button == 5:
                pos = (pos+n-1)%n
            screen.blit(textures[pos].subsurface((0,0,50,50)),(25,50)) 

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if canvasRect.collidepoint(mx,my):

        if mb[0] == 1:

            draw.line(screen,(0,0,0),(omx,omy),(mx,my),1)

        elif mb[2] == 1:

            sample = (textures[pos].subsurface((mx,my,30,30))) 
            screen.blit(sample, (mx-25,my-25))

    omx = mx
    omy = my

    display.flip() 
quit() 

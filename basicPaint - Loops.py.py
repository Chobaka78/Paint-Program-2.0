#basicPaint.py

from pygame import *
from random import*
from tkinter import*
from math import*

root=Tk()
root.withdraw() ## removes the extra TK window

init()
font.init()

size=(1080,720)
screen = display.set_mode(size)

## Fonts

comicFont = font.SysFont("Times New Roman",26)
displayText = comicFont.render("Backgrounds",True,(0,0,0))
rotPic = displayText

## other variables

eradius = 10
radius = 10
t = 5
lthick = 5
elthick = 5
page = 0
stamp = "no stamp"
background = "nothing"
size = 10
choice = "nothing"

## Colours

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW = (226, 244, 66)
LIGHTBLUE = (0, 255, 250)
PINK = (255, 0, 246)
PURPLE = (165, 0, 255)
MEGENTA = (255, 0, 144)
AQUA_BLUE = (2, 255, 191)
GREEN_YELLOW = (131, 255, 0)

## time 

myTime = time.Clock()



####################################################
## MUSIC
music_l = ["music/Genki Dama Theme.mp3","music/BeerusMadness.wav", "music/Ultra Instinct Reborn.wav",
"music/Time To Strike Back.wav", "music/Frieza is Resurrected.wav", "music/Dragonballsuper.wav"]

music = []
b = 0

for i in range(5):
    music.append(music_l[i])

mixer.music.load(music[b])
mixer.music.play()
# mixer.Sound.play(dbz_M)
# mixer.music.play(-1)

########################################################

## EVERYTHING FOR REGULAR IMAGES
########################################################

## Loading all regular 

dragonball = image.load("images/Dragonballback.png") ## back ground (put images/"name") this indicates it's in images folder
wheelPic = image.load("images/colwheel.jpg")
upArrowPic = image.load("images/up arrow.png")
downArrowPic = image.load("images/down arrow.png")
loadIcon = image.load("images/icons/load.png")
saveIcon = image.load("images/icons/save.jpg")
backIcon = image.load("images/icons/back_button.png")
prevPic = image.load("images/prevous.png")
playPic = image.load("images/play and pause.png")
nextPic = image.load("images/next.png")
##########################################################

## Rects for regular

dragonrect = Rect(0,0,1080,720) ## this if for the background
canvasB = Rect(204,120,684,454) ## this is the rectangular black border for the canvas
canvasRect = Rect(206,122,680,450) ## this is the canvas
wheelRect = Rect(683,600,200,100) ## colour wheel rectangle 
platB = Rect(204,598,684,104) ## platform border
platRect = Rect(206,600,680,100) ## platform where all the tools will be
sideplatB = Rect(96,598,104,104)
sideplat = Rect(98,600,100,100)
screRect = Rect(10,122,185,450) ## screen where more options will be displayed
screB_Rect = Rect(8,120,189,454)
loadRect = Rect(105,602,40,40)
saveRect = Rect(155,602,40,40)
show_colourrect = Rect(593,607,80,40)
upArrowRect = Rect(15,125,170,25)
downArrowRect = Rect(15,540,170,25)
prevRect = Rect(510,650,40,40)
playRect = Rect(560,650,40,40)
nextRect = Rect(610,650,40,40)
#############################################

## Transforming - scaling images

dragonT=transform.scale(dragonball,(1080,720)) ## scaling the background
wheelT=transform.scale(wheelPic,(202,99))
loadT = transform.scale(loadIcon,(40,40))
saveT = transform.scale(saveIcon,(40,40))
####################################################### 

# EVERYTHING FOR TOOLS
#######################################################

## Loading all tool images

toolimg = ["images/eraser.png", "images/pencil.png", "images/stamp tool.png", 
 "images/ellipse.png", "images/rectangle tool.png", "images/spraypaint.png",
"images/icons/back_button.png", "images/colour_picker tool.png", "images/textbox.png", 
"images/paintbrush.png", "images/marker_tool.png", "images/Undo.png", "images/Redo.png", "images/lineTool.png"]

tool_image = []

for i in toolimg:
    iPic = image.load(i)
    tool_image.append(iPic)

toolRects = [ Rect(210,650,40,40), Rect(210,605,40,40), Rect(260,650,40,40), 
Rect(260,605,40,40), Rect(310,605,40,40), Rect(360,605,40,40), Rect(410,605,40,40), 
Rect(460,605,40,40), Rect(460,650,40,40), Rect(360,650,40,40), Rect(410,650,40,40), 
Rect(105,652,40,40), Rect(155,652,40,40), Rect(310,650,40,40)]


tool_list = ["eraser", "pencil", "stamp", "ellipse", "rectangle", 
"spraypaint", "background", "colour_picker", "text", "paint", 
"marker", "undo", "redo", "line"]
#########################################################

## EVERYTHING FOR STAMPS

## load all stamps

stampimg = ["images/Choice 1/goku_ssgss.png", "images/Choice 1/goku ultra instinct.png", 
"images/Choice 1/goku ssg.png", "images/Choice 1/Jiren.png","images/Choice 1/gohan.png", 
"images/Choice 1/beerus.png","images/Choice 1/Kefla.png", "images/Choice 1/vegeta blue.png",
"images/Choice 1/black x zamsu.png", "images/Choice 1/Goku_Black rose.png", 
"images/Choice 1/golden freza.png", "images/Choice 1/Goku_Black.png"]

stamp_image = []

for a in stampimg:
    stamp_img = image.load(a)
    stamp_image.append(stamp_img)

stamp_list = ["gokub", "goku_u", "goku_ssg", "jerin", 
"gohan", "beerus", "kefla", "vegeta", "black_zamaus", 
"goku_rose", "goku_black", "goldenFreza"]


##############################################

# Transforming stamps
w = [217, 192, 128, 144, 117, 128, 116, 132, 125, 128, 118, 119]

h = [228, 135, 211, 240, 170, 218, 155, 203, 252, 235, 187, 160]

stamps_image = []

for s in range(12):
    stampI = transform.scale(stamp_image[s],(w[s],h[s]))
    stamps_image.append(stampI)

stampIcon = ["images/icons/goku icon.png", "images/icons/goku ultra.png", "images/icons/goku ssg.png",
"images/icons/jerin.png", "images/icons/gohanicon.png","images/icons/beerus.jpg",
"images/icons/kefla.png", "images/icons/vegeta.png", "images/icons/merged icon.png",
"images/icons/roseicon.png", "images/icons/golden freza.png", "images/icons/goku black.png"]

stamp_icon = []

for j in stampIcon:
    stampicons = image.load(j)
    stamp_icon.append(stampicons)

################################################

## Stamp Rects

stampRect = [Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100),
Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100), Rect(50,155,100,100),
Rect(50,295,100,100), Rect(50,420,100,100), Rect(50,155,100,100), Rect(50,295,100,100),
Rect(50,420,100,100)]

#########################################################

## EVERYTHING FOR Backgrounds

## Loaing backround images

backtext = ["images/back/page04.png", "images/back/page05.png", 
"images/back/page03.png", "images/back/page06.png", 
"images/back/page09.png", "images/back/page08.png", "images/back/page02.png", 
"images/back/page10.png", "images/back/page07.png", "images/back/Whiteback.png",]

texts = []

for s in backtext:
    im = image.load(s)
    texts.append(im)

backimage = ["images/Background/beerus_planet.jpg", "images/Background/boat_place.jpg", 
"images/Background/Kame_house.png", "images/Background/king_kai.jpg", "images/Background/nameless planet_stage.png", 
"images/Background/nameless_planet.png", "images/Background/stage tournment of power.png", "images/Background/super_dragon.png", 
"images/Background/tower.jpg", "images/Background/whiteback.jpg",]

textures = []

for n in backimage:
    pic = image.load(n) ## actual picture 
    textures.append(pic)

#########################################################

## All background rects

backrects = [Rect(20,250,165,30), Rect(20,290,165,30), Rect(20,210,165,30), 
Rect(20,330,165,30), Rect(20,450,165,30), Rect(20,410,165,30), 
Rect(20,170,165,30), Rect(20,490,165,30), Rect(20,370,165,30), 
Rect(20,530,165,30)]

###########################################################

## Default variables

col=BLACK #default colour is black
bcol = WHITE ## default colour for background
tool = "nothing" ## default tool is nothing 
display.set_caption("Dragon ball super Paint") ## for displaying dragon ball super paint in top left hand corner

###############################################
## BLITTING ALL REGULAR + ALL IMAGES / TOOLS
###############################################

screen.blit(dragonT,dragonrect) ## adding the background 
draw.rect(screen,BLACK,canvasB)
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,platB)
draw.rect(screen,WHITE,platRect)
draw.rect(screen,BLACK,sideplatB)
draw.rect(screen,WHITE,sideplat)
draw.rect(screen,BLACK,screB_Rect)
draw.rect(screen,WHITE,screRect)
screen.blit(wheelT,wheelRect)
draw.rect(screen,BLACK,Rect(591,605,84,44),0)
screen.blit(loadT,loadRect)
screen.blit(saveT,saveRect)
screen.blit(prevPic, prevRect)
screen.blit(playPic, playRect)
screen.blit(nextPic, nextRect)

for i in range(14):

    screen.blit(tool_image[i], toolRects[i])

###################################################

running = True
canvas_copy = screen.subsurface(canvasRect).copy()
canvas = screen.subsurface(canvasRect)
undo=[canvas_copy]
redo = []
## omx and omy is basically just mx and my but you need to put omx and omy

omx=300 
omy=300

while running:
    click = False ## for 1 step programs

    draw.rect(screen,col,show_colourrect,0)
  
    ## Random colours
    rred = randint(0,255)
    rgreen = randint(0,255)
    rblue = randint(0,255)
        
    for evt in event.get():
        
        if evt.type == QUIT:            
            running = False
            
        if evt.type == KEYDOWN:        
            if evt.key == K_RIGHT:
                if b <= len(music_l):
                    b += 1    
                    try:
                        mixer.music.load(music_l[b])
                    except:
                        b -= 1
                        mixer.music.load(music_l[b])
                    mixer.music.play(-1)

            if evt.key == K_LEFT:
                if b <= len(music_l):
                    if b >= 0:
                        b -= 1
                        if b == -1:
                            b += 1    
                        print(b)
                    mixer.music.load(music_l[b])
                    mixer.music.play(-1)                        

            if evt.key==K_RIGHT and tool == "eraser":
                eradius+=5

            elif evt.key==K_LEFT and tool == "eraser":
                eradius-=5

        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                if canvasRect.collidepoint((mx, my)):
                    undo.append(canvas.copy())

            if evt.button == 1 and toolRects[11].collidepoint(mx,my):
                if len(undo) > 1:
                    redo.append(undo.pop())
                    canvas.blit(undo[-1], (0,0))

            if evt.button == 1 and toolRects[12].collidepoint(mx,my):
                if len(redo) > 0:
                    undo.append(redo.pop())
                    canvas.blit(undo[-1], (0,0))
        if evt.type == MOUSEBUTTONDOWN:

            click = True
            sx,sy = evt.pos

            if evt.button == 1:
                canvas.copy()

            if evt.button == 5: # scrolling down

                if tool =="circle":
                    radius -=1

                    if radius <2:
                        radius =2

                elif tool == "rectangle":
                    t -=1

                    if t <0:
                        t = 0

                elif tool == "eraser":
                    eradius -=1

                    if eradius <0:
                        eradius =0

                elif tool == "ellipse":
                    elthick -=1

                    if elthick <0:
                        elthick =1

                elif tool == "line":
                    lthick -=1

                    if lthick <0:
                        lthick =1

            if evt.button == 4:

                if tool == "circle":
                    radius +=1

                elif tool == "rectangle":
                    t +=1

                elif tool == "eraser":
                    eradius +=1

                elif tool == "line":
                    lthick +=1

                elif tool == "ellipse":
                    elthick +=1

            background = screen.copy()

    mx,my=mouse.get_pos()

    # print(mx,my)

    # print(mx,my)## to calculate the x and y of anthing if needed (helpful)

    mb=mouse.get_pressed() ## shorter version of the mouse button check
#################################################################

## ALL EFFECTS FOR TOOLS
#################################################
    for u in range(14):
        draw.rect(screen,GREEN,toolRects[u],2)
        draw.rect(screen,BLACK,toolRects[11],2)
        draw.rect(screen,BLACK,toolRects[12],2)

    for m in range(14):

        if toolRects[m].collidepoint(mx,my):
            draw.rect(screen,BLUE,toolRects[m],2)

    for i in range(14):

        if tool == tool_list[i]:
            draw.rect(screen,BLACK,screB_Rect)
            draw.rect(screen,WHITE,screRect)

    for d in range(14):
        if tool == tool_list[d]:
            draw.rect(screen,RED,toolRects[d],2)
#############################################

    if tool == "background" and page == 0:
        draw.rect(screen,BLACK,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        screen.blit(rotPic,(20,130))

        
        for d in range(10):
            screen.blit(texts[d], backrects[d])
            draw.rect(screen,BLACK,backrects[d],2)

            if backrects[d].collidepoint(mx,my):
                draw.rect(screen,BLUE,backrects[d],3)
########################################################
    elif tool == "pencil":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
#########################################################
    elif tool == "eraser":
        draw.rect(screen,GREEN,screB_Rect)
        draw.rect(screen,WHITE,screRect)
########################################################
    elif tool == "stamp" and page ==0:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for i in range(0,3):
            screen.blit(stamp_icon[i], stampRect[i])
            draw.rect(screen,BLACK,stampRect[i],2)

            if stampRect[i].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[i],3)

        screen.blit(downArrowPic,downArrowRect)
########################################################
    elif tool == "stamp" and page==1:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for i in range(3,6):
            screen.blit(stamp_icon[i], stampRect[i])
            draw.rect(screen,BLACK,stampRect[i],2) 

            if stampRect[i].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[i],3)   

        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)
#######################################################
    elif tool == "stamp" and page== 2:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for h in range(6,9):
            screen.blit(stamp_icon[h], stampRect[h])
            draw.rect(screen,BLACK,stampRect[h],2)

            if stampRect[h].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[h],3)
        
        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)
#######################################################
    elif tool == "stamp" and page==3:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for e in range(9,12):
            screen.blit(stamp_icon[e], stampRect[e])
            draw.rect(screen,BLACK,stampRect[e],2)

            if stampRect[e].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[e],3)

        screen.blit(upArrowPic,upArrowRect)
#######################################################

    if page == 0:
        for i in range(0, 3):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)
###########################################################
    elif page == 1:
        for i in range(3, 6):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)
##########################################################
    elif page == 2:
        for i in range(6, 9):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)
#########################################################
    elif page == 3:
        for i in range(9, 12):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)
#########################################################
    ##print(page,tool)
############################################################
    if mb[0]: ## Checking left click

        for m in range(14):

            if toolRects[m].collidepoint(mx,my):
                tool = tool_list[m]

            if toolRects[3].collidepoint(mx,my):
                stamp = "nothing"
                page = 0

        if tool == "colour_picker" or "text" or "paint" or "marker":
            RC = (rred,rgreen,rblue)

        if tool == "background":
            page = 0


    if mb[0]==1: ## if left click

        if canvasRect.collidepoint(mx,my): ## make sure all the lines stay within the canvas
            screen.set_clip(canvasRect) ## only the canvas can be updated

            if tool=="pencil": ## if the tool selected is a pencil
                draw.line(screen,col,(omx,omy),(mx,my),3) ## draw lines with a thick ness of 3

            elif tool=="eraser": ## if tool is eraser
                ax,ay = omx-mx,omy-my
                dist = max(abs(ax),abs(ay))
                for l in range (dist):
                    x = int(mx+l/dist*ax)
                    y = int(my+l/dist*ay)
                    draw.circle(screen,WHITE,(x,y),size)

            elif tool == "eraser" and back == True:
                draw.circle(screen,bcol,(mx,my),eradius)

            elif tool == "circle":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.circle(screen,col,(sx,sy),radius,2)

            elif tool == "rectangle":            
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                distx = mx-sx
                disty = my-sy

                if t%2 == 0:
                    t+=1

                draw.rect(screen,col,Rect(sx,sy,distx,disty),t)
                ### to add the squares to the end of the rectangle
                draw.rect(screen,col,Rect(sx-(t/2)+1,sy-(t/2)+1,t,t),0)
                draw.rect(screen,col,Rect((sx+distx)-(t/2)-(1/2),sy-(t/2)+1,t,t),0)
                draw.rect(screen,col,Rect(sx-(t/2)+1,(sy+disty)-(t/2)-(1/2),t,t),0)
                draw.rect(screen,col,Rect((sx+distx)-(t/2),(sy+disty)-(t/2),t,t),0)
            

            elif tool == "ellipse":             
                screen.fill((0,0,0))
                screen.blit(background,(0,0))

                try:
                    ellRect = Rect(sx,sy,mx-sx,my-sy)
                    ellRect.normalize()               
                    draw.ellipse(screen,col,ellRect,elthick)

                except:
                    pass

            elif tool == "line":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.line(screen,col,(sx,sy),(mx,my),lthick)
                draw.circle(screen,col,(sx,sy),lthick//2)
                draw.circle(screen,col,(mx,my),lthick//2)

            elif tool == "colour_picker":

                if canvasRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
                    col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)
                    print(col) ## print default colour

            elif tool == "spraypaint":

                screen.set_clip(canvasRect)
                if canvasRect.collidepoint(mx,my):
                    radius=size
                    for i in range (30):
                        dx = randint(-radius,radius)
                        dy = randint(-radius,radius)
                        if hypot(dx,dy) <=radius:
                            draw.circle(screen,col,(mx+dx,my+dy),0)

            elif tool == "paint":

                if canvasRect.collidepoint(mx,my):
                    ax,ay = omx-mx,omy-my
                    dist = max(abs(ax),abs(ay))
                    for l in range (dist):
                        x = int(mx+l/dist*ax)
                        y = int(my+l/dist*ay)
                        draw.circle(screen,col,(x,y),size)

            elif tool=="marker":
                #screen.set_clip(canvasRect)
                if mb[0]==1:
                    dx,dy = omx-mx,omy-my
                    dist = max(abs(dx),abs(dy))
                    for i in range(dist):
                        x=int(mx+i/dist*dx)
                        y=int(my+i/dist*dy)
                        cover = Surface((size,size),SRCALPHA)
                        draw.circle(cover,(col[0],col[1],col[2],2),(size//2,size//2),size//2)
                        screen.blit(cover,(x-size//2,y-size//2))


############################################################ using tool for tools 1

        if page ==0:

            for g in range(0, 3):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    #screen.blit(stamps_image[g], (mx-(w[g])//2, my-(h[g])//2))
                    screen.blit(stamps_image[g], ((mx-62), (my-101)))

        if page == 1:

            for g in range(3, 6):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    #screen.blit(stamps_image[g], (mx-(w[g])//2, my-(h[g])//2))
                    screen.blit(stamps_image[g], ((mx-64), (my-157)))


        elif page == 2:

            for g in range(6, 9):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    # screen.blit(stamps_image[g], (mx-(w[g]//2), my-(h[g]//2)))
                    screen.blit(stamps_image[g], ((mx-62), (my-101)))

        elif page == 3:

            for g in range(9, 12):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    # screen.blit(stamps_image[g], (mx-(w[g])//2, my-(h[g])//2))
                    screen.blit(stamps_image[g], ((mx-60),(my-145)))


##################################################################
        if page ==0 and tool == "background":

            for k in range(10): ## Blitting all the images for the backgrounds
                if backrects[k].collidepoint(mx,my):
                    screen.blit(textures[k], canvasRect)

    if click:

                if downArrowRect.collidepoint(mx,my) and page >=0 and page <3 and tool == "stamp":
                    page+=1

                elif page!=0 and upArrowRect.collidepoint(mx,my) and page >0 and page <=3 and tool == "stamp" :
                    page -=1
                    
                screen.set_clip(None) # modify everything

                ## SAVING THE PROGRAM

                if saveRect.collidepoint(mx,my):
                    try:
                        fname = filedialog.asksaveasfilename(defaultextension = ".png")
                        ## asks the user to enter the file name they would like to save as
                        if fname !="":
                            image.save(screen.subsurface(canvasRect),fname)

                    except:
                        pass ## prevent from program crashing
                        print("saving error")

                ## OPENING A PROGRAM 

                if loadRect.collidepoint(mx,my):
                    try:
                        fname = filedialog.askopenfilename(filetypes = [("images","*.png;*.jpg;*.jpeg")])              
                        screen.set_clip(canvasRect)
                        myPic = image.load(fname)
                        myPic1 = transform.scale(myPic,(680,450))
                        screen.blit(myPic1,canvasRect)
                        screen.set_clip(None)

                    except:
                        print("loading error")
                        pass

#####Changing the colour

    if mb[0]==1: ## check if left click

        if wheelRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
            col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)
            print(col) ## print default colour

    # if tool == "eraser" and canvasRect.collidepoint(mx,my):
    #             screen.fill((0,0,0))
    #             screen.blit(background,(0,0))
    #             draw.circle(screen,col,(mx,my),eradius,1)
           
    omx=mx ## setting omx to mx                          
    omy=my ## setting omy to my
    display.flip()
    
quit() # closes out pygame window


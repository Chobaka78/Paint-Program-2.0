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



## Music

dbz_M = mixer.Sound("music/Dragonballsuper.wav")
mixer.music.load("music/Dragonballsuper.wav")
mixer.Sound.play(dbz_M)
mixer.music.play(-1)

## load all regular

dragonball = image.load("images/Dragonballback.png") ## back ground (put images/"name") this indicates it's in images folder
wheelPic = image.load("images/colwheel.jpg")
eraserPic = image.load("images/eraser.png")
pencilPic = image.load("images/pencil.png")
stampPic = image.load("images/stamp tool.png")
circlePic = image.load("images/circle tool.png")
rectanglePic = image.load("images/rectangle tool.png")
sprayPic = image.load("images/spraypaint.png")
upArrowPic = image.load("images/up arrow.png")
downArrowPic = image.load("images/down arrow.png")
colourPic = image.load("images/colour_picker tool.png")
textPic = image.load("images/textbox.png")
paintbrushPic = image.load("images/paintbrush.png")
markerPic = image.load("images/marker_tool.png")
loadIcon = image.load("images/icons/load.png")
saveIcon = image.load("images/icons/save.jpg")
backIcon = image.load("images/icons/back_button.png")
paint_brushPic = image.load("images/paintbrush.png")
markerPic = image.load("images/marker_tool.png")
Undo = image.load("images/Undo.png")
Redo = image.load("images/Redo.png")

#########################################################

## load all stamps

gokuPic = image.load("images/Choice 1/goku_ssgss.png")
goku_ultraPic = image.load("images/Choice 1/goku ultra instinct.png")
gohanPic = image.load("images/Choice 1/gohan.png")
beerusPic = image.load("images/Choice 1/beerus.png")
goku_ssgPic = image.load("images/Choice 1/goku ssg.png")
jerinPic = image.load("images/Choice 1/Jiren.png")
keflaPic = image.load("images/Choice 1/Kefla.png")
vegetabPic = image.load("images/Choice 1/vegeta blue.png")
black_zamasu = image.load("images/Choice 1/black x zamsu.png")
goku_blackPic = image.load("images/Choice 1/Goku_Black.png")
golden_frezaPic = image.load("images/Choice 1/golden freza.png")
goku_rose = image.load("images/Choice 1/Goku_Black rose.png")

#######################################################

## load all stamp icons 

gokuIcon = image.load("images/icons/goku icon.png")
gohanIcon = image.load("images/icons/gohanicon.png")
goku_ssgIcon = image.load("images/icons/goku ssg.png")
beerusIcon = image.load("images/icons/beerus.jpg")
goku_ultraIcon = image.load("images/icons/goku ultra.png")
jerinIcon = image.load("images/icons/jerin.png")
keflaIcon = image.load("images/icons/kefla.png")
vegetaIcon = image.load("images/icons/vegeta.png")
blackzamausIcon = image.load("images/icons/merged icon.png")
gokuroseIcon = image.load("images/icons/roseicon.png")
golden_frezaIcon = image.load("images/icons/golden freza.png")
goku_black = image.load("images/icons/goku black.png")

## Load all background text
backtext = ["images/back/page04.png", "images/back/page05.png", "images/back/page03.png", "images/back/page06.png", 
"images/back/page09.png", "images/back/page08.png", "images/back/page02.png", "images/back/page10.png", 
"images/back/page07.png", "images/back/Whiteback.png",]

texts = []

for s in backtext:
    im = image.load(s)
    texts.append(im)

#############################################################

## load all background images

backimage = ["images/Background/beerus_planet.jpg", "images/Background/boat_place.jpg", 
"images/Background/Kame_house.png", "images/Background/king_kai.jpg", "images/Background/nameless planet_stage.png", 
"images/Background/nameless_planet.png", "images/Background/stage tournment of power.png", "images/Background/super_dragon.png", 
"images/Background/tower.jpg", "images/Background/whiteback.jpg",]

textures = []

for n in backimage:
    pic = image.load(n) ## actual picture 
    textures.append(pic)

## default colour 

col=BLACK #default colour is black

bcol = WHITE ## default colour for background

## default tool

tool = "nothing" ## default tool is nothing 

display.set_caption("Dragon ball super Paint") ## for displaying dragon ball super paint in top left hand corner

###############################################

## identifying all rects for tools 

dragonrect = Rect(0,0,1080,720) ## this if for the background
canvasB = Rect(204,120,684,454) ## this is the rectangular black border for the canvas
canvasRect = Rect(206,122,680,450) ## this is the canvas
pencilRect = Rect(210,605,40,40) ## pencil rectagle 
eraserRect = Rect(210,650,40,40) ## eraser rectangle 
wheelRect = Rect(683,600,200,100) ## colour wheel rectangle 
platB = Rect(204,598,684,104) ## platform border
platRect = Rect(206,600,680,100) ## platform where all the tools will be
sideplatB = Rect(96,598,104,104)
sideplat = Rect(98,600,100,100)
screRect = Rect(10,122,185,450) ## screen where more options will be displayed
screB_Rect = Rect(8,120,189,454)
circleRect = Rect(260,605,40,40)
stampRect = Rect(260,650,40,40)
rectangleRect = Rect(310,605,40,40)
lineRect = Rect(310,650,40,40)
ellipseRect = Rect(360,650,40,40)
sprayRect = Rect(360,605,40,40)
backRect = Rect(410,605,40,40)
colourRect = Rect(460,605,40,40)
textRect = Rect(460,650,40,40)
paintRect = Rect(510,605,40,40)
markerRect = Rect(510,650,40,40)
loadRect = Rect(105,602,40,40)
saveRect = Rect(155,602,40,40)
show_colourrect = Rect(593,607,80,40)
undoRect = Rect(105,652,40,40)
redoRect = Rect(155,652,40,40)

#################################

## identifying all rects for backgrounds
backrects = [Rect(20,250,165,30), Rect(20,290,165,30), Rect(20,210,165,30), Rect(20,330,165,30), Rect(20,450,165,30), Rect(20,410,165,30), Rect(20,170,165,30), Rect(20,490,165,30), Rect(20,370,165,30), Rect(20,530,165,30)]

##############################################

## transforming all background texts

# back01T = transform.scale(back01,(165,30))
# back02T = transform.scale(back02,(165,20))
# back03T = transform.scale(back03,(165,20))
# back04T = transform.scale(back04,(165,20))
# back05T = transform.scale(back05,(165,20))
# back06T = transform.scale(back06,(165,20))
# back07T = transform.scale(back07,(165,25))
# back08T = transform.scale(back08,(165,30))
# back09T = transform.scale(back09,(165,25))

###########################################

## transforming - scaling images

dragonT=transform.scale(dragonball,(1080,720)) ## scaling the background
wheelT=transform.scale(wheelPic,(202,99))
pencilT=transform.scale(pencilPic,(40,40))
eraserT=transform.scale(eraserPic,(40,40))
circleT = transform.scale(circlePic,(35,35))
stampT = transform.scale(stampPic,(40,40))
sprayT = transform.scale(sprayPic,(40,40))
colourT = transform.scale(colourPic,(40,40))
loadT = transform.scale(loadIcon,(40,40))
saveT = transform.scale(saveIcon,(40,40))
backT = transform.scale(backIcon,(40,40))
textT = transform.scale(textPic,(40,40))
paintT = transform.scale(paint_brushPic,(40,40))
markerT = transform.scale(markerPic,(40,40))
UndoPic = transform.scale(Undo,(40,40))
RedoPic = transform.scale(Redo,(40,40))

########################################## Transforming the stamp pics only 

### page 0

gokuT = transform.scale(gokuPic,(217,228))
goku_ssgT = transform.scale(goku_ssgPic,(128,211))
goku_ultraT = transform.scale(goku_ultraPic,(192,135))

### page 1 

jerinT = transform.scale(jerinPic,(144,240))
gohanT = transform.scale(gohanPic,(117,170))
beerusT = transform.scale(beerusPic,(128,218))

### page 2 

keflaT = transform.scale(keflaPic,(116,155))
vegetaT = transform.scale(vegetabPic,(132,203))
black_zamT = transform.scale(black_zamasu,(125,252))

### page 3

goku_roseT = transform.scale(goku_rose,(128,235))
goku_blackT = transform.scale(goku_blackPic,(118,187))
golden_frezaT = transform.scale(golden_frezaPic,(119,160))

############################################

## Blitting all tools and canvas

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
screen.blit(pencilT,pencilRect)
screen.blit(eraserT,eraserRect)
screen.blit(stampT,stampRect)
screen.blit(circleT,Rect(262,607,35,35))
draw.rect(screen,BLACK,Rect(315,615,30,20),1)
draw.line(screen,BLACK,(315,655),(345,685),1)
draw.ellipse(screen,BLACK,[365,660,32,20],1)
screen.blit(sprayT,sprayRect)
screen.blit(backT,backRect)
screen.blit(colourT,colourRect)
screen.blit(textT,textRect)
screen.blit(paintT,paintRect)
screen.blit(markerT,markerRect)
draw.rect(screen,BLACK,Rect(591,605,84,44),0)
screen.blit(loadT,loadRect)
screen.blit(saveT,saveRect)
screen.blit(UndoPic,undoRect)
screen.blit(RedoPic,redoRect)
draw.rect(screen,BLACK,undoRect,2)
draw.rect(screen,BLACK,redoRect,2)

###############################

## identifying all the rects for stamps only

### page 0

gokuRect = Rect(50,155,100,100)
goku_ultraRect = Rect(50,295,100,100)
goku_ssgRect = Rect(50,420,100,100)

### page 1

jerinRect = Rect(50,155,100,100)
gohanRect = Rect(50,295,100,100)
beerusRect = Rect(50,420,100,100)

### page 2

kelfaRect = Rect(50,155,100,100)
vegetaRect = Rect(50,295,100,100)
black_zamusRect = Rect(50,420,100,100)

### page 3

goku_roseRect = Rect(50,155,100,100)
goldenfrezaRect = Rect(50,295,100,100)
goku_blackRect = Rect(50,420,100,100)

## up down arrows

upArrowRect = Rect(15,125,170,25)
downArrowRect = Rect(15,540,170,25)

##############################################

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
                
            if evt.key==K_RIGHT and tool == "eraser":
                eradius+=5

            elif evt.key==K_LEFT and tool == "eraser":
                eradius-=5

        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                if canvasRect.collidepoint((mx, my)):
                    undo.append(canvas.copy())

            if evt.button == 1 and undoRect.collidepoint(mx,my):
                if len(undo) > 1:
                    redo.append(undo.pop())
                    canvas.blit(undo[-1], (0,0))

            if evt.button == 1 and redoRect.collidepoint(mx,my):
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

    # print(mx,my)## to calculate the x and y of anthing if needed (helpful)

    mb=mouse.get_pressed() ## shorter version of the mouse button check
    #################################### selecting the tools

    ################### rectangle for tools

    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,stampRect,2)
    draw.rect(screen,GREEN,circleRect,2)
    draw.rect(screen,GREEN,rectangleRect,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,ellipseRect,2)
    draw.rect(screen,GREEN,sprayRect,2)
    draw.rect(screen,GREEN,backRect,2)
    draw.rect(screen,GREEN,colourRect,2)
    draw.rect(screen,GREEN,textRect,2)
    draw.rect(screen,GREEN,paintRect,2)
    draw.rect(screen,GREEN,markerRect,2)

    #################################### all extra tools for choice 1 

    if tool == "background" and page == 0:
        draw.rect(screen,BLACK,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        screen.blit(rotPic,(20,130))

        
        for d in range(10):
            screen.blit(texts[d], backrects[d])
            draw.rect(screen,BLACK,backrects[d],2)

        # screen.blit(back01T,backrects[0])
        # screen.blit(back02T,backrects[1])
        # screen.blit(back03T,backrects[2])
        # screen.blit(back04T,backrects[3])
        # screen.blit(back05T,backrects[4])
        # screen.blit(back06T,backrects[5])
        # screen.blit(back07T,backrects[6])
        # screen.blit(back08T,backrects[7])
        # screen.blit(back09T,backrects[8])

        # draw.rect(screen,BLACK,backrects[0],2)
        # draw.rect(screen,BLACK,backrects[1],2)
        # draw.rect(screen,BLACK,backrects[2],2)
        # draw.rect(screen,BLACK,backrects[3],2)
        # draw.rect(screen,BLACK,backrects[4],2)
        # draw.rect(screen,BLACK,backrects[5],2)
        # draw.rect(screen,BLACK,backrects[6],2)
        # draw.rect(screen,BLACK,backrects[7],2)
        # draw.rect(screen,BLACK,backrects[8],2)

    elif tool == "pencil":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        ##draw.rect(screen,GREEN,

    elif tool == "eraser":

        draw.rect(screen,GREEN,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "stamp" and page ==0:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(gokuIcon,gokuRect)
        draw.rect(screen,BLACK,gokuRect,2)
        screen.blit(goku_ultraIcon,goku_ultraRect)
        draw.rect(screen,BLACK,goku_ultraRect,2)
        screen.blit(goku_ssgIcon,goku_ssgRect)
        draw.rect(screen,BLACK,goku_ssgRect,2)     
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page==1:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(jerinIcon,jerinRect)
        draw.rect(screen,BLACK,jerinRect,2)   
        screen.blit(gohanIcon,gohanRect)
        draw.rect(screen,BLACK,gohanRect,2)
        screen.blit(beerusIcon,beerusRect)
        draw.rect(screen,BLACK,beerusRect,2)       

        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page== 2:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        screen.blit(keflaIcon,kelfaRect)
        draw.rect(screen,BLACK,kelfaRect,2)

        screen.blit(vegetaIcon,vegetaRect)
        draw.rect(screen,BLACK,vegetaRect,2)

        screen.blit(blackzamausIcon,black_zamusRect)
        draw.rect(screen,BLACK,black_zamusRect,2)
        
        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page==3:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        
        screen.blit(gokuroseIcon,goku_roseRect)
        draw.rect(screen,BLACK,goku_roseRect,2)
        
        screen.blit(golden_frezaIcon,goldenfrezaRect)
        draw.rect(screen,BLACK,goldenfrezaRect,2)
        
        screen.blit(goku_black,goku_blackRect)
        draw.rect(screen,BLACK,goku_blackRect,2)
        
        screen.blit(upArrowPic,upArrowRect)

    elif tool == "circle":

        draw.rect(screen,YELLOW,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "rectangle":

        draw.rect(screen,PURPLE,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "line":

        draw.rect(screen,MEGENTA,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "spraypaint":

        draw.rect(screen,LIGHTBLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "ellipse":

        draw.rect(screen,GREEN_YELLOW,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "colour_picker":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "text":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "paint":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "marker":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    ##################### changing the color
    
    if tool == "pencil":
        draw.rect(screen,RED,pencilRect,2)

    elif tool == "eraser":
        draw.rect(screen,RED,eraserRect,2)

    elif tool == "stamp":
        draw.rect(screen,RED,stampRect,2)

    elif tool == "circle":
        draw.rect(screen,RED,circleRect,2)

    elif tool == "rectangle":
        draw.rect(screen,RED,rectangleRect,2)

    elif tool == "line":
        draw.rect(screen,RED,lineRect,2)

    elif tool == "ellipse":
        draw.rect(screen,RED,ellipseRect,2)

    elif tool == "spraypaint":
        draw.rect(screen,RED,sprayRect,2)

    elif tool == "background":
        draw.rect(screen,RED,backRect,2)

    elif tool == "colour_picker":
        draw.rect(screen,RED,colourRect,2)

    elif tool == "text":
        draw.rect(screen,RED,textRect,2)

    elif tool == "paint":
        draw.rect(screen,RED,paintRect,2)

    elif tool == "marker":
        draw.rect(screen,RED,markerRect,2)
        
##################################################

    if page == 0:

        if stamp == "gokub" and tool == "stamp":
            draw.rect(screen,RED,gokuRect,2)

        if stamp == "goku_u" and tool == "stamp":
            draw.rect(screen,RED,goku_ultraRect,2)

        if stamp == "goku_ssg" and tool == "stamp":
            draw.rect(screen,RED,goku_ssgRect,2)

        if tool == "background":
            for e in range(10):
                if backrects[e].collidepoint(mx,my):
                    draw.rect(screen,RED,backrects[e],3)    
    if page ==1:

        if stamp == "jerin" and tool == "stamp":
             draw.rect(screen,RED,jerinRect,2)

        if stamp == "gohan" and tool == "stamp":
             draw.rect(screen,RED,gohanRect,2)

        if stamp == "beerus" and tool == "stamp":
             draw.rect(screen,RED,beerusRect,2)

    if page ==2:

        if stamp == "kelfa" and tool == "stamp":
             draw.rect(screen,RED,keflaRect,2)

        if stamp == "vegeta" and tool == "stamp":
             draw.rect(screen,RED,vegetaRect,2)

        if stamp == "black_zamaus" and tool == "stamp":
             draw.rect(screen,RED,black_zamusRect,2)

    if page ==3:

        if stamp == "goku_rose" and tool == "stamp":
             draw.rect(screen,RED,goku_roseRect,2)

        if stamp == "goldenFreza" and tool == "stamp":
             draw.rect(screen,RED,goldenfrezaRect,2)

        if stamp == "goku_black" and tool == "stamp":
             draw.rect(screen,RED,goku_blackRect,2)
    

    if mb[0]==1: ## Checking left click

        if pencilRect.collidepoint(mx,my): ## check if the pencil rectangle is clicked (Note: the rectangle is there but you cant see it you can only see the picture 
            tool="pencil" ## set tool to pencil

        elif eraserRect.collidepoint(mx,my): ## same as pencil
            tool="eraser" ## set tool to eraser

        elif stampRect.collidepoint(mx,my):
            tool = "stamp"
            page = 0
            stamp = "nothing"

        elif circleRect.collidepoint(mx,my):
            tool = "circle"

        elif rectangleRect.collidepoint(mx,my):
            tool = "rectangle"

        elif lineRect.collidepoint(mx,my):
            tool = "line"

        elif ellipseRect.collidepoint(mx,my):
            tool = "ellipse"
            
        elif sprayRect.collidepoint(mx,my):
            tool = "spraypaint"

        elif backRect.collidepoint(mx,my):
            tool = "background"
            page = 0

        elif colourRect.collidepoint(mx,my):
            tool = "colour_picker"
            RC = (rred,rgreen,rblue)

        elif textRect.collidepoint(mx,my):
            tool = "text"
            RC = (rred,rgreen,rblue)

        elif paintRect.collidepoint(mx,my):
            tool = "paint"
            RC = (rred,rgreen,rblue)

        elif markerRect.collidepoint(mx,my):
            tool = "marker"
            RC = (rred,rgreen,rblue)

    ##using the tools

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

            if gokuRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "gokub"

            if stamp == "gokub" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(gokuT,(mx-59,my-79))

            elif goku_ultraRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_u"

            if stamp == "goku_u" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_ultraT,(mx-64,my-25))

            elif goku_ssgRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_ssg"

            if stamp == "goku_ssg" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_ssgT,(mx-64,my-105))

        if page == 1:

            if jerinRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "jerin"

            if stamp == "jerin" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(jerinT,(mx-72,my-120))
               
            if gohanRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "gohan"

            if stamp == "gohan" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(gohanT,(mx-50,my-60))

            if beerusRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "beerus"

            if stamp == "beerus" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(beerusT,(mx-64,my-109))

        if page == 2:

            if kelfaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "kefla"

            if stamp == "kefla" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(keflaT,(mx-58,my-77))
                
            if vegetaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "vegeta"

            if stamp == "vegeta" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(vegetaT,(mx-66,my-101))

            if black_zamusRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "black_zamaus"

            if stamp == "black_zamaus" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(black_zamT,(mx-62,my-126))
                
        if page == 3:

            if goku_roseRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_rose"

            if stamp == "goku_rose" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_roseT,(mx-64,my-117))
                
            if goku_blackRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_black"

            if stamp == "goku_black" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_blackT,(mx-75,my-93))

            if goldenfrezaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goldenFreza"

            if stamp == "goldenFreza" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(golden_frezaT,(mx-59,my-80))

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


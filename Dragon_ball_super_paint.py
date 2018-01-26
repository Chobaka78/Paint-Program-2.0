#basicPaint.py

from pygame import *
from random import*
from tkinter import*
from math import*

root=Tk()
root.withdraw() ## removes the extra TK window

init() ## This is for the pygame
font.init() ## This is for fonts 

size1=(1080,720) # The screen size
screen = display.set_mode(size1) # The screen as a suface

## Fonts

comicFont = font.SysFont("Saiyan-Sans",26) ## this is the font used for the texts
displayText = comicFont.render("Backgrounds",True,(0,0,0)) #
rotPic = displayText

## other variables
page = 0 ## this is the page variable for multiple pages
stamp = "no stamp" ## this tells the computer what stamp is currently chosen
background = "nothing" ## this tells the computer what background is currently chosen
size = 10 ## default size for tools is 10
music_choice = "false" ## this is a varible that helps with the playing and pausing of music 
fill = "not filled" ## this is a varible that tells the user if the tool if fille or unfilled
pos = 9 ## this is the pos for the eraser tool on a background

##  All the Colours

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

####################################################
## MUSIC
music = ["music/Dragonballsuper.wav","music/BeerusMadness.wav", "music/Ultra Instinct Reborn.wav", ## list of all the songs
"music/Time To Strike Back.wav", "music/Frieza is Resurrected.wav", "music/Genki Dama Theme.mp3",
"music/Dragon Ball Super1.mp3", "music/The Birth of a God.mp3", "music/Friezas Secret Plan.mp3"]
b = 0 ## this is the index of music helps with selecting songs
mixer.music.load(music[b])
mixer.music.play()
########################################################

## EVERYTHING FOR REGULAR IMAGES
########################################################

## Loading all regular 

dragonball = image.load("images/Dragonballback.png") ## back ground (put images/"name") this indicates it's in images folder
wheelPic = image.load("images/colwheel.jpg") ## colour picking 
upArrowPic = image.load("images/up arrow.png") ## up arrow for changing the page
downArrowPic = image.load("images/down arrow.png") ## down arrow for changing the page
loadIcon = image.load("images/icons/load.png")
saveIcon = image.load("images/icons/save.jpg")
backIcon = image.load("images/icons/back_button.png")
prevPic = image.load("images/prevous.png")
playPic = image.load("images/play and pause.png")
nextPic = image.load("images/next.png")
icon = image.load("images/dbs_logo.png") ## this is for the little logo on top left corner 
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
prevRect = Rect(510,655,40,40)
playRect = Rect(560,655,40,40)
nextRect = Rect(610,655,40,40)
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
"images/icons/back_button.png", "images/colour_picker tool.png", "images/paintbucket.png", 
"images/paintbrush.png", "images/marker_tool.png", "images/Undo.png", "images/Redo.png", "images/lineTool.png",
"images/clear.png"]

tool_image = [] ## this is the tools images list

for i in toolimg:
    iPic = image.load(i)
    tool_image.append(iPic)

toolRects = [ Rect(210,650,40,40), Rect(210,605,40,40), Rect(260,650,40,40), 
Rect(260,605,40,40), Rect(310,605,40,40), Rect(360,605,40,40), Rect(410,605,40,40), 
Rect(460,605,40,40), Rect(460,650,40,40), Rect(360,650,40,40), Rect(410,650,40,40), 
Rect(105,652,40,40), Rect(155,652,40,40), Rect(310,650,40,40), Rect(510,605,40,40)]


tool_list = ["eraser", "pencil", "stamp", "ellipse", "rectangle", 
"spraypaint", "background", "colour_picker", "paintbucket", "paint", 
"marker", "undo", "redo", "line","clear"]
#########################################################

## EVERYTHING FOR STAMPS

## load all stamps

stampimg = ["images/Choice 1/goku_ssgss.png", "images/Choice 1/goku ultra instinct.png", 
"images/Choice 1/goku ssg.png", "images/Choice 1/Jiren.png","images/Choice 1/gohan.png", 
"images/Choice 1/beerus.png","images/Choice 1/Kefla.png", "images/Choice 1/vegeta blue.png",
"images/Choice 1/black x zamsu.png", "images/Choice 1/Goku_Black rose.png", 
"images/Choice 1/golden freza.png", "images/Choice 1/Goku_Black.png",
"images/Choice 1/Champa.png", "images/Choice 1/gotenks.png", "images/Choice 1/Hit.png",
"images/Choice 1/King_kai.png", "images/Choice 1/trunks.png", "images/Choice 1/vegito.png"]


stamp_image = [] ## this is the stamps list for the stamps

for a in stampimg:
    stamp_img = image.load(a)
    stamp_image.append(stamp_img)

stamp_list = ["gokub", "goku_u", "goku_ssg", "jerin", 
"gohan", "beerus", "kefla", "vegeta", "black_zamaus", 
"goku_rose", "goku_black", "goldenFreza", "champa", "gotenks",
"hit", "kinkai", "trunks", "vegito"]


##############################################

# Transforming stamps
w = [217, 192, 128, 144, 117, 128, 116, 132, 125, 128, 118, 119, 85,
70, 106, 105, 102, 101] ## all the widths of the stamps resized 

h = [228, 135, 211, 240, 170, 218, 155, 203, 252, 235, 187, 160, 159,
114, 142, 128, 75, 218] ## all the heights of the stamps resized

stamps_image = [] ## the stamps image list for stamps after transforming them

for s in range(18):
    stampI = transform.scale(stamp_image[s],(w[s],h[s]))
    stamps_image.append(stampI)

stampIcon = ["images/icons/goku icon.png", "images/icons/goku ultra.png", "images/icons/goku ssg.png",
"images/icons/jerin.png", "images/icons/gohanicon.png","images/icons/beerus.jpg",
"images/icons/kefla.png", "images/icons/vegeta.png", "images/icons/merged icon.png",
"images/icons/roseicon.png", "images/icons/golden freza.png", "images/icons/goku black.png",
"images/icons/champa.png", "images/icons/gotenks.png", "images/icons/hit.png",
"images/icons/King_kai.png", "images/icons/trunks.png", "images/icons/vegito.png"]

stamp_icon = [] ## list for stamp icons

for j in stampIcon:
    stampicons = image.load(j)
    stamp_icon.append(stampicons)

################################################

## Stamp Rects

stampRect = [Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100),
Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100), Rect(50,155,100,100),
Rect(50,295,100,100), Rect(50,420,100,100), Rect(50,155,100,100), Rect(50,295,100,100),
Rect(50,420,100,100), Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100),
Rect(50,155,100,100), Rect(50,295,100,100), Rect(50,420,100,100)]

#########################################################

## EVERYTHING FOR Backgrounds

## Loaing backround images

backtext = ["images/back/page04.png", "images/back/page05.png", 
"images/back/page03.png", "images/back/page06.png", 
"images/back/page09.png", "images/back/page08.png", "images/back/page02.png", 
"images/back/page10.png", "images/back/page07.png", "images/back/Whiteback.png",]

texts = [] ## this is the list for the background texts

for s in backtext:
    im = image.load(s)
    texts.append(im)

backimage = ["images/Background/beerus_planet.jpg", "images/Background/boat_place.jpg", 
"images/Background/Kame_house.png", "images/Background/king_kai.jpg", "images/Background/nameless planet_stage.png", 
"images/Background/nameless_planet.png", "images/Background/stage tournment of power.png", "images/Background/super_dragon.png", 
"images/Background/tower.jpg", "images/Background/whiteback.jpg",]

textures = [] ## this is the list for the backgrounds 

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
### LOADING ALL THE FONT IMAGES
FontsPics = ["images/FontPics/eraserFont.png", "images/FontPics/pencilFont.png", "images/FontPics/stampFont.png", "images/FontPics/ellipseFont.png",
"images/FontPics/rectFont.png", "images/FontPics/sprayFont.png", "images/FontPics/backgroundFont.png", "images/FontPics/colourpickerFont.png",
"images/FontPics/paintbucketFont.png", "images/FontPics/paintbrushFont.png", "images/FontPics/markerFont.png", "images/FontPics/undoFont.png",
"images/FontPics/redoFont.png", "images/FontPics/lineFont.png", "images/FontPics/clearFont.png"]

mainFont = image.load("images/FontPics/mainFont.png")
loadFont = image.load("images/FontPics/loadFont.png")
saveFont = image.load("images/FontPics/saveFont.png")

Fonts = [] ## this is the list for the font pics

for i in FontsPics:
    fontpic = image.load(i)
    Fonts.append(fontpic)

################################################
#SELECTED FONTS
eraser_sFont = image.load("images/SelectFont/eraserfont.png")
pencil_sFont = image.load("images/SelectFont/pencilfont.png")
spray_sFont = image.load("images/SelectFont/sprayfont.png")
marker_sFont = image.load("images/SelectFont/markerfont.png")
ellipse_sFont = image.load("images/SelectFont/ellipsefont.png")
rect_sFont = image.load("images/SelectFont/rectfont.png")
paintb_sFont = image.load("images/SelectFont/paintbucketfont.png")
paint_sFont = image.load("images/SelectFont/paintfont.png")
colourP_sFont = image.load("images/SelectFont/colourpickerfont.png")
line_sFont = image.load("images/SelectFont/linefont.png")
clear_sFont = image.load("images/SelectFont/clearfont.png")

unfill_sFont = image.load("images/SelectFont/unfillfont.png")
fill_sFont = image.load("images/SelectFont/filledfont.png")

sizesd = ["images/SelectFont/smallfont.png", "images/SelectFont/mediumfont.png", "images/SelectFont/large.png",
"images/SelectFont/extralargefont.png"]

sizeOp = [] ## this is the size list for default sizes

for h in sizesd:
    sizeP = image.load(h)
    sizeOp.append(sizeP)

############################################
## RECTS FOR FONTS / SELECTED FONTS
mainFont_Rect = Rect(15,130,165,420)
sfontRect = Rect(15,430,154,120)
unfillRect = Rect(25,390,55,30)
fillRect = Rect(100,390,55,30)

adjustRect =[Rect(25,140,165,50),Rect(25,215,165,50), Rect(25,290,165,50), Rect(25,360,165,50)] ## all the rects for the sizes


#############################################################

## Default variables

col=BLACK #default colour is black
bcol = WHITE ## default colour for background
tool = "nothing" ## default tool is nothing 
display.set_caption("Dragon ball super Paint") ## for displaying dragon ball super paint in top left hand corner
display.set_icon(icon) ## setiting the picture on top left corner

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
draw.circle(screen,GREEN,(530,675),20,2)
draw.circle(screen,GREEN,(580,675),20,2)
draw.circle(screen,GREEN,(630,675),20,2)

for i in range(15):

    screen.blit(tool_image[i], toolRects[i]) ## blitting all the tools

#################################
##Blitting regular fonts
screen.blit(mainFont,mainFont_Rect) ## blitting the intro font

###################################################

running = True
canvas_copy = screen.subsurface(canvasRect).copy() ## subsurface used for undo redo taking screenshot
canvas = screen.subsurface(canvasRect) ## subsurface for undo redo
undo=[canvas_copy] ## undo list with original copy of canvas
redo = [] ## empty redo list
##textbox = screen.subsurface()

while running:
    mx,my=mouse.get_pos() ## get the mx 
    click = False ## for 1 step programs
    draw.rect(screen,col,show_colourrect,0) ## this is the rectangle that shows the current colour 
  
    ## Random colours
    rred = randint(0,255) ## random colours 
    rgreen = randint(0,255) ## random colours 
    rblue = randint(0,255) ## random colours 
        
    for evt in event.get():
        
        if evt.type == QUIT:            
            running = False    
                
        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                if canvasRect.collidepoint((mx, my)): ## undo function
                    undo.append(canvas.copy()) ## screen shot

            if evt.button == 1 and toolRects[11].collidepoint(mx,my):
                if len(undo) > 1:
                    redo.append(undo.pop())
                    canvas.blit(undo[-1], (0,0))

            if evt.button == 1 and toolRects[12].collidepoint(mx,my): ## redo function
                if len(redo) > 0:
                    undo.append(redo.pop()) 
                    canvas.blit(undo[-1], (0,0))

        if evt.type == MOUSEBUTTONDOWN:

            click = True
            sx,sy = evt.pos

            if evt.button == 1 and nextRect.collidepoint(mx,my) and b <= len(music): ## music function where all the play and pause is done
                b = b+1

                try:
                    mixer.music.load(music[b])

                except:
                    b-=1
                    mixer.music.load(music[b])
                mixer.music.play(-1)


            if evt.button == 1 and prevRect.collidepoint(mx,my) and b<=len(music):
                if b >=0:
                    b-=1
                    if b == -1:
                        b+=1

                mixer.music.load(music[b])
                mixer.music.play(-1)

            if evt.button == 1 and playRect.collidepoint(mx,my) and music_choice == "false": ## check if play is clicked and the choice is false
                mixer.music.pause() ## pause music
                music_choice = "true" ## se it to true so it can be clicked agaon

            elif evt.button == 1 and playRect.collidepoint(mx,my) and music_choice == "true": ## check if play is clicked and choice is true
                mixer.music.unpause() ## play from the point where paused 
                music_choice = "false" ## set it to false

            if evt.button == 1:
                canvas.copy() ## take screen shot of the canvas only 

            if evt.button == 5: # scrolling down

               if size>0:
                size-=1

            if evt.button == 4: ## scrolling up
                size+=1

            background = screen.copy() ## taking a screen shot of the screen

    mb=mouse.get_pressed() ## shorter version of the mouse button check

###################################################################
## THIS IS THE TEXT FOR LEETING THE USER KNOW THEIR POS AND THE CURRENT SIZE 
##########################################################################  
    posText = comicFont.render("Pos:",True,(66,223,244))
    xposText = comicFont.render("X=",True,(255,0,0))
    yposText = comicFont.render("Y=",True,(255,0,0))
    xText = comicFont.render(str(mx),True,(0,0,0))
    comaText = comicFont.render(",",True,(0,0,0))
    yText = comicFont.render(str(my),True,(0,0,0))
    sizetext  = comicFont.render("Size:",True,(66,223,244))
    sizeText = comicFont.render(str(size),True,(0,0,0))

    posPic = posText
    XposPic = xposText
    yposPic = yposText
    xPic = xText
    comaPic = comaText
    yPic = yText
    sizePic = sizetext
    sizepic = sizeText

    draw.rect(screen,(255,126,0),Rect(200,576,700,20),0)
    screen.blit(posPic,(206,575))
    screen.blit(XposPic, (256,575))
    screen.blit(xPic, (296,575))
    screen.blit(yposPic, (351,575))
    screen.blit(yPic, (391,575))
    screen.blit(sizePic, (700,575))
    screen.blit(sizepic, (755,575))

#################################################################

## ALL EFFECTS FOR TOOLS
#################################################
    for u in range(15):
        draw.rect(screen,GREEN,toolRects[u],2)
        draw.rect(screen,BLACK,toolRects[11],2)
        draw.rect(screen,BLACK,toolRects[12],2)

    for i in range(15):

        if tool == tool_list[i]:
            draw.rect(screen,BLACK,screB_Rect)
            draw.rect(screen,WHITE,screRect)

    for d in range(15):
        if tool == tool_list[d]:
            draw.rect(screen,RED,toolRects[d],2)

    if prevRect.collidepoint(mx,my):
        draw.circle(screen,BLUE,(530,675),20,3)

    else:
        draw.circle(screen,GREEN,(530,675),20,2)

    if playRect.collidepoint(mx,my):
        draw.circle(screen,BLUE,(580,675),20,3)

    else:
        draw.circle(screen,GREEN,(580,675),20,2)

    if nextRect.collidepoint(mx,my):
        draw.circle(screen,BLUE,(630,675),20,3)

    else:
        draw.circle(screen,GREEN,(630,675),20,2)

    screen.set_clip(None)
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
## THESE ARE SOME EFFECTS FOR WHEN A TOOL IS SELECTED
########################################################
    elif tool == "pencil":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(pencil_sFont, sfontRect)

#########################################################
    elif tool == "eraser":
        draw.rect(screen,GREEN,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(eraser_sFont, sfontRect)
        for i in range(3):
            screen.blit(sizeOp[i], adjustRect[i])

        for f in range(3):
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

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
        screen.blit(downArrowPic,downArrowRect)

#######################################################
    elif tool == "stamp" and page==4:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for e in range(12,15):
            screen.blit(stamp_icon[e], stampRect[e])
            draw.rect(screen,BLACK,stampRect[e],2)

            if stampRect[e].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[e],3)

        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)

########################################################
    elif tool == "stamp" and page==5:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        for e in range(15,18):
            screen.blit(stamp_icon[e], stampRect[e])
            draw.rect(screen,BLACK,stampRect[e],2)

            if stampRect[e].collidepoint(mx,my):
                draw.rect(screen,BLUE,stampRect[e],3)

        screen.blit(upArrowPic,upArrowRect)

########################################################
    elif tool == "marker":
        draw.rect(screen,BLACK,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(marker_sFont, sfontRect)
        for f in range(4):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)
##########################################################
    elif tool == "spraypaint":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(spray_sFont, sfontRect)

        for f in range(4):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

#########################################################
    elif tool == "ellipse":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(ellipse_sFont, sfontRect)
        screen.blit(unfill_sFont, unfillRect)
        screen.blit(fill_sFont, fillRect)
        draw.rect(screen,BLACK,fillRect,2)
        draw.rect(screen,BLACK,unfillRect,2)

        if unfillRect.collidepoint(mx,my):
            draw.rect(screen,BLUE,unfillRect,2)

        elif fillRect.collidepoint(mx,my):
            draw.rect(screen,BLUE,fillRect,2)

        if evt.type == 1 and unfillRect.collidepoint(mx,my):
            fill = "not filled"

        elif evt.type == 1 and fillRect.collidepoint(mx,my):
            fill = "filled"

        for f in range(3):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

####################################################################
    elif tool == "rectangle":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(rect_sFont, sfontRect)
        screen.blit(unfill_sFont, unfillRect)
        screen.blit(fill_sFont, fillRect)
        draw.rect(screen,BLACK,fillRect,2)
        draw.rect(screen,BLACK,unfillRect,2)

        if unfillRect.collidepoint(mx,my):
            draw.rect(screen,BLUE,unfillRect,2)

        elif fillRect.collidepoint(mx,my):
            draw.rect(screen,BLUE,fillRect,2)

        if evt.type == 1 and unfillRect.collidepoint(mx,my):
            fill = "not filled"

        elif evt.type == 1 and fillRect.collidepoint(mx,my):
            fill = "filled"

        for f in range(3):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

#####################################################################3
    elif tool == "paintbucket":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(paintb_sFont, sfontRect)

    elif tool == "colour_picker":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(colourP_sFont, sfontRect)

    elif tool == "paint":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(paint_sFont, sfontRect)

        for f in range(4):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

    elif tool == "line":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(line_sFont, sfontRect)

        for f in range(4):
            screen.blit(sizeOp[f], adjustRect[f])
            if adjustRect[f].collidepoint(mx,my):
                draw.rect(screen,BLUE,adjustRect[f],2)

    elif tool == "clear":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(clear_sFont, sfontRect)

#########################################################
## THESE ARE THE EFFECTS FOR THE STAMPS LIKE SELECTING
#########################################################
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
########################################################
    elif page == 4:
        for i in range(12, 15):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)
########################################################
    elif page == 5:
        for i in range(15, 18):
            if stamp == stamp_list[i] and tool == "stamp":
                draw.rect(screen,RED,stampRect[i],2)

    screen.set_clip(None)

############################################################
    if mb[0]==1: ## Checking left click

        for m in range(15):

            if toolRects[m].collidepoint(mx,my):
                if click:
                        tool = tool_list[m]

            if toolRects[3].collidepoint(mx,my):
                stamp = "nothing"
                page = 0

        if tool == "colour_picker" or "text" or "paint" or "marker":
            RC = (rred,rgreen,rblue) ## having a random colored border everytime you click 

        if tool == "background":
            page = 0

########################################################################
### THIS IS CHECKING IF THE UNFILL OR FILL BUTTON IS CLICKED FOR RECTANLGE AND ELLIPSE
#######################################################################
        if unfillRect.collidepoint(mx,my) and tool == "rectangle":
            fill = "not filled"

        elif fillRect.collidepoint(mx,my) and tool == "rectangle":
            fill = "filled"

        if unfillRect.collidepoint(mx,my) and tool == "ellipse":
            fill = "not filled"

        elif fillRect.collidepoint(mx,my) and tool == "ellipse":
            fill = "filled"

        for i in range(4):
            if adjustRect[i].collidepoint(mx,my):
                size = 10*i+10
###################################################################################
##USING THE TOOLS 
#######################################################################
    if mb[0]==1: ## if left click

        if page ==0 and tool == "background":

            for k in range(10): ## Blitting all the images for the backgrounds
                if backrects[k].collidepoint(mx,my):
                   screen.blit(textures[k], canvasRect)
                   pos = k

        if canvasRect.collidepoint(mx,my): ## make sure all the lines stay within the canvas
            screen.set_clip(canvasRect) ## only the canvas can be updated


            if tool=="pencil": ## if the tool selected is a pencil
                draw.line(screen,col,(omx,omy),(mx,my),3) ## draw lines with a thick ness of 3

            elif tool=="eraser": ## if tool is eraser
                try:
                    sample = (textures[pos].subsurface((mx-206,my-122,size,size))) ## taking the exact location of the background
                    screen.blit(sample, (mx,my))

                except:
                    pass


            elif tool == "circle": ## if the tool is circle
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.circle(screen,col,(sx,sy),size,2)

            elif tool == "rectangle" and fill == "not filled":            
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                distx = mx-sx ## change in distance in the x
                disty = my-sy ## change in distance in the y

                if size%2 == 0:
                    size+=1

                draw.rect(screen,col,Rect(sx,sy,distx,disty),size)
                ### ADDING 4 SQUARES TO THE ENDS OF THE RECTANGLE TO GET 90 DEGREE CORNERS

                draw.rect(screen,col,Rect(sx-(size/2)+1,sy-(size/2)+1,size,size),0)
                draw.rect(screen,col,Rect((sx+distx)-(size/2)-(1/2),sy-(size/2)+1,size,size),0)
                draw.rect(screen,col,Rect(sx-(size/2)+1,(sy+disty)-(size/2)-(1/2),size,size),0)
                draw.rect(screen,col,Rect((sx+distx)-(size/2),(sy+disty)-(size/2),size,size),0)

            elif tool == "rectangle" and fill == "filled":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                distx = mx-sx
                disty = my-sy

                draw.rect(screen,col,Rect(sx,sy,distx,disty),0)
            

            elif tool == "ellipse" and fill == "not filled":             
                screen.fill((0,0,0))
                screen.blit(background,(0,0))

                distanceX = (mx-sx)
                distanceY = (my-sy)

                try:
                    for i in range(4): ## DRAWING FOR SEPERATE ELIPPSE MOVED UP i DOWN i LEFT i RIGHT i IN A LOOP 3 TIMES
                        ellRect = Rect(sx+i,sy,distanceX,distanceY)
                        ellRect = Rect(sx-i,sy,distanceX,distanceY)
                        ellRect = Rect(sx,sy+i,distanceX,distanceY)
                        ellRect = Rect(sx,sy-i,distanceX,distanceY)
                        ellRect.normalize()      

                        draw.ellipse(screen,col,ellRect,size)

                except:
                    pass

            elif tool == "ellipse" and fill == "filled": ### DRAWING THE FILLED ELLIPSE TOOL 
                screen.fill((0,0,0))
                screen.blit(background,(0,0))

                distanceX = (mx-sx)
                distanceY = (my-sy)

                try: 
                        ellRect = Rect(sx,sy,distanceX,distanceY)
                        ellRect.normalize() 
                        draw.ellipse(screen,col,ellRect,0)


                except:
                    pass


            elif tool == "line":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                dx, dy=((mx-sx), (my-sy))
                distance = max(hypot(dx, dy), 1)
                angles = atan2(dy,dx)
                drx, dry = cos(angles), sin(angles)
                
                for v in range(round(distance)):
                    draw.circle(screen,col,((sx+round(drx*v)),sy+round(dry*v)),size)

            elif tool == "colour_picker":

                if canvasRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
                    col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)

            elif tool == "spraypaint":

                screen.set_clip(canvasRect)
                if canvasRect.collidepoint(mx,my):
                    for i in range (30):
                        dx = randint(-size,size)
                        dy = randint(-size,size)
                        if hypot(dx,dy) <=size:
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

            elif tool == "paintbucket":
                if mb[0]==1:
                    pixelpos = [(mx,my)]
                    pixel = screen.get_at((mx,my))
                    if pixel!=col:
                        while len(pixelpos)>0:#continously loops until all pixels are the same colour
                            if canvasRect.collidepoint(pixelpos[0]) and screen.get_at(pixelpos[0])== pixel:
                                screen.set_at(pixelpos[0],col)
                                pixelpos.append((pixelpos[0][0],pixelpos[0][1]+1))  #Adds four surrounding pixels to the list
                                pixelpos.append((pixelpos[0][0],pixelpos[0][1]-1))
                                pixelpos.append((pixelpos[0][0]+1,pixelpos[0][1]))
                                pixelpos.append((pixelpos[0][0]-1,pixelpos[0][1]))
                            del(pixelpos[0])


############################################################ 

## THESE ARE THE PAGES FROM 0 TO 5 AND THE STAMPS BEING BLITTED ON THE SCREEN

        if page ==0:

            for g in range(0, 3):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))


        if page == 1:

            for g in range(3, 6):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))


        elif page == 2:

            for g in range(6, 9):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))

        elif page == 3:

            for g in range(9, 12):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))

        elif page == 4:

            for g in range(12, 15):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))
                    

        elif page == 5:

            for g in range(15, 18):

                if stampRect[g].collidepoint(mx,my) and tool == "stamp":
                    stamp = stamp_list[g]

                if stamp == stamp_list[g] and canvasRect.collidepoint(mx,my) and tool == "stamp":
                    screen.fill((0,0,0))
                    screen.blit(background,(0,0))
                    x1 = mx-(stamps_image[g].get_width()//2)
                    y1 = my-(stamps_image[g].get_height()//2)
                    screen.blit(stamps_image[g], (x1,y1))

##################################################################
    if click:

        ## CLEARING THE CANVAS ----------------------------------------
                if tool == "clear" and canvasRect.collidepoint(mx,my):
                    draw.rect(screen,WHITE,canvasRect) ## This is clearing the canvas

                if downArrowRect.collidepoint(mx,my) and page >=0 and page <5 and tool == "stamp":
                    page+=1

                elif page!=0 and upArrowRect.collidepoint(mx,my) and page >0 and page <=5 and tool == "stamp" :
                    page -=1
                    
                screen.set_clip(None) # modify everything

        ## SAVING THE PROGRAM --------------------------------------------

                if saveRect.collidepoint(mx,my):
                    try:
                        fname = filedialog.asksaveasfilename(defaultextension = ".png")
                        ## asks the user to enter the file name they would like to save as
                        if fname !="":
                            image.save(screen.subsurface(canvasRect),fname)

                    except:
                        pass ## prevent from program crashing

        ## OPENING A PROGRAM -------------------------------------------------------

                if loadRect.collidepoint(mx,my):
                    try:
                        fname = filedialog.askopenfilename(filetypes = [("images","*.png;*.jpg;*.jpeg")])              
                        screen.set_clip(canvasRect)
                        myPic = image.load(fname)
                        myPic1 = transform.scale(myPic,(680,450))
                        screen.blit(myPic1,canvasRect)
                        screen.set_clip(None)

                    except:
                        pass

### THESE ARE THE EFFECTS FOR THE FONTS BEING DISPLAYED 

    for m in range(15):

        if toolRects[m].collidepoint(mx,my):
            draw.rect(screen,BLUE,toolRects[m],2)
            if tool !="stamp" and tool !="background" and toolRects[m].collidepoint(mx,my):
                screen.blit(Fonts[m], (15,130,165,420))

    if loadRect.collidepoint(mx,my) and tool != "stamp" and tool != "background":
        screen.blit(loadFont, (15,130,165,420))

    if saveRect.collidepoint(mx,my) and tool != "stamp" and tool != "background":
        screen.blit(saveFont, (15,130,165,420))

#####Changing the colour

    if mb[0]==1: ## check if left click

        if wheelRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
            col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)

# draw.circle(screen,BLACK,(mx,my),size,2)
           
    omx=mx ## setting omx to mx                          
    omy=my ## setting omy to my
    display.flip()
    
quit() # closes out pygame window

 

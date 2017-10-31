#graphic12.py
from pygame import *
from random import *
from math import *
#### Defining of Variables ####
game = "startscreen" # determines what the game is doing ex. playing, startscreen, gameover
init()
tool = "start" # what tool is selected
startdelay = -10 # delay so when you press the start button the ship doesnt shoot
delaytimer = 0 # regulates the timer so that it is approximately in seconds
timershot = 100 # delay
captured = 0 # number of characters you have sucked up
shotlist = [] # list holding the bullets the ship shoots
builddelay = 5 # delay that makes sure you cant shoot while placing buildings
timer  = 60 # game timer, when it is zero you lose a life
font1 = font.SysFont("Times New Roman",14) # times new roman font
font2 = font.SysFont("Arial",35) # arial font
font3 = font.SysFont("Futura",60) # futura font
myClock = time.Clock() # regulates the framerate of the game
col = 150 # colour of the tractor beam
col2 = 150 # colour of the titlescreen title
inc2 = 1
shots = 0
badlistpos = []

buildx,buildy = 0,0
num = 0
buildtimer = 1
delay = 0
baddelay = 0
num2 = 0
suckedup = 0
buildlist = []
timer = 60
valid = False
screen=display.set_mode((800,600))
UFO=image.load("UFO.png").convert_alpha()
background = image.load("background.png").convert_alpha()
crosshair = image.load("crosshair.png").convert_alpha()
building = transform.scale(image.load("m.jpg").convert_alpha(),(60,120))
bucket = transform.scale(image.load("paintbucket.png").convert_alpha(),(200,206))
rightarrow= transform.scale(image.load("rightarrow.png").convert_alpha(),(817/5,223/5))
leftarrow= transform.scale(image.load("leftarrow.png").convert_alpha(),(817/5,223/5))
titlescreen = transform.scale(image.load("ufotitle.jpg").convert_alpha(),(485,364))
fullmap = Rect(-415,0,600,9575)
bucketrect = Rect(-15,500,200,200)
buildrect = Rect(400,50,25,25)
balllist = []
health = 500
shipy=300
shipx=400
frameDelay = 3
frameDelay2 = 1000
frame = 0
goal = 0
frameball = 0
pics = []
charpics = []
for i in range(27):
    pics.append(transform.scale(image.load("Explode-05_frame_" + str(i) + ".gif"),(128,96)))
for i in range(1,4):
    charpics.append(transform.scale(image.load("character" + str(i) + ".png"),(256/4,192/4)))
buildinglist = []
edges = []
bottomrect = Rect(-415,585,10000,600)
edges.append(Rect(-415,585,10000,600))
edges.append(Rect(-400,-10000,10000,10000))
edges.append(Rect(-10430,0,10000,800))
edges.append(Rect(9930,0,10000,800))
inc = 1
incy = 1
inc3 =1
vx = 0
rects = []
vy = 0
speedx = 0
speedy = 0
level = 2
lives = 1
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
class buckets:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.l = 200
        self.w = 206
        self.rect = Rect(self.x,self.y,200,206)
    def randompos(self):
        self.x = randint(-15,9500)
        self.rect = Rect(self.x,self.y,200,206)
    def draw(self,shipx):
        if shipx >=-10:
            screen.blit(bucket,(self.x-shipx,self.y))
        if shipx <= -10:
            screen.blit(bucket,(self.x,self.y))
    def point(self,shipx):
        if shipx >=-10:
            if 424 < self.x -shipx - 600:
                screen.blit(rightarrow,(600,300))
            if 424 > self.x - shipx + 600:
                screen.blit(leftarrow,(0,300))
        if shipx <-10:
            if shipx < self.x -600:
                screen.blit(rightarrow,(600,300))
            if shipx > self.x +600:
                screen.blit(leftarrow,(0,300))


bucket1 = buckets(-15,500)
class bullet:
    def __init__(self,x1,x2,y,ang,mx,my,s):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.angle = ang
        self.up = 0
        self.mx = mx
        self.my = my
        self.frame = 0
        self.delay = 3
        self.speed = s
        self.pos = 0
    def shoot(self,speedx):
       if shipx >= -10:
                if self.mx >= self.x1 and self.my >= self.y:
                        self.up += self.speed
                        draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up) - shipx,self.y - toy(2*pi - self.angle,self.up)),4)
                        self.pos = self.x2 + tox(self.angle,self.up)
                elif self.mx <= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up)- shipx,self.y - toy(pi + self.angle,self.up)),4)
                    self.pos = self.x2 + tox(self.angle+pi,self.up)
                elif self.mx <= self.x1 and self.my <= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(pi -self.angle,self.up)- shipx,self.y - toy(self.angle,self.up)),4)
                    self.pos =self.x2 + tox(pi -self.angle,self.up)
                elif self.mx >= self.x1 and self.my <= self.y:
                    self.up +=  self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up)- shipx,self.y - toy(self.angle,self.up)),4)
                    self.pos =self.x2 + tox(self.angle,self.up)
       if shipx < -10:
            if self.mx >= self.x2 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x2  and self.my >= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x2  and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(pi-self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x2 and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
    def shipshoot(self,speedx):
        if self.x1 == 424:

            if self.mx >= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    self.x2 -= speedx
                    draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x1 and self.my >= self.y:
                self.up += self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x1 and self.my <= self.y:
                self.up += self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(pi -self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x1 and self.my <= self.y:
                self.up +=  self.speed
                self.x2 -= speedx
                draw.circle(screen,(255,0,0),(self.x2 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
        if self.x1 < 424:

            if self.mx >= self.x1 and self.my >= self.y:
                    self.up += self.speed
                    draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle,self.up),self.y - toy(2*pi - self.angle,self.up)),4)
            elif self.mx <= self.x1  and self.my >= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle+pi,self.up),self.y - toy(pi + self.angle,self.up)),4)
            elif self.mx <= self.x1  and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(pi-self.angle,self.up),self.y - toy(self.angle,self.up)),4)
            elif self.mx >= self.x1 and self.my <= self.y:
                self.up += self.speed
                draw.circle(screen,(255,0,0),(self.x1 + tox(self.angle,self.up),self.y - toy(self.angle,self.up)),4)
    def animate(self):
                self.delay -= 1                         # count down to zero
                if self.delay == 0:                     # then advance frame like normal
                    self.delay = 20
                    self.frame += 1
                    if self.frame == 9:
                        self.frame = 0


class badgun:
    def __init__(self,x,y,ang):
        self.x = x
        self.y = y
        self.l = 50
        self.w = 20
        self.rect =Rect(x,y,20,50)
        self.listpos = []
        self.listshots = []
        self.delay = 0
        self.rate = randint(50,1000)
        self.health = 100
        self.angle = ang
    def shoot(self, shipx):
        if shipx >= -10:
                self.angle = getangle(distance(self.x-shipx+10,self.y,self.x-shipx+10,shipy),distance(self.x-shipx+10,self.y,424,self.y))
        elif shipx < -10:
                self.angle  = getangle(distance(self.x+10,self.y,self.x+10,shipy),distance(self.x+10,self.y,shipx+424,self.y))
        if self.delay == 0:
            if shipx >= -10:
                ang = getangle(distance(self.x-shipx+10,self.y,self.x-shipx+10,shipy),distance(self.x-shipx+10,self.y,424,self.y))
                self.listshots.append(bullet(self.x+10-shipx,self.x,self.y,ang,424,shipy,10))
                self.delay +=1
            elif shipx < -10:
                ang  = getangle(distance(self.x+10,self.y,self.x+10,shipy),distance(self.x+10,self.y,shipx+424,self.y))
                self.listshots.append(bullet(self.x+10,self.x+10,self.y,ang,shipx+424,shipy,10))
                self.delay +=1
        else:
            self.delay +=1
            if self.delay == self.rate:
                self.delay = 0

class buildings:
    def __init__(self,x,y):
        self.x =x
        self.y =y
        self.l = 120
        self.w = 60
        self.rect = Rect(x,y,60,120)
        self.timer = 0
    def createguys(self,shipx):
        if self.timer == 0:
            balls.append(ball(self.x+75,575))
            self.timer +=1
        else:
            self.timer +=1
            if self.timer == 10:
                self.timer = 0
class ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vydown = 0
        self.vyup = 0
        self.speed =  randint(1,2)
        self.destx = self.speed *(randint(0,10000/self.speed))
        self.wieght = 5
        self.col = 255,0,0
        self.pic = charpics
        self.captured = False
    def move(self):
        if shipx >= -10 and shipx <= 9149:
                if mb[2] == 1  and  self.y > shipy and self.x-192/4-shipx >= 424-dist/5 and self.x-192/4-shipx <= 424+dist/5:
                    self.vydown = 0
                    self.vyup += int(500/dist)
                    self.y -= - self.wieght + self.vyup
                    self.vx = speedx
                    if self.x-shipx-192/6 > 424:
                        self.x -= 3
                    if self.x-shipx-192/6 < 424:
                        self.x += 3
                elif self.y < 575 and -self.wieght + self.vyup <= 0:
                    self.vyup -= 1
                    self.vydown += 1
                    self.y += self.wieght + self.vydown - self.vyup
                    self.x += self.vx
                elif self.y < 575:
                        self.vyup -= 1
                        self.vydown += 1
                        self.y += self.wieght + self.vydown - self.vyup
                        self.x += self.vx
                elif self.y == 575:
                    self.vydown = 0
                    self.vx = 0
                    if self.destx == self.x:
                        self.destx =  randint(0,799)
                    else:
                        if self.destx < self.x:
                            self.x -= self. speed+self.vx
                        if self.destx > self.x:
                            self.x += self.speed+self.vx
                if self.y >575:
                    self.y = 575
        if shipx < -10:
                if mb[2] == 1  and  self.y > shipy and self.x-192/4 >= shipx+424-dist/5 and self.x-192/4 <= shipx+424+dist/5:
                    self.vydown = 0
                    self.vyup += int(500/dist)
                    self.y -= - self.wieght + self.vyup
                    self.vx = speedx
                    if self.x - 192/6 > shipx + 424:
                        self.x -= 2
                    if self.x - 192/6 < shipx + 424:
                        self.x += 2
                elif self.y < 575 and -self.wieght + self.vyup <= 0:
                    self.vyup -= 1
                    self.vydown += 1
                    self.y += self.wieght + self.vydown - self.vyup
                    self.x += self.vx
                elif self.y < 575:
                        self.vyup -= 1
                        self.vydown += 1
                        self.y += self.wieght + self.vydown - self.vyup
                        self.x += self.vx
                elif self.y == 575:
                    self.vydown = 0
                    self.vx = 0
                    if self.destx == self.x:
                        self.destx =  randint(15,799)
                    else:
                        if self.destx < self.x:

                            self.x -= self.speed+self.vx
                        if self.destx > self.x:
                            self.x += self.speed+self.vx
                if self.y >575:
                    self.y = 575
balls = []
def getangle(y,x):
    theta = atan2(y,x)
    return theta
def tox (angle,size): # determines x coordinate when given the inner angle and radius of the circle
    return cos(angle)*size
def toy(angle, size): # determines y coordinate when given the inner angle and radius of the circle
    return sin(angle)*size
for i in range(100):
    balls.append(ball(randint(15,1000),575))
def drawText(message,x, y,font,col): # copied from Mr. Mackenzie
    text = font.render( message , 1, (col))
    textpos = text.get_rect().move(x, y)
    screen.blit(text, textpos)

def moveship(keys, x, y):
        if keys[K_w]==1:
            y-=3
        if keys[K_s]==1:
            y+=3
        if keys[K_a]==1:
            x-=3
        if keys[K_d]==1:
            x+=3
        return x, y
def collide(rect, shiprect, health, shipx, shipy, speedx, speedy,build):
        oldhealth = 100
        num  = shiprect.colliderect(rect)
        if num == True:
            oldhealth = health
            if speedx > 0:
                health -= speedx
            if speedx < 0:
                health += speedx
            if speedy > 0:
                health -= speedy
            if speedy < 0:
                health += speedy
            if build == True:
                shipx -= speedx
                shipy -= speedy
            speedy = 0
            speedx = 0

        return speedx, speedy, health,num,shipx,shipy,oldhealth

running=True
while running==True:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        mx,my = mouse.get_pos()
        mb= mouse.get_pressed()
    if game == "startscreen":

        screen.fill((0,0,0))
        screen.blit(titlescreen,(-10,-10))
        col2+=1*inc2
        if col2 == 254:
            inc2= -1
        if col2 == 150:
            inc2 = 1
        playrect = Rect(250,300,100,35)
        instructrect = Rect(250,350,100,35)
        drawText("Play Game",250,300,font2,(255,0,0))
        drawText("Instructions",250,350,font2,(255,0,0))
        if playrect.collidepoint(mx,my):
            drawText("Play Game",250,300,font2,(0,255,0))
            if mb[0] == 1:
                game = "start"
        if instructrect.collidepoint(mx,my):
            drawText("Instructions",250,350,font2,(0,255,0))
            if mb[0] == 1:
                game = "instructions"

        drawText("Abduction",200,200,font3,(0,col2,0))
    if game == "instructions":
        screen.fill((0,0,0))
        drawText("Back",50,50,font1,(255,0,0))
        drawText("Controls",50,75,font2,(255,0,0))
        drawText("Right - Click Tractor Beam",50,125,font1,(255,0,0))
        drawText("Left - Click Shoot",50,150,font1,(255,0,0))
        drawText("Spacebar - Dump guys",50,175,font1,(255,0,0))
        drawText("W - Move Up",50,200,font1,(255,0,0))
        drawText("A - Move Left",50,225,font1,(255,0,0))
        drawText("S - Move Down",50,250,font1,(255,0,0))
        drawText("D - Move Right",50,275,font1,(255,0,0))




        """You are the commander of a UFO.
        You must abduct as many humans as possible within the time limit and dump them into the bucket for collection.
        You may create spawn zones to create more humans.
        Watch out for enemy defense turrets and Good Luck!"""

        backrect = Rect(50,50,75,35)
        if backrect.collidepoint(mx,my):
            drawText("Back",50,50,font2,(0,255,0))
            if mb[0] ==1:
                game = "startscreen"

    if game == "start":
        startdelay +=1
        if startdelay == 0:
            tool = ""

        if delaytimer == 0:

            timer -=1
            delaytimer+=1
        else:
            delaytimer +=1
        if delaytimer  == 30:
            delaytimer = 0
        if shipx >= -10 and shipx <= 9570:
            screen.blit(background, (-shipx, 0))
        if shipx > 9570:
            screen.blit(background, (-9570, 0))
        if shipx < -10:
            screen.blit(background, (0, 0))
        if buildlist != []:
            for build in buildlist:
               build.createguys(shipx)
               if shipx >= -10 and shipx <= 9215:
                    speedx, speedy, health,num,shipx,shipy,oldhealth = collide(Rect(build.x-shipx,build.y,build.w,build.l),shiprect,health, shipx, shipy, speedx,speedy, True)
                    screen.blit(building,(build.x-shipx,build.y))
               if shipx < -10:
                    speedx, speedy, health,num,shipx,shipy,oldhealth = collide(Rect(build.x-shipx,build.y,build.w,build.l),shiprect,health, shipx, shipy, speedx,speedy, True)
                    screen.blit(building,(build.x,build.y))

        if health > 0:
            keys=key.get_pressed()
            speedx, speedy = moveship(keys,speedx,speedy)
            if speedx > 0:
                speedx-=1
            if speedx < 0:
                speedx+=1
            if speedy > 0:
                speedy-=1
            if speedy < 0:
                speedy+=1
            shipx += speedx
            shipy += speedy
        if shipx >= -10 and shipx <= 9149:
            shiprect = Rect(424-12.5,shipy-12.5,25,25)
        if shipx <-10:
            shiprect = Rect(shipx-12.5,shipy-12.5,25,25)
        if shipx >= -10 and shipx <= 9149:
            shiprect2 = Rect(424-25,shipy-25,50,50)
        if shipx <-10:
            shiprect2 = Rect(shipx-25,shipy-25,50,50)
        for rect in edges:
            speedx, speedy, health,num,shipx,shipy,oldhealth = collide(rect,shiprect,health, shipx, shipy, speedx,speedy, False)
        if shipx<=-400:
            shipx = -410
        if shipx >= 9931:
            shipx = 9931
        if shipy >= 560:
            shipy = 570
        if shipy <= 10:
            shipy = 10

        screen.blit(crosshair,(mx-12.5,my-12.5))
        if mb[2] ==1:
            col+=1*inc
            if col == 254:
                inc = -1
            if col == 150:
                inc = 1
            dist = distance(425,575,425,shipy)
            if shipx >= -10 and shipx <= 9149:
                draw.polygon(screen,(0,col,0),((424,shipy),(424-dist/5,shipy+dist),(424+dist/5,shipy+dist)))
            else:
                draw.polygon(screen,(0,col,0),((shipx+424,shipy),(shipx-dist/5+424,shipy+dist),(shipx+dist/5+424,shipy+dist)))
        if health > 0:
            if shipx >= -10 and shipx <= 9149:
                screen.blit(UFO, (400, shipy-25))
            if shipx > 9149:
                screen.blit(UFO, (shipx-9149, shipy-25))
            if shipx < -10:
                screen.blit(UFO, (shipx+400, shipy-25))

        if delay == 0:
            if mb[0] == 1 and my >100 and tool == "":
                shots += 1
                if shipx >= -10 and shipx <= 9149:
                    angle = getangle(distance(424,shipy,424,my),distance(424,shipy,mx,shipy))
                    shotlist.append(bullet(424,424,shipy,angle,mx,my,25))
                if shipx < -10:
                    omx, omy,oshipx,oshipy = mx, my, shipx,shipy
                    angle2 = getangle(distance(oshipx+424,oshipy,oshipx+424,my),distance(oshipx+424,oshipy,mx,oshipy))
                    shotlist.append(bullet(oshipx,oshipx,oshipy,angle2,omx,omy,25))
                delay += 1
        else:
            delay += 1
            if delay == 10:
                delay = 0
        if shots > 0:
            for shotz in shotlist:
                shotz.shipshoot(speedx)
                if shotz.x1 >= 424 and shotz.x1 <= 9149:
                    if shotz.mx >= 424 and shotz.my >= shotz.y:
                            if shotz.y - toy(2*pi - shotz.angle,shotz.up) >= 575:
                                shotz.up = 0
                                shotlist.remove(shotz)
                            if shotz.x1 + tox(shotz.angle,shotz.up) >= 9570:
                                shotz.up = 0
                                shotlist.remove(shotz)
                    if shotz.mx <= 424 and shotz.my >= shotz.y:
                        if shotz.x1 + tox(shotz.angle+pi,shotz.up) <= -415:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.y - toy(pi + shotz.angle,shotz.up) >= 575:
                                shotz.up = 0
                                shotlist.remove(shotz)
                    if shotz.mx <= 424 and shotz.my <= shotz.y:
                        if shotz.x1 + tox(pi-shotz.angle,shotz.up) <= -415:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.y - toy(shotz.angle,shotz.up) <= 0:
                                shotz.up = 0
                                shotlist.remove(shotz)
                    if shotz.mx >= 424 and shotz.my <= shotz.y:
                        if shotz.x1 + tox(shotz.angle,shotz.up) >= 10000:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.y - toy(shotz.angle,shotz.up) <= 0:
                                shotz.up = 0
                                shotlist.remove(shotz)
                if shotz.x1 < 424:
                    shotz.x1 =  shipx+424
                    if shotz.mx >= shotz.x1 + 424 and shotz.my >= shotz.y:
                        if shotz.y - toy(2*pi - shotz.angle,shotz.up) >= 575:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.x1 + tox(shotz.angle,shotz.up) >= 9570:
                            shotz.up = 0
                            shotlist.remove(shotz)
                    if shotz.mx <= shotz.x1 + 424 and shotz.my >= shotz.y:
                        if shotz.x1 + tox(shotz.angle+pi,shotz.up) <= -415:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.y - toy(pi + shotz.angle,shotz.up) >= 575:
                                shotz.up = 0
                                shotlist.remove(shotz)
                    if shotz.mx <= shotz.x1 + 424 and shotz.my <= shotz.y:
                       if shotz.x1 + tox(pi-shotz.angle,shotz.up) <= -415:
                                shotz.up = 0
                                shotlist.remove(shotz)
                       if shotz.y - toy(shotz.angle,shotz.up) <= 0:
                                shotz.up = 0
                                shotlist.remove(shotz)
                    if shotz.mx >= shotz.x1 + 424 and shotz.my <= shotz.y:
                        if shotz.x1 + tox(shotz.angle,shotz.up) >= 10000:
                                shotz.up = 0
                                shotlist.remove(shotz)
                        if shotz.y - toy(shotz.angle,shotz.up) <= 0:
                                shotz.up = 0
                                shotlist.remove(shotz)
        for ballz in balls:
            ballz.move()
            if suckedup + 1 <= 50:
                if ballz.y in range(shipy, shipy+25) and mb[2] == 1 and ballz.x-shipx-192/5 in range(400,450):
                    balls.remove(ballz)
                    suckedup += 1
            if shipx <= 9149 and shipx >= -10:
                if ballz.destx > ballz.x:
                    screen.blit(charpics[frameball],(ballz.x-256/4-shipx,ballz.y-192/4)) # copied from Mr. Mackenzie
                else:
                    screen.blit(transform.flip(charpics[frameball],1,0),(ballz.x-256/4-shipx,ballz.y-192/4))
                frameDelay2 -= 1                          # count down to zero
                if frameDelay2 == 0:     # copied from Mr. Mackenzie                # then advance frame like normal
                    frameDelay2 = 500
                    frameball += 1
                    if frameball == 3:
                        frameball = 0
            if shipx > 9149:
                if ballz.destx > ballz.x:
                    screen.blit(charpics[frameball],(ballz.x-256/4-9149,ballz.y-192/4))
                else:
                    screen.blit(transform.flip(charpics[frameball],1,0),(ballz.x-256/4-9149,ballz.y-192/4))
                frameDelay2 -= 1         # copied from Mr. Mackenzie                # count down to zero
                if frameDelay2 == 0:                     # then advance frame like normal
                    frameDelay2 = 500
                    frameball += 1
                    if frameball == 3:
                        frameball = 0
            if shipx < -10:
                if ballz.destx > ballz.x:
                    screen.blit(charpics[frameball],(ballz.x-256/4,ballz.y-192/4))
                else:
                    screen.blit(transform.flip(charpics[frameball],1,0),(ballz.x-256/4,ballz.y-192/4))
                frameDelay2 -= 1        # copied from Mr. Mackenzie                 # count down to zero
                if frameDelay2 == 0:                     # then advance frame like normal
                    frameDelay2 = 500
                    frameball += 1
                    if frameball == 3:
                        frameball = 0
            if bucket1.rect.collidepoint(ballz.x,ballz.y) and ballz.captured == True:
                captured += 1
                goal +=1
                balls.remove(ballz)
        if keys[K_SPACE] == 1 or health <= 0:
            for i in range(suckedup):
                balls.append(ball(shipx+450+randint(-10,10),shipy))
                balls[-1].captured = True
                balls[-1].vx = randint(-1,1)
                balls[-1].vydown = randint(0,5)
            suckedup = 0


        if health > 0:
            draw.rect(screen,(0,255,0),(50,50,125,25))
            draw.rect(screen,(255,0,0),(50,50,health/4,25))

        if health <= 0:
            if shipx >=  -10:
                screen.blit(pics[frame],(400 - 256/4,shipy-192/4))
                frameDelay -= 1                         # count down to zero
                if frameDelay == 0:                     # then advance frame like normal
                    frameDelay = 3
                    frame += 1
                    if frame == 9:
                        frame = 0
                        health = 100
                        lives -=1
            else:
                screen.blit(pics[frame],(shipx+ 400 - 256/4, shipy - 192/4)) # copied from mr mackenzie
                frameDelay -= 1                         # count down to zero
                if frameDelay == 0:                     # then advance frame like normal
                    frameDelay = 3
                    frame += 1
                    if frame == 9:
                        frame = 0
                        health = 100
                        lives -=1
        bucket1.draw(shipx)
        if goal >= level**2+50:
            level+=1
            goal = 0
            bucket1.randompos()
            for i in range(level**2+1):
                x = randint(200, 2000)
                badlistpos.append(badgun(x,500,0))
        for bad in badlistpos:
            bad.shoot(shipx)
            for shot in bad.listshots:
                    shot.shoot(shipx)
                    if shipx >= -10 and shipx < 9149:
                        if shot.x1 >= -10 and shot.x1 <= 9149:
                            if shot.mx >= shot.x1  and shot.my >= shot.y:

                                    if shiprect2.collidepoint(shot.pos-ballx,shot.y-toy(2*pi  - shot.angle,shot.up)):
                                        health -= 10
                                    if shot.y - toy(2*pi - shot.angle,shot.up) >= 575:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                    if shot.x1 + tox(shot.angle,shot.up) >= 9570:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx <= shot.x1 and shot.my >= shot.y:

                                if shiprect2.collidepoint(shot.pos-ballx,shot.y-toy(pi + shot.angle,shot.up)):
                                        health -= 10
                                if shot.x1 + tox(shot.angle+pi,shot.up) <= -415:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(pi + shot.angle,shot.up) >= 575:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx <= shot.x1  and shot.my <= shot.y:

                                if shiprect2.collidepoint(shot.pos-shipx,shot.y-toy(shot.angle,shot.up)):
                                        health -= 10
                                if shot.x1 + tox(pi-shot.angle,shot.up) <= -415:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(shot.angle,shot.up) <= 0:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx >= shot.x1  and shot.my <= shot.y:
                                if shiprect2.collidepoint(shot.pos-shipx,shot.y-toy(shot.angle,shot.up)):
                                        health -= 10
                                if shot.x1 + tox(shot.angle,shot.up) >= 10000:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(shot.angle,shot.up) <= 0:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                    if shipx < -10:
                            if shot.mx >= shot.x2  and shot.my >= shot.y:
                                    if shiprect.collidepoint(shot.pos,shot.y-toy(2*pi  - shot.angle,shot.up)):
                                        health -= 10
                                    if shot.y - toy(2*pi - shot.angle,shot.up) >= 575:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                    if shot.x2 + tox(shot.angle,shot.up) >= 9570:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx <= shot.x2 and shot.my >= shot.y:
                                if shiprect.collidepoint(shot.pos,shot.y-toy(pi + shot.angle,shot.up)):
                                        health -= 10
                                if shot.x2 + tox(shot.angle+pi,shot.up) <= -415:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(pi + shot.angle,shot.up) >= 575:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx <= shot.x2  and shot.my <= shot.y:
                                if shiprect.collidepoint(shot.pos,shot.y-toy(shot.angle,shot.up)):
                                        health -= 10
                                if shot.x2 + tox(pi-shot.angle,shot.up) <= -415:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(shot.angle,shot.up) <= 0:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                            if shot.mx >= shot.x2  and shot.my <= shot.y:
                                if shiprect.collidepoint(shot.pos,shot.y-toy(shot.angle,shot.up)):
                                        health -= 10
                                if shot.x2 + tox(shot.angle,shot.up) >= 10000:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
                                if shot.y - toy(shot.angle,shot.up) <= 0:
                                        shot.up = 0
                                        bad.listshots.remove(shot)
            if shipx > -10:
                if 424 >= bad.x - shipx + 10 and shipy >= bad.y:
                    draw.line(screen,(0,0,0),(bad.x-shipx+10,bad.y),(bad.x-shipx+10+tox(bad.angle,50),bad.y-toy(2*pi - bad.angle,50)))
                if 424 <= bad.x -shipx+ 10 and shipy >= bad.y:
                    draw.line(screen,(0,0,0),(bad.x-shipx+10,bad.y),(bad.x-shipx+10+tox(bad.angle+pi,50),bad.y-toy(bad.angle+pi,50)))
                if 424 <= bad.x -shipx + 10 and shipy <= bad.y:
                    draw.line(screen,(0,0,0),(bad.x-shipx+10,bad.y),(bad.x-shipx+10+tox(pi-bad.angle,50),bad.y-toy(bad.angle,50)))
                if 424 >= bad.x -shipx + 10 and shipy <= bad.y:
                    draw.line(screen,(0,0,0),(bad.x-shipx+10,bad.y),(bad.x-shipx+10+tox(bad.angle,50),bad.y-toy(bad.angle,50)))
            if shipx < -10:
                if shipx+424 >= bad.x + 10 and shipy >= bad.y:
                    draw.line(screen,(0,0,0),(bad.x+10,bad.y),(bad.x+10+tox(bad.angle,50),bad.y-toy(2*pi - bad.angle,50)))
                if shipx+424 <= bad.x + 10 and shipy >= bad.y:
                    draw.line(screen,(0,0,0),(bad.x+10,bad.y),(bad.x+10+tox(bad.angle+pi,50),bad.y-toy(bad.angle+pi,50)))
                if shipx+424 <= bad.x  + 10 and shipy <= bad.y:
                    draw.line(screen,(0,0,0),(bad.x+10,bad.y),(bad.x+10+tox(pi-bad.angle,50),bad.y-toy(bad.angle,50)))
                if shipx+424 >= bad.x + 10 and shipy <= bad.y:
                    draw.line(screen,(0,0,0),(bad.x+10,bad.y),(bad.x+10+tox(bad.angle,50),bad.y-toy(bad.angle,50)))

            if shipx >= -10:
                draw.rect(screen,(0,255,0),(bad.x- shipx,bad.y,bad.w,bad.l+50))
            if shipx < -10:

                draw.rect(screen,(0,255,0),(bad.x,bad.y,bad.w,bad.l+50))
        drawText("Weight: ", 200,50, font1,(255,0,0))
        drawText(str(suckedup),250,50, font1,(255,0,0))
        drawText("Points: ", 300,50, font1,(255,0,0))
        drawText(str(captured), 350,50, font1,(255,0,0))
        drawText("Lives: ", 450,50, font1,(255,0,0))
        drawText(str(lives), 500,50, font1,(255,0,0))
        drawText("Goal: ", 200,100, font1,(255,0,0))
        drawText(str(level**2+50-goal), 250,100, font1,(255,0,0))
        drawText("Level: ", 300,100, font1,(255,0,0))
        drawText(str(level), 350,100, font1,(255,0,0))
        drawText("Timer: ", 400,100, font1,(255,0,0))
        drawText(str(timer), 450,100, font1,(255,0,0))
        draw.rect(screen,(255,0,0),(buildrect))
        if mb[0] == 1 and buildrect.collidepoint(mx,my):
            tool = "build"
            valid = True
        if valid == True:
            snap = distance(mx,my,mx,575)
            if snap <=  150:
                screen.blit(building,(mx,575-120))
                if mb[0] == 1:
                    if captured - 10 >=   0:
                        omx = mx
                        if shipx >= -10:
                            buildlist.append(buildings(omx+shipx,455))
                        if shipx < -10:
                            buildlist.append(buildings(omx,455))
                        captured -=10
                        valid = False
                        for i in range(5):
                            builddelay -=1
                            if builddelay == 0:
                                tool = ""
                                buildelay =1
                    else:
                        draw.rect(screen,(255,0,0),(mx,455,60,120))
                        valid = False
                        for i in range(5):
                            builddelay -=1
                            if builddelay == 0:
                                tool = ""
                                builddelay =1
            else:
                screen.blit(building,(mx,my))
        if timer ==0:
            health =0
            timer = 60

        if lives == 0:
            game = "gameover"


    if game == "gameover":
        screen.fill((0,0,0))
        drawText("Game Over",250,250,font3,(0,255,0))
        drawText("Retry?",250,350,font2,(255,0,0))
        drawText("Return to Menu",250,400,font2,(255,0,0))
        retryrect = Rect(250,350,100,35)
        returnrect = Rect(250,400,100,35)
        if retryrect.collidepoint(mx,my):
            drawText("Retry?",250,350,font2,(0,255,0))
            if mb[0] == 1:
                lives = 4
                level = 1
                captured = 0
                suckedup = 0
                timer = 60
                ballx = 400
                bally = 300
                goal = 0
                startdelay = -1
                goal = level**2+50
                game = "start"
        if returnrect.collidepoint(mx,my):
            drawText("Return to Menu",250,400,font2,(0,255,0))
            if mb[0] == 1:
                lives = 4
                level = 1
                captured = 0
                suckedup = 0
                goal = 0
                timer = 60
                ballx = 400
                bally = 300
                startdelay = -1
                goal = level**2+50
                game = "startscreen"

    if game == "start":
        bucket1.point(shipx)
    "fullscreen = screen.subsurface(fullmap).copy()"
    display.flip()
    myClock.tick(30)
quit()

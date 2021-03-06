#Work cited: You, Brendan, Internet
#DONKEY KONG SIMULATION

from ggame import App, RectangleAsset, CircleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black = Color(0, 1)
lgreen = Color(0xd9ffcc, 1.0)
dgreen = Color(0x006600, 1.0)
purp = Color(0x9900cc, 1.0)
blue = Color(0x3399ff,1.0)
gold = Color(0xcc9900, 1.0)
red = Color(0xff6666, 1.0)
noline = LineStyle(0, black)
sider = RectangleAsset (20, 720, noline, dgreen) 
capr = RectangleAsset (2, 28, noline, dgreen)
player = RectangleAsset (20, 50, noline, purp)
heart = CircleAsset (15, noline, red)
prize = RectangleAsset (35, 15, noline, gold)
toppp = RectangleAsset (1080, 20, noline, dgreen)
barrels = CircleAsset (10, noline, black)
global level
level = 1
global levelshift
levelshift = 0
vy=0
vx=0
ti=0

class dk(App):
    def __init__(self, width, height):
            super().__init__(width, height)
            bg_asset = RectangleAsset(width, height, noline, lgreen)
            bg = Sprite(bg_asset, (0,0))
            self.lvltext = 0
            self.leveltext = 0
    def step (self):
        playe.step()
        bare.step()
        barh.step()
        barj.step()
        bark.step()
        barl.step()
    def lvlchange (self):
        global level
        if level == 1:
            self.lvl1s = [block(x) for x in lvl1]
            self.lvltxt = TextAsset(level,style='40px luminari')
            self.leveltext = Sprite(self.lvltxt, (1000,15))
        if level > 1:
            self.leveltext.destroy()
            self.lvltxt = TextAsset(level,style='40px luminari')
            self.leveltext = Sprite(self.lvltxt, (1000,15))
        if level == 2:
            for p in self.lvl1s:
                p.destroy()
            self.lvl2s = [block(x) for x in lvl2]
        if level == 3:
            for p in self.lvl2s:
                p.destroy()
            self.lvl3s = [block(x) for x in lvl3]
        if level == 4:
            for p in self.lvl3s:
                p.destroy()
            self.lvl4s = [block(x) for x in lvl4]
        if level == 5:
            for p in self.lvl4s:
                p.destroy()
            self.lvl5s = [block(x) for x in lvl5]
        if level == 6:
            for p in self.lvl5s:
                p.destroy()
            self.lvl6s = [block(x) for x in lvl6]
        if level == 7:
            for p in self.lvl6s:
                p.destroy()
            self.lvl7s = [block(x) for x in lvl7]
        if level == 8:
            for p in self.lvl7s:
                p.destroy()
            self.lvl8s = [block(x) for x in lvl8]
        if level == 9:
            for p in self.lvl8s:
                p.destroy()
            self.lvl9s = [block(x) for x in lvl9]
        if level == 10:
            for p in self.lvl9s:
                p.destroy()
            self.lvl10s = [block(x) for x in lvl10]
        if level == 11:
            for p in self.lvl10s:
                p.destroy()
            self.lvl11s = [block(x) for x in lvl11]
        if level == 12:
            for p in self.lvl11s:
                p.destroy()
            self.lvl12s = [block(x) for x in lvl12]
            
            


   
onblock = 0
jump = 0
wub=0
go = 0

class bar(Sprite):
    def __init__(self, position, vx, vy, ti, delay):
        super().__init__(barrels, position)
        self.vx = vx
        self.vy = vy
        self.ti = ti
        self.vxo = self.vx
        self.vyo = self.vy
        self.origx = self.x
        self.origy = self.y
        self.onblock=0
        self.go = 0
        self.tim=0
        self.delay = delay
    def start(self):
        self.visible = True
        self.go = 1
        self.x = self.origx
        self.y = self.origy
        self.vx = self.vxo
        self.vy = self.vyo
    def dead(self):
        for x in myapp.getSpritesbyClass(bar):
            x.tim = -2
            x.x = x.origx
            x.y = x.origy
            x.go=0
    def step(self):
        self.tim+=1
        if self.tim == self.delay:
            self.start()
        if self.go == 1:
            on = self.collidingWithSprites(top)
            self.onblock = 0
            if len(on) > 0:
                self.onblock = 1
            if self.onblock == 1:
                self.ti = 0
                self.vy = 0
                self.y = on[0].y-10
            self.vy =self.ti+self.vy
            self.y=self.y+self.vy
            self.x=self.x+self.vx
            if onblock != 1:
                self.ti += 0.005
            if len(on) == 0:
                self.onblock=0
            csides = self.collidingWithSprites(side)
            if len(csides) > 0:
                self.vx=-self.vx
            if self.x > 1030 and self.y>650:
                self.x=540
                self.y=12
            
            

class play(Sprite):
    def __init__(self, position, vx, vy, ti):
        super().__init__(player, position)
        dk.listenKeyEvent('keydown', 'left arrow', self.lup)
        dk.listenKeyEvent('keydown', 'right arrow', self.rup)
        dk.listenKeyEvent('keydown', 'up arrow', self.uup)
        dk.listenKeyEvent('keydown', 'space', self.wup)
        self.vx=vx
        self.vy=vy
        self.ti=ti
        self.onblock=0
        self.jump = 0
        self.wub =0
        self.dead = 0
        self.vy=0
        self.countlives = 3
        global levelshift
        levelshift = 1
        self.timertxt=0
        self.timert=0
        global timercount, timerlist, alltime
        timercount=0
        timerlist = []
        alltime = 0
        timeasset = TextAsset("level",style = '25px luminari')
        timmeasset = Sprite(timeasset, (930, 25))
        timmmeasset = TextAsset("time",style = '25px luminari')
        timmmmeasset = Sprite(timmmeasset, (930, 73))
        livesasset=TextAsset("lives",style = '15px luminari')
        livvesasset = Sprite(livesasset, (60, 50))
    def step(self):
        self.dead = 0
        self.onblock=0
        
        #timer
        global alltime
        alltime += 0.015625
        if (alltime)%1 == 0:
            global timerlist, timercount
            timercount += 1
            self.timertxt = TextAsset(timercount,style='40px luminari')
            if len(timerlist)>0:
                for x in timerlist:
                    x.destroy()
                    timerlist=[]
            timerlist.append(Sprite(self.timertxt, (1000, 60)))
        
        #gravity
        if self.wub == 0:
            self.ti=self.ti+0.012
        self.vy=self.ti+self.vy
        self.y=self.y+self.vy
        self.x=self.x+self.vx
        if self.ti>0.72:
            self.y-=8
            
        #under and side collisions
        under = self.collidingWithSprites(bot)
        if len(under) > 0:
            self.vy=-0.25*self.vy
            self.y+=10
        csides = self.collidingWithSprites(side)
        ccap = self.collidingWithSprites(cap)
        ccapb = self.collidingWithSprites(capb)
        if len(csides) > 0:
            self.vx=-self.vx
        if len(ccap) + len(ccapb) > 0:
            self.vx=0
        
        #dead
        be = self.collidingWithSprites(bar)
        if len(be) >= 1:
            self.x=1000
            self.y=660
            self.ti=2
            be[0].dead()
            if self.countlives == 3:
                hearta.firstloss()
            if self.countlives ==2:
                heartb.secondloss()
            if self.countlives ==1:
                heartc.lastloss()
            if self.countlives ==0:
                play.stop()
            self.countlives -= 1
        
        
        #onblock and jumping
        on = self.collidingWithSprites(top)
        if len(on) == 0:
            self.onblock = 0
        if len(on) == 1:
            self.onblock = 1
            self.y = on[0].y-self.height
        if self.wub != 1:
            if self.jump == 1:
                if self.onblock ==1:
                    self.vy -= 8.5
                    self.jump = 0
                    self.onblock=0
        if self.wub == 1:
            if self.jump != 1:
                if self.onblock == 1:
                    self.vy -= 3.5
                    self.ti+=0.0008
                    self.wub = 0
                    self.onblock = 0
        if self.onblock == 1:
            self.ti = 0
            self.vy = 0
        
        
        #win
        winc = self.collidingWithSprites(win)
        if len (winc) > 0:
            global level
            level += 1
            global levelshift
            levelshift = 1
            bare.dead()
            barl.dead()
            bark.dead()
            barj.dead()
            barh.dead()
            self.x=1000
            self.y=660
            self.ti=2
            
        global levelshift
        if levelshift == 1:
            myapp.lvlchange()
            global levelshift
            levelshift = 0
            
        
        
        
        
    def rup(self, event):
        if self.vx<3:
            self.vx+=1
    def lup(self, event):
        if self.vx>-3:
            self.vx-=1
    def uup(self, event):
        if self.onblock==1:
            self.jump = 1
    def wup(self, event):
        self.wub = 1
    def stop(self):
        self.vx=0
        self.vy=0
        self.ti=0
        
        
class liv(Sprite):
    def __init__(self, position, lives):
        super().__init__(heart, position)
        self.lives = lives
    def firstloss (self):
        if self.lives == 3:
            self.visible = False
            self.lives = 2
    def secondloss (self):
        if self.lives == 2:
            self.visible = False
            self.lives = 1
    def lastloss (self):
        if self.lives == 1:
            self.visible = False
            self.lives = 0
            

class bot(Sprite):
    def __init__(self,position, length):
        super().__init__(RectangleAsset (length, 20, noline, dgreen) , position)
class top(Sprite):
    def __init__(self,position, length):
        super().__init__(RectangleAsset (length, 20, noline, dgreen), (position[0], position[1]-10))
class cap(Sprite):
    def __init__(self,position, length):
        super().__init__(RectangleAsset (2, 28, noline, dgreen), (position[0] - 2, position[1]-8))
class capb(Sprite):
    def __init__(self,position, length):
        super().__init__(RectangleAsset (2, 28, noline, dgreen), (position[0] + length, position[1]-8))


class block():
    def __init__(self, spec): 
        position = spec[0]
        length = spec[1]
        self.top = top(position, length)
        self.bot = bot(position, length)
        self.cap = cap(position, length)
        self.cap2 = capb(position, length)
        
    def destroy(self):
        self.top.destroy()
        self.bot.destroy()
        self.cap.destroy()
        self.cap2.destroy()


class side(Sprite):
    def __init__(self,position):
        super().__init__(sider, position)

        
class win(Sprite):
    def __init__(self,position):
        super().__init__(prize, position)
        

myapp = dk(SCREEN_WIDTH, SCREEN_HEIGHT)

side ((-10,0))
side ((1070, 0))


lvl3= [((0, 720), 1080), ((0, 576), 600), ((800, 576), 300), ((0, 432), 300), ((480, 432), 450), ((0, 288), 100),
((250, 288), 500), ((900, 288), 500), ((0, 144), 500), ((650, 144), 600)]

lvl5=[((0, 720), 1080), ((100, 576), 980), ((0, 432), 980), ((100, 288), 1000),((0, 144),980)]

lvl4=[((0, 720), 1080), ((300, 576), 500), ((300, 432), 200), ((600, 432),200), ((300, 288),100), ((0, 144),250)]

lvl2=[((0, 720), 1080), ((0, 576), 900),((0, 432), 700),((0, 288), 500), ((0, 144), 300), ((630,144),600)]

lvl6=[((0,720),1080), ((50,576),20), ((100,432),20),((50,288),20),((100, 144),20)]

lvl1=[((0,720),1080), ((0,576),600), ((200,432),200),((0,288),200),((100, 144),200), ((400,144),600)]

lvl7=[((0, 720), 1080), ((0, 576), 350), ((440, 576), 270), ((200, 510), 100),((60, 450), 100), 
((200, 400), 500), ((600, 300), 50), ((630, 270),50), ((750, 200),100), ((490,90),180), 
((200,100),120), ((800, 300),380)]


playe = play((1000, 640), 0, 0, 0)
prizee = win((100, 120))

bare = bar ((540, -10), 1.9, 0, 0, 5)
barh = bar ((540, -10), -1.8, 0, 0, 20)
barj = bar ((540, -10), 1.5, 0, 0, 600)
bark = bar ((540, -10), -1.5, 0, 0, 1000)
barl = bar ((540, -10), 2.1, 0, 0, 1200)

hearta = liv ((32, 30), 3)
heartb = liv ((72, 30), 2)
heartc = liv ((112, 30), 1)




    













myapp.run()

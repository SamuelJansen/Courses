import pygame as pg

import Frame, Object, Handler, Mouse, Screen

import setting, fatherFunction

import time as now
import os
import ctypes

print('Aplication library imported')

class Application:

    FLOOR = 'FLOOR'

    def __init__(
        self,name,fps,aps,colors,pathMannanger,
        position = [0,0],
        floor = False,
        scaleRange = 1000,
        imagePath = None,
        soundPath = None,
        settingsPath = None
    ):

        self.application = self.father = fatherFunction.absoluteFather(self)
        self.pathMannanger = pathMannanger

        self.name = name
        self.type = Object.ObjectType.APPLICATION

        self.getPaths(imagePath,soundPath,settingsPath)

        self.color = colors

        self.fps = fps
        self.aps = aps
        self.scaleRange = scaleRange

        self.settings = setting.getSettings(self.settingsPath)
        self.size = setting.getAplicationSize(self)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (position[0],position[1])
        self.localMachinePosition = ctypes.windll.user32.SetWindowPos
        pg.mixer.pre_init(44100,16,32,0)
        pg.init()
        pg.display.set_caption(self.name)

        self.setPosition(position)

        self.devScreenSize = (1000,564)
        self.devResize = [self.devScreenSize[0]/self.size[0],self.devScreenSize[1]/self.size[1]]
        print(f'Aplication --> size = {self.size}, devScreenSize = {self.devScreenSize}, devResize = {self.devResize}')

        self.velocityControl = (100 * self.size[0]) / (self.aps * 1920)

        self.longitudesImageOnScreen = 4
        self.latitudesImageOnScreen = 3
        self.blitOrder = 0

        try :
            pg.mixer.init()
        except :
            print("Mixer module not initialized")

        self.fontStyle = 'Comic Sans MS'

        self.frame = None ###- Aplication.initialize() must be called

        self.initializeObjectInterface()

        self.floor = floor
        if self.floor :
            Object.Object(
                Application.FLOOR,
                [0,0],
                self.size,
                self.scaleRange,
                0.0001,
                self.father,
                type = Object.ObjectType.APPLICATION_FLOOR
            )

        self.focus = None
        self.mouse = Mouse.Mouse(self)

        self.running = False

    def initializeObjectInterface(self):
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.image = []
        self.text = None
        self.textPosition = None
        self.textList = []
        self.textPositionList = []
        self.selectable = True
        self.screen = Screen.Screen(self)
        self.handler = Handler.Handler(self)

    def initialize(self,timeNow):
        '''
        It's better to call this method after create all objects'''
        self.timeNow = timeNow
        if self.frame :
            print('Frame already created')
        else :
            self.frame = Frame.Frame(self)
        self.updateScreen()
        self.running = True

    def update(self,timeNow):
        self.timeNow = timeNow
        self.updateFrame()

    def updateFrame(self):
        self.frame.update()
        if self.frame.new :
            self.updateMouse()
            self.updateScreen()

    def updateMouse(self):
        self.mouse.update()

    def updateScreen(self):
        if self.screen.mustUpdate :
            self.screen.surface.fill(self.color['backgroundColor'])
            self.screen.update()
        # self.updatePosition(self.position)
        pg.display.update(self.screen.blitRect)

    def updatePosition(self,position):
        self.setPosition(position)

    def setPosition(self,position):
        self.position = position.copy()
        self.localMachinePosition(
            pg.display.get_wm_info()['window'],
            -1,
            self.position[0], ###- x
            self.position[1], ###- y
            0,
            0,
            0x0001
        )

    def getPaths(self,imagePath,soundPath,settingsPath):
        self.imagePath = imagePath
        self.soundPath = soundPath
        self.settingsPath = settingsPath
        if not self.imagePath :
            self.imagePath = f'{self.pathMannanger.getApiModulePath(self.name)}resourse\\image\\'
        if not self.soundPath :
            self.soundPath = f'{self.pathMannanger.getApiModulePath(self.name)}resourse\\sound\\'
        if not self.settingsPath :
            self.settingsPath = 'resourse/' + self.name + '.ht'

    def getFloor(self):
        if self.floor :
            return self.handler.objects[Application.FLOOR]
        else :
            return self

    def run(self,arrow):
        self.initialize(now.time())
        while self.running :

            if self.frame.apfNew :
                for pgEvent in pg.event.get() :
                    if pgEvent.type == pg.QUIT :
                        self.running = False
                    arrow.newEvent(pgEvent)
                    self.mouse.handleEvent(pgEvent)
                    """
                    if a.arrows[1]==-1 :
                        gl.playSound(upSound)
                    if a.arrows[1]==1 :
                        gl.playSound(downSound)
                    if a.arrows[0]==1 :
                        gl.playMusic('Sounds/TakeaWalk.mp3')
                    if a.arrows[0]==-1 :
                        gl.playSound(leftSound)
                    #"""

            self.update(now.time())
        pg.quit()
        #sys.exit()

import pygame as pg

import Frame, Object, Handler, Mouse, Screen, Session, MemoryOptimizer
import applicationFunction, setting, fatherFunction, objectFunction, imageFunction

import CourseRepository

import time as now
import os
import ctypes

print('Aplication library imported')

class Application:

    def update(self):
        self.timeNow = now.time()
        self.updateFrame()

    def forcedUpdate(self):
        while now.time() < self.frame.timeNext :
            pass
        self.update()

    def __init__(
        self,name,fps,aps,colors,pathMannanger,
        position = [0,0],
        floor = True,
        scaleRange = 1000,
        imagePath = None,
        soundPath = None,
        settingsPath = None
    ):

        self.application = self.tutor = self.father = fatherFunction.absoluteFather(self)
        self.pathMannanger = pathMannanger
        self.extension = self.pathMannanger.getExtension()

        self.repository = CourseRepository.CourseRepository(self)

        self.name = name
        self.type = objectFunction.Type.APPLICATION

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
        self.fontStyle = 'Times New Roman'
        self.fontStyle = 'Calibri'
        self.fontStyle = 'Corbel'
        self.standardFontSize = 18


        self.frame = None ###- Aplication.initialize() must be called

        self.initializeObjectInterface()

        self.setIcon([256,256])

        self.floor = floor
        if self.floor :
            Object.Object(
                applicationFunction.getFloorName(self),
                [0,0],
                self.size,
                self.scaleRange,
                0.0001,
                self.father,
                type = objectFunction.Type.APPLICATION_FLOOR
            )

        self.session = None
        self.sessionClass = Session.Session

        self.memoryOptimizer = MemoryOptimizer.MemoryOptimizer(self)

        self.running = False

    def initializeObjectInterface(self):
        self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        self.image = []
        self.text = None
        self.textPosition = None
        self.textList = []
        self.textPositionList = []
        self.selectable = True
        self.screen = Screen.Screen(self,None)
        self.handler = Handler.Handler(self)
        self.focus = None
        self.clickable = False
        self.functionKey = None
        self.handleEvent = None
        self.singleClickable = False
        self.doubleClickable = False

    def setIcon(self,iconSize):
        self.iconName = f'{self.name}.{applicationFunction.Attribute.ICON}'
        self.iconSize = iconSize
        self.iconPath = f'{imageFunction.getImagePath(self)}{self.iconName}.{applicationFunction.Attribute.IMAGE_EXTENSION}'
        self.icon = imageFunction.getImage(self.iconPath,self.iconSize,self)
        pg.display.set_icon(self.icon)
        return self.icon

    def getPaths(self,imagePath,soundPath,settingsPath):
        self.imagePath = imagePath
        self.soundPath = soundPath
        self.settingsPath = settingsPath
        if not self.imagePath :
            self.imagePath = f'{self.pathMannanger.getApiModulePath(self.name)}resourse\\image\\'
        if not self.soundPath :
            self.soundPath = f'{self.pathMannanger.getApiModulePath(self.name)}resourse\\sound\\'
        if not self.settingsPath :
            self.settingsPath = f'resourse\\{self.name}.{self.extension}'

    def getFloor(self):
        if self.floor :
            return self.handler.objects[applicationFunction.getFloorName(self)]
        else :
            return self

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

    def getAbsoluteOriginalPosition(self):
        return self.handler.getOriginalPosition()

    def initialize(self):
        '''
        It's better to call this method after create all objects'''
        self.timeNow = now.time()
        if self.frame :
            print('Frame already created')
        else :
            self.frame = Frame.Frame(self)
        self.updateScreen()

        self.mouse = Mouse.Mouse(self)
        self.running = True

    def optimizeMemory(self):
        if self.frame.timeNext - self.timeNow > (1 / self.fps) * (2 / 10) :
            self.memoryOptimizer.update()

    def newSession(self,desk,path):
        self.session = self.sessionClass(desk,path)

    def removeSession(self,event):
        if self.session :
            self.session.close(event)

    def updateFrame(self):
        self.frame.update()
        if self.frame.apfNew :
            self.updateMouse()
        if self.frame.new :
            self.updateScreen()
        else :
            self.optimizeMemory()

    def updateScreen(self):
        if self.screen.mustUpdate :
            self.screen.surface.fill(self.color['backgroundColor'])
            self.screen.update()
        ###- keep it below
        ###- self.updatePosition(self.position)
        pg.display.update(self.screen.blitRect)

    def updateMouse(self):
        self.mouse.update()

    def updatePosition(self,position):
        self.setPosition(position)

    def run(self,arrow):
        self.initialize()

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

            self.update()
            # forceObjectsUpdate(self)

        pg.quit()
        #sys.exit()

    def close(self,event):
        self.removeSession(event)
        self.running = False

    def findObjectByName(self,name):
        return self.findObjectByNameInObjectTree(name,self)

    def findObjectByNameInObjectTree(self,name,object):
        for objectSon in object.handler.objects.values() :
            if name in objectSon.getName() :
                return objectSon
            objectFound = self.findObjectByNameInObjectTree(name,objectSon)
            if objectFound :
                return objectFound


def forceObjectsUpdate(object) :
    object.mustUpdate = True
    for objectSon in object.handler.objects.values() :
        forceObjectsUpdate(objectSon)

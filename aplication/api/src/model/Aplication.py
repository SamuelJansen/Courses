import pygame as pg
import time as now
from model import Screen, Frame, Object
import os
import ctypes
from function import setting

class Aplication:
    '''
    It defines the aplication characteristics'''
    def __init__(
        self,name,fps,aps,colors,
        position=(0,0),
        scaleRange=1000,
        imagePath = 'resourse\\image\\',
        soundPath = 'resourse\\sound\\',
        settingsPath = None
    ):
        '''
        Game()
        name    --> It's the aplication's name
        colors  --> It's a dictionary with color's names as keys
        fps     --> frames per second
        apf     --> actions per frame'''
        self.name = name
        self.type = Object.ObjectTypes.APLICATION

        self.imagePath = imagePath
        self.soundPath = soundPath
        if not settingsPath :
            self.settingsPath = 'resourse/' + self.name + '.ht'
        self.color = colors

        self.scaleRange = scaleRange
        self.fps = fps
        self.aps = aps

        self.settings = setting.getSettings(self.settingsPath)
        self.position = position
        pg.mixer.pre_init(44100,16,32,0)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % self.position
        SetWindowPos = ctypes.windll.user32.SetWindowPos
        pg.init()

        pg.display.set_caption(self.name)

        if self.settings['screenSize']==[0,0] :
            self.screenModule = pg.display.set_mode([0,0],pg.FULLSCREEN)
            screenSizeX, screenSizeY = self.screenModule.get_size()
            self.size = [screenSizeX, screenSizeY]
        else :
            self.size = self.settings['screenSize']
        self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA,32)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA,32)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA,32)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF|pg.SRCALPHA)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.SRCALPHA)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.SRCALPHA)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE|pg.DOUBLEBUF)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.HWSURFACE)
        # self.screenModule = pg.display.set_mode(self.size,pg.NOFRAME|pg.DOUBLEBUF)
        # self.screenModule = pg.display.set_mode(self.size)

        SetWindowPos(
            pg.display.get_wm_info()['window'],
            -1,
            self.position[0], ###- x
            self.position[1], ###- y
            0,
            0,
            0x0001 )
        self.velocityControl = (100 * self.size[0]) / (self.aps * 1920)

        self.devScreenSize = (1000,564)
        self.devResize = [self.devScreenSize[0]/self.size[0],self.devScreenSize[1]/self.size[1]]
        print(f'Aplication --> size = {self.size}, devScreenSize = {self.devScreenSize}, devResize = {self.devResize}')

        self.longitudesImageOnScreen = 4
        self.latitudesImageOnScreen = 3
        self.blitOrder = 0

        try :
            pg.mixer.init()
        except :
            print("Mixer module not initialized")

        self.screen = None
        self.frame = None

        self.objectHandler = Object.ObjectHandler()

        self.running = False

    def initialize(self,timeNow):
        '''
        It's better to call this method after create all objects'''
        self.screen = Screen.Screen(self)
        if self.frame :
            print('Frame already created')
        else :
            self.frame = Frame.Frame(timeNow,self)
        self.running = True

    def updateScreen(self):
        '''
        It updates the screen image in the right order.
        Cenario at the background, objects and characteres respecting its places'''
        self.screen.update(self)

    def updateFrame(self,timeNow):
        self.frame.update(timeNow,self)
        if self.frame.new :
            self.updateScreen()

    def update(self,timeNow):
        self.updateFrame(timeNow)

import pygame as pg
import time as now
from model import Screen, Frame, Object
import os
import ctypes
from function import setting, fatherFunction

class Aplication():
    '''
    It defines the aplication characteristics'''
    def __init__(
        self,name,fps,aps,colors,
        position=(0,0),
        scaleRange=1000,
        floor=False,
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

        self.aplication = self.father = fatherFunction.absoluteFather(self)

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
        self.size = setting.getAplicationSize(self)


        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position
        self.localMachinePosition = ctypes.windll.user32.SetWindowPos
        pg.mixer.pre_init(44100,16,32,0)
        pg.init()
        pg.display.set_caption(self.name)

        self.position = None
        self.updatePosition(position)

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


        self.frame = None
        self.objectHandler = Object.ObjectHandler(self)
        self.screen = Screen.Screen(self)

        father = self
        aplication = self

        if floor :
            self.floor = Object.Object(
                self.name,
                [0,0],
                self.size,
                self.scaleRange,
                0.0001,
                father,
                aplication,
                type = Object.ObjectTypes.APLICATION_FLOOR
            )
        else :
            self.floor = None
            self.rect = pg.Rect(self.position[0],self.position[1],self.size[0],self.size[1])

        self.running = False

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
            self.updateScreen()

    def updateScreen(self):
        '''
        It updates the screen image in the right order.
        Cenario at the background, objects and characteres respecting its places'''
        if self.screen.mustUpdate :
            self.screen.surface.fill(self.color['backgroundColor'])
            self.screen.update()
        pg.display.update(self.screen.blitRect)

    def updatePosition(self,position):
        self.position = position
        self.localMachinePosition(
            pg.display.get_wm_info()['window'],
            -1,
            self.position[0], ###- x
            self.position[1], ###- y
            0,
            0,
            0x0001 )

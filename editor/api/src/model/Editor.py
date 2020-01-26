# import Aplication, Object, UserInterface, UserInterfaceSurface, Button
from model import Aplication
from model.object import Object
from model.object.user_interface import UserInterface, UserInterfaceSurface, Header, Button

from model.course import Module

print('Editor library imported')

class Editor(Aplication.Aplication):

    def __init__(self,name,fps,aps,colors,pathMannanger,
        position = (0,0),
        imagePath = None,
        soundPath = None
    ):

        Aplication.Aplication.__init__(self,name,fps,aps,colors,pathMannanger,
            position = position,
            floor = True,
            imagePath = imagePath,
            soundPath = soundPath
        )
        # print(f'Editor.floor.size = {self.floor.size}')

        headderSurfaceName = 'headerSurface'
        headderSurfacePosition  = [0,0]
        headerSurfaceSize = ['100%',22]
        scale = None
        father = self.floor
        Header.Header(
            headderSurfaceName,
            headderSurfacePosition,
            headerSurfaceSize,
            scale,
            father,
            padding = [2,2],
            imagePath = imagePath,
            soundPath = soundPath
        )
        buttonsNameList = ['exit','openModule','close','save','add','launch','update','unlaunch']

        print(f'Editor.objectHandler.objects = {self.objectHandler.objects}')

        buttonSize = ['square','100%']
        for buttonName in buttonsNameList :
            self.floor.objectHandler.objects[headderSurfaceName].addButton(buttonName,buttonSize)

    def newMenuColumn(self):
        pass

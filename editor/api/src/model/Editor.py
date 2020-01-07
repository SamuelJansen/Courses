from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Game,Object
from model import Button

class Editor(Game.Game):

    def __init__(self,name,fps,aps,colors,
        position = (0,0),
        imagePath = pathMannanger.localPath+'Courses/editor/api/src/resourse/image/',
        soundPath = pathMannanger.localPath+'Courses/editor/api/src/resourse/sound/'
    ):

        Game.Game.__init__(self,name,fps,aps,colors,
            position = position,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.workstation = Object.Object(
            self.name,
            '',
            [0,0],
            self.size,
            self.scaleRange,
            0.0001,
            self,
            type=Object.ObjectTypes.USER_INTERFACE
        )

        name = 'exit'
        position = [0,0]
        size = [10,10]
        scale = 50
        functionKey = 'exit'
        father = self.workstation
        self.exitButton = Button.Button(name,position,size,scale,functionKey,self,
            father=father
        )
        self.exitButton.function()
        # print(f'{self.objects[object].name} object is type {self.objects[object].type} and has {self.objects[object].blitOrder} blit order')
        # print(f'Editor.exitButton.getPosition() = {self.exitButton.getPosition()}')

        name = 'exit2'
        position = [0,50]
        self.anotherExitButton = Button.Button(name,position,size,scale,functionKey,self,
            father=father
        )
        # print(f'{self.objects[object].name} object is type {self.objects[object].type} and has {self.objects[object].blitOrder} blit order')

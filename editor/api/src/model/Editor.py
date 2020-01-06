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
        scale = 500
        functionIndex = 'EXIT'
        father = self.workstation
        self.exitButton = Button.Button(name,position,size,scale,functionIndex,self,
            father=self
        )
        print(f'Editor.exitButton.getPosition() = {self.exitButton.getPosition()}')

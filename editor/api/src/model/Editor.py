from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Aplication,Object
from model import Button

class Editor(Aplication.Aplication):

    def __init__(self,name,fps,aps,colors,
        position = (0,0),
        imagePath = pathMannanger.localPath+'Courses\\editor\\api\\src\\resourse\\image\\',
        soundPath = pathMannanger.localPath+'Courses\\editor\\api\\src\\resourse\\sound\\'
    ):

        Aplication.Aplication.__init__(self,name,fps,aps,colors,
            position = position,
            imagePath = imagePath,
            soundPath = soundPath
        )

        father = self
        aplication = self

        self.workstation = Object.Object(
            self.name,
            [0,0],
            self.size,
            self.scaleRange,
            0.0001,
            # self,
            # self,
            father,
            aplication,
            type = Object.ObjectTypes.USER_INTERFACE
        )

        print(f'Editor.workstation.size = {self.workstation.size}')

        previousPosition = [0,0]
        size = [15,15]
        father = self.workstation
        aplication = self
        self.headerButtons = {}
        self.headderButtonsName = ['exit','unlaunch','launch','update']
        for buttonName in self.headderButtonsName :
            name = buttonName + '_pressed'
            position = [previousPosition[0]+1,1]
            previousPosition = position.copy()
            previousPosition[0] += size[0]
            functionKey = name[:-8]

            self.headerButtons[buttonName] = Button.Button(
                name,
                position,
                functionKey,
                father,
                aplication,
                size=size
            )


        # self.exitButton.run(self)

        # print(f'{self.objects[object].name} object is type {self.objects[object].type} and has {self.objects[object].blitOrder} blit order')
        # print(f'Editor.exitButton.getPosition() = {self.exitButton.getPosition()}')

        # name = 'exit2'
        # position = [0,50]
        # self.anotherExitButton = Button.Button(name,position,size,scale,functionKey,self,
        #     father=father
        # )
        # print(f'{self.objects[object].name} object is type {self.objects[object].type} and has {self.objects[object].blitOrder} blit order')

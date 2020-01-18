from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Aplication, Object, UserInterface,UserInterfaceSurface
from model import Button
from model.course import Module

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
        print(f'Editor.floor.size = {self.floor.size}')

        headderSurfaceName = 'headerSurface'
        headderSurfacePosition  = [0,0]
        headerSurfaceSize = ['100%',22]
        scale = None
        father = self.floor
        aplication = self
        self.headerSurface = UserInterfaceSurface.UserInterfaceSurface(
            headderSurfaceName,
            headderSurfacePosition,
            headerSurfaceSize,
            scale,
            father,
            aplication,
            imagePath = None,
            soundPath = None
        )
        self.headerButtons = {}
        self.headerButtonsName = ['exit','open','close','save','add','launch','update','unlaunch']

        initialPosition = [0,0]
        padding = [2,2]
        self.instanciateHeaderButtons(initialPosition,padding,self.headerSurface)
        self.instanciateCreateButtons()

    def instanciateHeaderButtons(self,initialPosition,padding,father):

        previousPosition = initialPosition
        size = ['square','100%']
        size = UserInterface.parseSize(size,father)
        size = UserInterface.getSizePadded(size,padding)
        aplication = self

        for buttonName in self.headerButtonsName :
            name = buttonName #+ '_pressed'
            position = [previousPosition[0],0]
            position = UserInterface.getPositionPadded(position,padding)#+padding[0],+padding[1]]
            previousPosition = position.copy()
            previousPosition[0] += size[0]
            functionKey = name#[:-8]

            self.headerButtons[buttonName] = Button.Button(
                name,
                position,
                functionKey,
                father,
                aplication,
                size=size,
                padding=padding
            )

    def instanciateCreateButtons(self):
        modulesPath = pathMannanger.getApiModulePath('course') + Module.Module.MODULES_FILE

        modules = []
        with open(modulesPath,"r",encoding="utf-8") as modulesFile :
            for line in modulesFile :
                modules.append(line.strip())
        print(modules)

    def instanciateSelectButtons(self):
        pass

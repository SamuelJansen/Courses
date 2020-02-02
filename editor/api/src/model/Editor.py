import Application, Header

from model.course import Module

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headderSurfaceName = 'headerSurface'
        headderSurfacePosition  = [0,0]
        headerSurfaceSize = ['100%',22]
        father = self.getFloor()
        print(f'Editor father.name = {father.name}, father type = {father.type}')

        headder = Header.Header(
            headderSurfaceName,
            headderSurfacePosition,
            headerSurfaceSize,
            father,
            padding = [2,2],
            imagePath = self.imagePath,
            soundPath = self.soundPath
        )
        buttonsNameList = ['exit','openModule','close','save','add','launch','update','unlaunch']

        print(f'Editor.handler.objects = {self.handler.objects}')

        buttonSize = ['square','100%']
        for buttonName in buttonsNameList :
            headder.addButton(buttonName,buttonSize)

    def newMenuColumn(self):
        pass

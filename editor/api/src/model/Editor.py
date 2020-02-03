import Application, Header, Surface

from model.course import Module

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerName = 'headerSurface'
        headerPosition  = [0,0]
        headerSize = ['100%',22]
        headerFather = self.getFloor()
        print(f'Editor headerFather.name = {headerFather.name}, type = {headerFather.type}')

        buttonsNameList = ['exit','openModule','close','save','add','launch','update','unlaunch']
        buttonSize = [Surface.Surface.SQUARE,'100%']
        header = Header.Header(
            headerName,
            headerPosition,
            headerSize,
            headerFather,
            itemsName = buttonsNameList,
            itemSize = buttonSize,
            padding = [2,2]
        )

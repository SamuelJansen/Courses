import Application, Header
import surfaceFunction, headerFunction

import exit, openModule, close, save, add, launch, update, unlaunch

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerName = headerFunction.Attribute.NAME
        headerPosition  = [0,0]
        headerSize = ['100%',22]
        headerFather = self.getFloor()

        header = Header.Header(
            headerName,
            headerPosition,
            headerSize,
            headerFather,
            itemsName = ['exit','openModule','close','save','add','launch','update','unlaunch'],
            itemsExternalFunction = [
                exit.exit,
                openModule.openModule,
                close.close,
                save.save,
                add.add,
                launch.launch,
                update.update,
                unlaunch.unlaunch
            ],
            itemSize = [surfaceFunction.Types.SQUARE,'100%'],
            itemsImagePath = f'{self.application.pathMannanger.getApiModulePath(self.application.name)}resourse\\button\\image\\',
            itemsAudioPath = f'{self.application.pathMannanger.getApiModulePath(self.application.name)}resourse\\button\\audio\\',
            padding = [2,2]
        )

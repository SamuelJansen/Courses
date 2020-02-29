import Application, Header
import surfaceFunction, headerFunction, setting

import ItemDto
import exit, openModule, closeModule, save, add, launch, update, unlaunch

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerName = headerFunction.Attribute.NAME
        headerPosition  = [0,0]
        headerSize = ['100%',22]
        headerFather = self.getFloor()

        headerItems = [
            ItemDto.ItemDto('exit',exit.exit),
            ItemDto.ItemDto('openModule',openModule.openModule),
            ItemDto.ItemDto('closeModule',closeModule.closeModule),
            ItemDto.ItemDto('save',save.save),
            ItemDto.ItemDto('add',add.add),
            ItemDto.ItemDto('launch',launch.launch),
            ItemDto.ItemDto('update',update.update),
            ItemDto.ItemDto('unlaunch',unlaunch.unlaunch)
        ]

        Header.Header(
            headerName,
            headerPosition,
            headerSize,
            headerFather,
            items = headerItems,
            itemSize = [surfaceFunction.Types.SQUARE,'100%'],
            itemsImagePath = f'{self.application.pathMannanger.getApiModulePath(self.application.name)}resourse\\header\\image\\',
            itemsAudioPath = f'{self.application.pathMannanger.getApiModulePath(self.application.name)}resourse\\header\\audio\\',
            padding = [2,2]
        )

    def getHeaderNames(self):
        return setting.getFileNames(f'{self.application.pathMannanger.getApiModulePath(self.application.name)}event\\header\\','py')

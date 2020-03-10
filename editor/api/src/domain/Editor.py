import Application, Header
import surfaceFunction, headerFunction, setting, applicationFunction

import ItemDto
import exit, openModule, closeModule, save, add, launch, update, unlaunch

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerName = headerFunction.Attribute.NAME
        headerPosition  = [0,0]
        headerSize = ['100%',20]
        headerFather = self.getFloor()
        priority = applicationFunction.Priority.HIGHT

        headerItems = [
            ItemDto.ItemDto('exit',onLeftClick=exit.exit,priority=priority),
            ItemDto.ItemDto('openModule',onLeftClick=openModule.openModule,priority=priority),
            ItemDto.ItemDto('closeModule',onLeftClick=closeModule.closeModule,priority=priority),
            ItemDto.ItemDto('save',onLeftClick=save.save,priority=priority),
            ItemDto.ItemDto('add',onLeftClick=add.add,priority=priority),
            ItemDto.ItemDto('launch',onLeftClick=launch.launch,priority=priority),
            ItemDto.ItemDto('update',onLeftClick=update.update,priority=priority),
            ItemDto.ItemDto('unlaunch',onLeftClick=unlaunch.unlaunch,priority=priority)
        ]

        Header.Header(
            headerName,
            headerPosition,
            headerSize,
            headerFather,
            items = headerItems,
            itemSize = [surfaceFunction.Types.SQUARE,'100%'],
            padding = [1,1]
        )

import Application, Header
import surfaceFunction

from event.exit import *
from event.openModule import *
from event.close import *
from event.save import *
from event.add import *
from event.launch import *
from event.update import *
from event.unlaunch import *

from model.course import Module

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerName = 'headerSurface'
        headerPosition  = [0,0]
        headerSize = ['100%',22]
        headerFather = self.getFloor()

        header = Header.Header(
            headerName,
            headerPosition,
            headerSize,
            headerFather,
            itemsName = ['exit','openModule','close','save','add','launch','update','unlaunch'],
            itemsExternalFunction = [exit,openModule,close,save,add,launch,update,unlaunch],
            itemSize = [surfaceFunction.Types.SQUARE,'100%'],
            padding = [2,2]
        )

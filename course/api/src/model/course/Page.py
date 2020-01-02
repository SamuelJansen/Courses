from function import importMannanger
userPath = importMannanger.makeAplicationLibrariesAvaliable()
from model import Object

class Page(Object.Object):
    def __init__(self,name,lesson,objects,plataform):
        self.name = name
        self.lesson = lesson
        self.objects = objects
        pagePosition = [0,0]
        pageSize = plataform.app.size
        pageScale = plataform.app.scaleRange
        pageVelocity = 0.0001
        Object.Object.__init__(
            self,
            self.name,
            self.lesson,
            pagePosition,
            pageSize,
            pageScale,
            pageVelocity,
            plataform.app
        )

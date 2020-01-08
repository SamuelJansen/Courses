from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Object

class Page(Object.Object):
    def __init__(self,name,lessonName,objects,plataform):
        self.name = name
        self.lessonName = lessonName
        pagePosition = [0,0]
        pageSize = plataform.size
        pageScale = plataform.scaleRange
        pageVelocity = 0.0001

        folder = self.lessonName
        position = pagePosition
        size = pageSize
        scale = pageScale
        velocity = pageVelocity

        Object.Object.__init__(
            self,
            name,
            folder,
            position,
            size,
            scale,
            velocity,
            plataform
        )
        self.objects = objects

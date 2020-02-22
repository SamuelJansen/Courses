import Object
import surfaceFunction, objectFunction, eventFunction

print('UserInterfaceSurface library imported')

class Surface(Object.Object):

    def __init__(self,name,position,size,father,
        externalEvent = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        size = surfaceFunction.parseSize(size,father)
        velocity = 0.00001

        Object.Object.__init__(
            self,
            name,
            position,
            size,
            scale,
            velocity,
            father,
            type = objectFunction.Type.USER_INTERFACE,
            externalEvent = externalEvent,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = soundPath
        )

        if padding :
            self.padding = padding
        else :
            self.padding = [0,0]

        self.userInterfaceSurface = self

        self.handler.fixOriginalPosition()
        self.handler.fixOriginalSize()

        # if eventFunction.Type.MODAL not in self.handler.inheritanceTree :
        #     try :
        #         print(f'Surface: name = {self.name}, position = {self.position}, originalPosition = {self.handler.originalPosition}, size = {self.size}, originalSize = {self.handler.originalSize}, padding = {self.padding}')
        #     except :
        #         print(f'Surface: name = {self.name}, position = {self.position}, originalPosition = {self.handler.originalPosition}, size = {self.size}, originalSize = {self.handler.originalSize}, padding = noPadding')
        #     try :
        #         print(f'        father = {self.father.name}, position = {self.father.position}, originalPosition = {self.father.handler.originalPosition}, size = {self.father.size}, originalSize = {self.father.handler.originalSize}, padding = {self.father.padding}')
        #     except :
        #         print(f'        father = {self.father.name}, position = {self.father.position}, originalPosition = {self.father.handler.originalPosition}, size = {self.father.size}, originalSize = {self.father.handler.originalSize}, padding = noPadding')
        #     try :
        #         print(f'        tutor = {self.tutor.name}, position = {self.tutor.position}, originalPosition = {self.tutor.handler.originalPosition}, size = {self.tutor.size}, originalSize = {self.tutor.handler.originalSize}, padding = {self.tutor.padding}')
        #     except :
        #         print(f'        tutor = {self.tutor.name}, position = {self.tutor.position}, originalPosition = {self.tutor.handler.originalPosition}, size = {self.tutor.size}, originalSize = {self.tutor.handler.originalSize}, padding = noPadding')

    def getAbsolutePosition(self):
        if self.father.type == objectFunction.Type.APPLICATION :
            return self.getPosition()
        else :
            position = self.getPosition()
            fatherAbsoluteOriginalPosition = self.father.getAbsoluteOriginalPosition()
            return [
                position[0] + fatherAbsoluteOriginalPosition[0],
                position[1] + fatherAbsoluteOriginalPosition[1]
            ]

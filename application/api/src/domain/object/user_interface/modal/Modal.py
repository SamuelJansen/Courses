import UserInterface
import surfaceFunction, eventFunction

print('Modal library imported')

class Modal(UserInterface.UserInterface):

    def __init__(self,name,size,father,
        type = None,
        position = None,
        text = None,
        textPosition = None,
        fontSize = None,
        scale = None,
        padding = None,
        onLeftClick = None,
        onMenuResolve = None,
        onMessageResolve = None,
        noImage = True,
        surfaceColor = None,
        imagePath = None,
        audioPath = None
    ):

        name,position,padding,originalPadding,keepFatherImage,father,tutor = self.getModalFatherAttributes(name,position,padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            type = type,
            text = text,
            textPosition = textPosition,
            fontSize = fontSize,
            scale = scale,
            padding = padding,
            onLeftClick = onLeftClick,
            onMenuResolve = onMenuResolve,
            noImage = noImage,
            surfaceColor = surfaceColor,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.setModalTutorAttributes(originalPadding,keepFatherImage,tutor)

        ###- print(f'{self.name} created, father = {self.father.name}, tutor = {self.tutor.name}, type = {self.type}, blit order = {self.blitOrder}')

        # if eventFunction.Type.MODAL in self.handler.inheritanceTree :
        #     try :
        #         print(f'Modal:  name = {self.name}, position = {self.position}, originalPosition = {self.handler.originalPosition}, size = {self.size}, originalSize = {self.handler.originalSize}, padding = {self.padding}')
        #     except :
        #         print(f'Modal:  name = {self.name}, position = {self.position}, originalPosition = {self.handler.originalPosition}, size = {self.size}, originalSize = {self.handler.originalSize}, padding = noPadding')
        #     try :
        #         print(f'        father = {self.father.name}, position = {self.father.position}, originalPosition = {self.father.handler.originalPosition}, size = {self.father.size}, originalSize = {self.father.handler.originalSize}, padding = {self.father.padding}')
        #     except :
        #         print(f'        father = {self.father.name}, position = {self.father.position}, originalPosition = {self.father.handler.originalPosition}, size = {self.father.size}, originalSize = {self.father.handler.originalSize}, padding = noPadding')
        #     try :
        #         print(f'        tutor = {self.tutor.name}, position = {self.tutor.position}, originalPosition = {self.tutor.handler.originalPosition}, size = {self.tutor.size}, originalSize = {self.tutor.handler.originalSize}, padding = {self.tutor.padding}')
        #     except :
        #         print(f'        tutor = {self.tutor.name}, position = {self.tutor.position}, originalPosition = {self.tutor.handler.originalPosition}, size = {self.tutor.size}, originalSize = {self.tutor.handler.originalSize}, padding = noPadding')


    def getModalFatherAttributes(self,name,position,padding,father):
        name += f'.{father.name}'
        if not position :
            position = father.getAbsoluteOriginalPosition().copy()
            keepFatherImage = True
        else :
            keepFatherImage = False
        padding,originalPadding = surfaceFunction.stashPadding(padding,father)
        tutor = father
        father = father.application.getFloor()
        return name,position,padding,originalPadding,keepFatherImage,father,tutor

    def setModalTutorAttributes(self,originalPadding,keepFatherImage,tutor):
        self.padding = originalPadding
        self.handler.setTutor(tutor)
        if keepFatherImage :
            self.handler.addTutorImage(self.tutor,surfaceFunction.getPositionPadded([0,0],self.padding))
        # self.father.screen.mustUpdateNextFrame()

    def getName(self):
        return self.name.split('.')[0]

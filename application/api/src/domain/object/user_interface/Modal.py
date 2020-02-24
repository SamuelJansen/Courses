import UserInterface
import surfaceFunction, eventFunction

print('Modal library imported')

class Modal(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        externalFunction = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        audioPath = None
    ):

        name,position,padding,originalPadding,father,tutor = self.getModalFatherAttributes(name,padding,father)

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            externalFunction = externalFunction,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            audioPath = imagePath
        )

        self.setModalTutorAttributes(tutor,originalPadding)

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


    def getModalFatherAttributes(self,name,padding,father):
        name += f'.{father.name}'
        position = father.getAbsoluteOriginalPosition()
        padding,originalPadding = surfaceFunction.stashPadding(padding,father)
        tutor = father
        father = father.application.getFloor()
        return name,position,padding,originalPadding,father,tutor

    def setModalTutorAttributes(self,tutor,originalPadding):
        self.padding = originalPadding
        self.handler.setTutor(tutor)
        self.handler.addTutorImage(self.tutor,surfaceFunction.getPositionPadded([0,0],self.padding))

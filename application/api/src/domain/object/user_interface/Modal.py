import UserInterface
import surfaceFunction

print('Modal library imported')

class Modal(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        eventFunction = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        name,position,padding,originalPadding,father,tutor = self.getModalFatherAttributes(name,padding,father)

        UserInterface.UserInterface.__init__(
            self,name,position,size,father,
            eventFunction = eventFunction,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.setModalTutorAttributes(tutor,originalPadding)

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

import UserInterface
import modalFunction, surfaceFunction

print('Modal library imported')

class Modal(UserInterface.UserInterface):

    NAME = 'Modal'

    def __init__(self,name,position,size,father,
        functionKey = None,
        scale = None,
        padding = None,
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        father,tutor,position,padding,originalPadding = self.getModalFatherAttributes(padding,father)

        UserInterface.UserInterface.__init__(
            self,name,position,size,father,
            functionKey = functionKey,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.setModalTutorAttributes(tutor,originalPadding)

    def getModalFatherAttributes(self,padding,father):
        position = father.getAbsoluteOriginalPosition()
        padding,originalPadding = modalFunction.stashPadding(padding,father)
        tutor = father
        father = father.application.getFloor()
        return father,tutor,position,padding,originalPadding

    def setModalTutorAttributes(self,tutor,originalPadding):
        self.tutor = tutor
        self.blitOrder = self.tutor.blitOrder + 1
        self.userInterfaceSurface = self.tutor.userInterfaceSurface
        self.padding = originalPadding
        self.handler.addTutor(self.tutor,surfaceFunction.getPositionPadded([0,0],self.padding))

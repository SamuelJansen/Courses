from model import Object

class UserInterface(Object.Object):

    def __init__(self,name,position,size,scale,father,plataform,
        imagePath = None,
        soundPath = None
    ):

        velocity = 0.00001

        Object.Object.__init__(
            self,name,position,size,scale,velocity,father,plataform,
            type = Object.ObjectTypes.USER_INTERFACE,
            imagePath = imagePath,
            soundPath = soundPath
        )

import UserInterface

print('Button library imported')

class Button(UserInterface.UserInterface):

    def __init__(self,name,position,size,father,
        externalFunction = None,
        padding = None,
        imagePath = None,
        audioPath = None
    ):

        UserInterface.UserInterface.__init__(self,name,position,size,father,
            externalFunction = externalFunction,
            padding = padding,
            imagePath = imagePath,
            audioPath = audioPath
        )

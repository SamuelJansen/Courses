from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface
from function.eventFunction import eventFunctions, getFunctionKey

class Button(UserInterface.UserInterface):

    def __init__(
        self,name,position,functionKey,father,
        size=None,
        padding=None,
        scale=None,
        imagePath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/image/',
        soundPath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/sound/'
    ):

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.functionKey = getFunctionKey(functionKey)
        self.run = eventFunctions[self.functionKey]

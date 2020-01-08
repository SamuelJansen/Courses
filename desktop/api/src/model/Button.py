from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface

class Button(UserInterface.UserInterface):

    functions = {}
    function = (lambda functions=functions : lambda function:functions.setdefault(function.__name__,function))()

    @function
    def nextPage(inputDictionary) :
        print(f'    function called: nextPage({inputDictionary})')
        pass

    @function
    def previousPage(inputDictionary) :
        print(f'    function called: previousPage({inputDictionary})')
        pass

    @function
    def exit():
        print(f'    function called: exit()')
        pass

    def __init__(
        self,name,position,size,scale,functionKey,father,plataform,
        imagePath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/image/',
        soundPath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/sound/'
    ):

        velocity = 0.00001

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,plataform,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.functionKey = functionKey
        self.callFunction = Button.functions[self.functionKey]

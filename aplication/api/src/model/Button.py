from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface

class Button(UserInterface.UserInterface):

    functions = {}
    function = (lambda functions=functions : lambda function:functions.setdefault(function.__name__,function))()

    @function
    def exit(aplication) :
        aplication.running = False
        print(f'    function called: exit({aplication.name})')
        pass

    @function
    def nextPage(aplication) :
        print(f'    function called: nextPage({aplication.name})')
        pass

    @function
    def previousPage(aplication) :
        print(f'    function called: previousPage({aplication.name})')
        pass

    @function
    def unlaunch(aplication) :
        print(f'    function called: unlaunch({aplication.name})')
        pass

    @function
    def launch(aplication) :
        print(f'    function called: launch({aplication.name})')
        pass

    @function
    def update(aplication) :
        print(f'    function called: update({aplication.name})')
        pass

    def __init__(
        self,name,position,functionKey,father,aplication,
        size=None,
        padding=None,
        scale=None,
        imagePath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/image/',
        soundPath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/sound/'
    ):

        velocity = 0.00001

        UserInterface.UserInterface.__init__(
            self,name,position,size,scale,father,aplication,
            imagePath = imagePath,
            soundPath = soundPath
        )

        self.functionKey = functionKey
        self.run = Button.functions[self.functionKey]

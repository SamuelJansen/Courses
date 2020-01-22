from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface
from function.eventFunction import eventFunctions

class Button(UserInterface.UserInterface):

    # functions = {}
    # function = (lambda functions=functions : lambda function:functions.setdefault(function.__name__,function))()

    # @function
    # def exit(object) :
    #     # object.aplication.running = False
    #     exitAplication.exitAplication(object)
    #     print(f'    function called: exit({object.aplication.name})')
    #
    # @function
    # def unlaunch(object) :
    #     object.father.objectHandler.deleteObject(object.name)
    #     print(f'    function called: unlaunch({object.aplication.name})')
    #
    # @function
    # def launch(object) :
    #     print(f'    function called: launch({object.aplication.name})')
    #     pass
    #
    # @function
    # def update(object) :
    #     print(f'    function called: update({object.aplication.name})')
    #     pass
    #
    # @function
    # def add(object) :
    #     modulesPath = pathMannanger.getApiModulePath('course') + Module.Module.MODULES_FILE
    #     modules = []
    #     with open(modulesPath,"r",encoding="utf-8") as modulesFile :
    #         for line in modulesFile :
    #             modules.append(line.strip())
    #     print(modules)
    #     print(f'    function called: add({object.aplication.name})')
    #     pass
    #
    # @function
    # def close(object) :
    #     print(f'    function called: adclosed({object.aplication.name})')
    #     pass
    #
    # @function
    # def open(object) :
    #     print(f'    function called: open({object.aplication.name})')
    #     pass
    #
    # @function
    # def save(object) :
    #     print(f'    function called: save({object.aplication.name})')
    #     pass
    #
    # @function
    # def nextPage(object) :
    #     print(f'    function called: nextPage({object.aplication.name})')
    #     pass
    #
    # @function
    # def previousPage(object) :
    #     print(f'    function called: previousPage({object.aplication.name})')
    #     pass

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

        self.functionKey = functionKey
        # self.run = Button.functions[self.functionKey]
        self.run = eventFunctions[self.functionKey]

from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface

class Button(UserInterface.UserInterface):

    functions = {}
    function = (lambda functions=functions : lambda function:functions.setdefault(function.__name__,function))()

    @function
    def exit(object) :
        object.aplication.running = False
        print(f'    function called: exit({object.aplication.name})')
        pass

    @function
    def unlaunch(object) :
        print(f'    function called: unlaunch({object.aplication.name})')
        print(f'''object.father.objectHandler.objects[{object.name}].name = {object.father.objectHandler.objects[object.name].name}''')
        object.father.objectHandler.deleteObject(object.name)
        print('object.father.objectHandler.objects:')
        for name in object.father.objectHandler.objects :
            print(f'    - {name}')

    @function
    def launch(object) :
        print(f'    function called: launch({object.aplication.name})')
        pass

    @function
    def update(object) :
        print(f'    function called: update({object.aplication.name})')
        pass

    @function
    def add(object) :
        print(f'    function called: add({object.aplication.name})')
        pass

    @function
    def close(object) :
        print(f'    function called: adclosed({object.aplication.name})')
        pass

    @function
    def open(object) :
        print(f'    function called: open({object.aplication.name})')
        pass

    @function
    def save(object) :
        print(f'    function called: save({object.aplication.name})')
        pass

    @function
    def nextPage(object) :
        print(f'    function called: nextPage({object.aplication.name})')
        pass

    @function
    def previousPage(object) :
        print(f'    function called: previousPage({object.aplication.name})')
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

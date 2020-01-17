from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import UserInterface

class Button(UserInterface.UserInterface):

    functions = {}
    function = (lambda functions=functions : lambda function:functions.setdefault(function.__name__,function))()

    @function
    def exit(object,aplication) :
        aplication.running = False
        print(f'    function called: exit({aplication.name})')
        pass

    @function
    def unlaunch(object,aplication) :
        print(f'''object.father.objectHandler.objects[{object.name}].name = {object.father.objectHandler.objects[object.name].name}''')
        tab = '    '
        del object.father.objectHandler.objects[object.name]
        print('object.father.objectHandler.objects:')
        for name in object.father.objectHandler.objects :
            print(f'{tab}- {name}')
        object.father.updateScreen()
        print(f'    function called: unlaunch({aplication.name})')
        pass

    @function
    def launch(object,aplication) :
        print(f'    function called: launch({aplication.name})')
        pass

    @function
    def update(object,aplication) :
        print(f'    function called: update({aplication.name})')
        pass

    @function
    def add(object,aplication) :
        print(f'    function called: add({aplication.name})')
        pass

    @function
    def close(object,aplication) :
        print(f'    function called: adclosed({aplication.name})')
        pass

    @function
    def open(object,aplication) :
        print(f'    function called: open({aplication.name})')
        pass

    @function
    def save(object,aplication) :
        print(f'    function called: save({aplication.name})')
        pass

    @function
    def nextPage(object,aplication) :
        print(f'    function called: nextPage({aplication.name})')
        pass

    @function
    def previousPage(object,aplication) :
        print(f'    function called: previousPage({aplication.name})')
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

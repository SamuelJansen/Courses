from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Object
from function import buttonFunction

# buttonFunctions = {}
# buttonFunction = lambda function:buttonFunctions.setdefault(function.__name__,function)
#
# @buttonFunction
# def nextPage(input) :
#     print(f'    function called: goNextPage({input})')
#     pass
#
# @buttonFunction
# def previousPage(input) :
#     print(f'    function called: goPreviousPage({input})')
#     pass
#
# @buttonFunction
# def exit():
#     print(f'    function called: exit()')
#     pass

class Button(Object.Object):

    # functionDictionary = {
    #     'exit' : Button.exit,
    #     'previousPage' : Button.goNextPage,
    #     'nextPage' : Button.goPreviousPage
    # }

    def __init__(self,name,position,size,scale,functionKey,aplication,
            father=None,
            imagePath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/image/',
            soundPath = pathMannanger.localPath+'Courses/desktop/api/src/resourse/button/sound/'
        ):

        game = aplication
        folder = ''
        velocity = 0.00001

        Object.Object.__init__(
          self,
          name,
          folder,
          position,
          size,
          scale,
          velocity,
          game,
          imagePath = imagePath,
          soundPath = soundPath,
          father = father
        )
        self.functionKey = functionKey

    def function(self):
        buttonFunction.buttonFunctions[self.functionKey]()

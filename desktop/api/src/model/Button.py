from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Object


def goNextPage(input) :
    print(f'    function called: goNextPage({input})')
    pass

def goPreviousPage(input) :
    print(f'    function called: goPreviousPage({input})')
    pass

def exit():
    print(f'    function called: exit()')
    pass


class Button(Object.Object):
    functionDictionary = {
        'EXIT' : exit,
        'PREVIOUS_PAGE' : goNextPage,
        'NEXT_PAGE' : goPreviousPage
    }
    def __init__(self,name,position,size,scale,functionIndex,aplication,
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
          soundPath = soundPath
        )
        self.function = Button.functionDictionary[functionIndex]
        # father.addNewObject(self)

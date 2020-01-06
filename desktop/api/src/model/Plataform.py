from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Game

class Plataform(Game.Game):
    def __init__(self,name,fps,aps,colors,
        position=(0,0),
        imagePath = pathMannanger.localPath+'Courses/course/api/src/resourse/image/',
        soundPath = pathMannanger.localPath+'Courses/course/api/src/resourse/sound/'
    ):

        self.localPath = pathMannanger.localPath

        Game.Game.__init__(self,name,fps,aps,colors,
            position=position,
            imagePath=imagePath,
            soundPath=soundPath
        )

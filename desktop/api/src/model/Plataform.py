from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Game

class Plataform:
    def __init__(self,name,fps,aps,colors,
        imagePath = pathMannanger.localPath+'Courses/course/api/src/resourse/image/',
        soundPath = pathMannanger.localPath+'Courses/course/api/src/resourse/sound/',
    ):
        self.localPath = pathMannanger.localPath
        self.app = Game.Game(name,fps,aps,colors,imagePath=imagePath,soundPath=soundPath)

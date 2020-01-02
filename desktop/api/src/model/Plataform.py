from function import importMannanger
userPath = importMannanger.makeAplicationLibrariesAvaliable()
from model import Game

class Plataform:
    def __init__(self,name,fps,aps,colors,
        imagePath = userPath+'Courses/course/api/src/resourse/image/',
        soundPath = userPath+'Courses/course/api/src/resourse/sound/',
    ):
        self.app = Game.Game(name,fps,aps,colors,imagePath=imagePath,soundPath=soundPath)

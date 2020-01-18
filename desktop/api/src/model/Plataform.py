from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Aplication

class Plataform(Aplication.Aplication):
    def __init__(self,name,fps,aps,colors,
        position=(0,0),
        imagePath = pathMannanger.localPath+'Courses/course/api/src/resourse/image/',
        soundPath = pathMannanger.localPath+'Courses/course/api/src/resourse/sound/'
    ):

        Aplication.Aplication.__init__(self,name,fps,aps,colors,
            position=position,
            imagePath=imagePath,
            soundPath=soundPath
        )

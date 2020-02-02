import Aplication

print('Plataform library imported')

class Plataform(Aplication.Aplication):
    def __init__(self,name,fps,aps,colors,pathMannanger,
        position=(0,0),
        imagePath = None,
        soundPath = None
    ):

        Aplication.Aplication.__init__(self,name,fps,aps,colors,pathMannanger,
            position=position,
            imagePath=imagePath,
            soundPath=soundPath
        )

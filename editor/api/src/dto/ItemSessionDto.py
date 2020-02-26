class ItemSessionDto:

    def __init__(self,name,size,father,externalFunction,imagePath,audioPath):
        self.name = name
        self.size = size.copy()
        self.father = father
        self.externalFunction = externalFunction
        self.imagePath = imagePath
        self.audioPath = audioPath

class Lesson:
    def __init__(self,name,pages,module):

        self.module = module
        self.plataform = self.module.plataform

        self.name = name

        self.pages = pages

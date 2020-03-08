import Application, Object

import CourseRepository

print('Plataform library imported')

class Plataform(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)
        
        self.applicatonUser = None

    def setApplicationUser(self,registration,password):
        self.registration = registration
        self.password = password
        self.applicatonUser = self.repository.getApplicationUser()

        moduleName = 'Robótica 1'
        lessonName = 'Aula 01'
        # self.pageNames = list(self.applicatonUser.courses[moduleName][lessonName].keys())
        self.pageNames = list(self.applicatonUser.courses[moduleName][lessonName].keys())
        self.allPageNames = self.repository.getAllPageNames(moduleName,lessonName)
        print(f'self.allPageNames = {self.allPageNames}')
        self.pagePointer = 10
        self.pagesImagePath = f'''{self.application.pathMannanger.getApiModulePath('course')}resourse\\modules\\{moduleName}\\{lessonName}\\image\\'''

    def nextPage(self):
        self.removePage()
        self.pagePointer += 1
        self.buildPage()

    def buildPage(self):

        Object.Object(
            self.allPageNames[self.pagePointer],
            [0,0],
            self.size,
            None,
            0.00001,
            self,
            imagePath = self.pagesImagePath
        )

    def removePage(self):
        self.handler.removeObjectTree(self.allPageNames[self.pagePointer])

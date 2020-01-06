from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from function import registrationFunction

class AplicationUser:

    def __init__(self,registration,password,coursesName=None):
        self.registration = registration
        self.password = password
        self.courses = []
        if coursesName :
            self.courses = registrationFunction.getCourses(coursesName)
        self.presentCourse = None
        self.presentModule = None
        self.presentLesson = None

    def addCourse(self,course):
        self.courses.append(course)

    def getLessonPath():
        self.presentCourse = 'macro-2020-03'
        self.presentModule = 'assistente_administrativo'
        self.presentLesson = 'aula1'
        presentLessonPath = pathMannanger.getApiModulePath('course')+'resourse/modules/'+self.presentModule+'/'+self.presentLesson+'/script.ht'
        return presentLessonPath

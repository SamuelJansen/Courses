from function import registrationFunction

class ApplicationUser:

    def __init__(self,registration,password,plataform,coursesName=None):
        self.registration = registration
        self.password = password
        self.courses = []
        if coursesName :
            self.courses = registrationFunction.getCourses(coursesName,plataform)
        self.presentCourse = None
        self.presentModule = None
        self.presentLesson = None

    def addCourse(self,course):
        self.courses.append(course)

    def getLessonPath(plataform):
        ###- this method needs some function later on
        self.presentCourse = 'macro_2020_03'
        self.presentModule = 'assistente_administrativo'
        self.presentLesson = 'aula1'
        presentLessonPath = plataform.pathMannanger.getApiModulePath('course')+'resourse/modules/'+self.presentModule+'/'+self.presentLesson+'/script.ht'
        return presentLessonPath

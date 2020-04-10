import CourseRepository

class ApplicationUser:

    def __init__(self,registration,password,application,
        courseNames = None
    ):
        self.registration = registration
        self.password = password
        self.application = application
        self.courses = {}
        self.allPageNames = None

    def getPageName(self,pageNameData):
        return pageNameData.split()[1]

    def getAllPageNames(self,moduleName,lessonName):
        return self.application.repository.getAllPageNames(moduleName,lessonName)

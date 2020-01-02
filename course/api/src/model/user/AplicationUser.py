class AplicationUser:
    def __init__(self,registration):
        self.registration = registration
        self.courses = []
        self.course = 'macro-2020-03'
        self.module = 'assistente_administrativo'
        self.lesson = 'aula1'
    def addCourse(self,course):
        self.courses.append(course)

    def getPath():
        return self.course+'/'+self.module+'/'+self.lesson+'/'

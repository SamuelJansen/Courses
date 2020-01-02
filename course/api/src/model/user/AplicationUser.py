class AplicationUser:
    def __init__(self,registration):
        self.registration = registration
        self.courses = []
    def addCourse(self,course):
        self.courses.append(course)

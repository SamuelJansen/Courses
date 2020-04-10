class Module:

    def __init__(self,name,lessons,course):

        self.course = course
        self.plataform = self.course.plataform

        self.name = name

        self.lessons = lessons

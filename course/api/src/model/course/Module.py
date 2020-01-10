class Module:
    MODULES_FILE = 'resourse\\modules\\modules.ht'
    def __init__(self,name,modulePath,lessons,courseName=None):
        self.name = name
        self.modulePath = modulePath
        self.lessons = lessons

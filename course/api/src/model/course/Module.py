class Module:

    MODULE_PATH = 'resourse\\modules\\'
    MODULES_FILE = 'modules.ht'

    def __init__(self,name,modulePath,lessons,
        courseName = None
    ):
        self.name = name
        self.modulePath = modulePath
        self.lessons = lessons

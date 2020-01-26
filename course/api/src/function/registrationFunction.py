from function import pathFunction
from model.course import Course, Module

def getCourses(coursesName,plataform) :
    courses = {}
    for courseName in coursesName :
        courseNameParsed = pathFunction.parseName(courseName)
        coursePath = plataform.pathMannanger.getApiModulePath('course')+'resourse/courses/'+courseNameParsed+'/'+courseNameParsed+'.ht'
        ###- print(f'coursePath = {coursePath}')
        try :
            with open(coursePath,"r",encoding="utf-8") as courseFile :
                print(f'courseFile = {courseFile}')
                modulesName = []
                for module in courseFile :
                    modulesName.append(module.strip())
                print(f'modulesName = {modulesName}')
                modules = getModules(modulesName)
                courses[courseNameParsed] = Course.Course(courseName,coursePath,modules)
        except :
            courses[courseNameParsed] = None
            print(f'getCourses(coursesName) error --> courses[{courseNameParsed}] = {courses[courseNameParsed]}')
            print(f'    coursePath = {coursePath}')
            print(f'    {courseName} course not found')

    return courses

def getModules(modulesName,plataform) :
    modules = {}
    for moduleName in modulesName :
        moduleNameParsed = pathFunction.parseName(moduleName)
        modulePath = plataform.pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+moduleNameParsed+'.ht'
        try :
            with open(modulePath,"r",encoding="utf-8") as moduleFile :
                lessonsName = []
                for page in moduleFile :
                    lessonsName.append(page.strip())
                print(f'lessonsName = {lessonsName}')
                modules[moduleNameParsed] = Module.Module(moduleName,modulePath,lessonsName)
        except :
            modules[moduleNameParsed] = None
            print(f'getModules(modulesName) error --> modules[{moduleNameParsed}] = {modules[moduleNameParsed]}')
            print(f'    {moduleName} module not found')

    return modules

    # 'macro-2020-03'
    # 'assistente_administrativo'
    # 'aula1'

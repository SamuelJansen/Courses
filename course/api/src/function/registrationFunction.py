from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from function import pathFunction
from model.course import Course,Module

def getCourses(coursesName) :
    courses = {}
    for courseName in coursesName :
        courseNameParsed = pathFunction.parseName(courseName)
        coursePath = pathMannanger.getApiModulePath('course')+'resourse/courses/'+courseNameParsed+'.ht'
        ###- print(f'coursePath = {coursePath}')
        try :
            with open(coursePath,"r",encoding="utf-8") as courseFile :
                modulesName = []
                for module in courseFile :
                    modulesName.append(module.strip())
                ###- print(f'modulesName = {modulesName}')
                courses[courseNameParsed] = Course.Course(courseName,coursePath,getModules(modulesName))
        except :
            courses[courseNameParsed] = None
            print(f'getCourses(coursesName) error --> courses[{courseNameParsed}] = {courses[courseNameParsed]}')
            print(f'    {courseName} course not found')

    return courses

def getModules(modulesName) :
    modules = {}
    for moduleName in modulesName :
        moduleNameParsed = pathFunction.parseName(moduleName)
        modulePath = pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+moduleNameParsed+'.ht'
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

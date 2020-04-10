import os

from tokenRepository import *

import imageFunction, setting

import ApplicationUser, Course, Module, Lesson, Page
import coursePathFunction

class CourseRepository:

    def __init__(self,application):
        self.application = application
        self.pathMannanger = self.application.pathMannanger
        applicationUserFilePath = f'''{self.pathMannanger.getApiPath('Courses')}resourse\\application_users\\application_users.{self.application.extension}'''
        with open(applicationUserFilePath,"r",encoding="utf-8") as applicationUserFile :
            applicationUsers = ''.join(applicationUserFile).strip().split(f'{db_REGISTRATION}{db_COLON}')
        self.applicationUsers = applicationUsers

    def getApplicationUser(self):
        applicationUserData = self.getApplicationUserData()
        applicationUserKeyValuePair = self.getApplicationUserKeyValuePair(applicationUserData)
        if applicationUserKeyValuePair[db_PASSWORD] == self.application.password :
            return self.buildApplicationUser(applicationUserKeyValuePair)

    def getApplicationUserData(self):
        for applicationUser in self.applicationUsers :
            if applicationUser.strip().split('\n')[0] == self.application.registration :
                return f'{db_REGISTRATION}{db_COLON}{applicationUser}'.split('\n')

    def getApplicationUserKeyValuePair(self,applicationUserData):
        applicationUserKeyValuePair = {}
        for keyValuePair in applicationUserData :
            keyValuePairSplited = keyValuePair.split(db_COLON)
            applicationUserKeyValuePair[keyValuePairSplited[0].strip()] = keyValuePairSplited[1].strip()
        return applicationUserKeyValuePair

    def buildApplicationUser(self,applicationUserKeyValuePair):
        applicationUser = ApplicationUser.ApplicationUser(
            applicationUserKeyValuePair[db_REGISTRATION],
            applicationUserKeyValuePair[db_PASSWORD],
            self.application
        )
        for courseName in applicationUserKeyValuePair[db_COURSES].split(db_COMA) :
            applicationUser.courses[courseName.strip()] = {}

            for moduleName in self.getModulesFromCourseFile(courseName) :
                moduleName = moduleName.strip()
                if f'__{moduleName}__' in applicationUserKeyValuePair.keys() :
                    applicationUser.courses[moduleName] = {}

                    for lessonName in self.getLessonsFromModuleDirectory(moduleName) :
                        if f'__{moduleName}__{lessonName}__' in applicationUserKeyValuePair.keys() :
                            applicationUser.courses[moduleName][lessonName] = {}

                            for pageData in self.getPagesFromLessonData(applicationUserKeyValuePair[f'{db_DOUBLE_UNDERSCORE}{moduleName}{db_DOUBLE_UNDERSCORE}{lessonName}{db_DOUBLE_UNDERSCORE}']) :
                                applicationUser.courses[moduleName][lessonName][pageData.split(db_PAGE_DATA_SEPARATOR)[0]] = pageData.split(db_PAGE_DATA_SEPARATOR)[1:]
        return applicationUser

    def getModulesFromCourseFile(self,courseName):
        with open(self.getCoursePath(courseName),"r",encoding="utf-8") as courseFile :
            moduleNames = []
            for module in courseFile :
                moduleNames.append(module.strip())
            return moduleNames

    def getCoursePath(self,courseName):
        courseNameParsed = coursePathFunction.parseName(courseName)
        return f'''{self.pathMannanger.getApiPath('Courses')}resourse\\courses\\{courseNameParsed}.{self.application.extension}'''

    def getLessonsFromModuleDirectory(self,moduleName):
        return os.listdir(self.getLessonsPath(moduleName))

    def getLessonsPath(self,moduleName):
        moduleNameParsed = coursePathFunction.parseName(moduleName)
        return f'''{self.pathMannanger.getApiPath('Courses')}resourse\\modules\\{moduleNameParsed}\\'''

    def getLessonPath(self,moduleName,lessonName):
        print(f'CourseRepository.getLessonName() = {self.application.repository.getLessonsPath(moduleName)}{lessonName}\\')
        return f'{self.application.repository.getLessonsPath(moduleName)}{lessonName}\\'

    def getPagesFromLessonData(self,lessonData):
        return lessonData.strip().split(db_COMA)

    def getAllImagePageNames(self,moduleName,lessonName):
        return imageFunction.getImageFileNames(f'{self.getLessonPath(moduleName,lessonName)}\\image','png')

    def getPageNamesFromLessonScriptPath(self,lessonScriptPath):
        return list(self.loadScript(lessonScriptPath).pages.keys()) ###- setting.sortItNumerically()

    def loadScript(self,lessonScriptPath):
        lessonScriptPath = self.completeLessonScriptPath(lessonScriptPath)

        courseName = 'STANDARD_COURSE' ###- TODO, implement get course name
        course = Course.Course(courseName,self.application)

        moduleName = self.getModuleNameFromLessonScriptPath(lessonScriptPath)
        lessons = {}
        module = Module.Module(moduleName,lessons,course)

        lessonName = self.getLessonNameFromLessonScriptPath(lessonScriptPath)
        pages = {}
        module.lessons[lessonName] = Lesson.Lesson(lessonName,pages,module)

        try :
            with open(lessonScriptPath,"r",encoding="utf-8") as scriptFile :
                for lessonScriptLine in scriptFile :
                    if lessonScriptLine != '\n' :
                        pageName = self.getPageNameFromLessonScriptLine(lessonScriptLine)
                        pageScript = lessonScriptLine.strip()
                        module.lessons[lessonName].pages[pageName] = Page.Page(pageName,pageScript,module.lessons[lessonName])
        except :
            with open(lessonScriptPath,"+w",encoding="utf-8") as scriptFile : pass

        return module.lessons[lessonName]

    def completeLessonScriptPath(self,lessonScriptPath):
        ###- C:\Users\Samuel Jansen\Courses\api\src\resourse\Robótica 1\Aula 03\Robótica 1.Aula 03.glb
        lessonScriptPath = lessonScriptPath.strip()
        try :
            if (
                lessonScriptPath.split('\\')[-1].split('.')[-2] == lessonScriptPath.split('\\')[-2] and
                lessonScriptPath.split('\\')[-1].split('.')[-3] == lessonScriptPath.split('\\')[-3]
            ) :
                return lessonScriptPath
        except :
            if lessonScriptPath.split('\\')[-1] == f'''{lessonScriptPath.split(self.pathMannanger.backSlash)[-3]}.{lessonScriptPath.split(self.pathMannanger.backSlash)[-2]}.{self.application.extension}''' :
                return lessonScriptPath
        return f'''{lessonScriptPath}{lessonScriptPath.split(self.pathMannanger.backSlash)[-3]}.{lessonScriptPath.split(self.pathMannanger.backSlash)[-2]}.{self.application.extension}'''

    def getModuleNameFromLessonScriptPath(self,lessonScriptPath):
        return lessonScriptPath.strip().split('\\')[-3]

    def getLessonNameFromLessonScriptPath(self,lessonScriptPath):
        return lessonScriptPath.strip().split('\\')[-2]

    def getPageNameFromLessonScriptLine(self,lessonScriptLine):
        pageScriptElements = lessonScriptLine.strip().split(db_COMA)
        for pageScriptElement in pageScriptElements :
            key = pageScriptElement.split(db_COLON)[0]
            if key == db_PAGE :
                return pageScriptElement.split(db_COLON)[1]

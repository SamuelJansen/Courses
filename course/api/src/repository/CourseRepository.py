import os

from tokenRepository import *

import imageFunction, setting

import ApplicationUser, Course, Lesson, Page
import coursePathFunction

class CourseRepository:

    def __init__(self,application):
        self.application = application
        self.pathMannanger = self.application.pathMannanger
        applicationUserFilePath = f'''{self.pathMannanger.getApiModulePath('course')}resourse\\application_users\\application_users.{self.application.extension}'''
        with open(applicationUserFilePath,"r",encoding="utf-8") as applicationUserFile :
            applicationUsers = ''.join(applicationUserFile).strip().split(f'{REGISTRATION}{COLON}')
        self.applicationUsers = applicationUsers

    def getApplicationUser(self):
        applicationUserData = self.getApplicationUserData()
        applicationUserKeyValuePair = self.getApplicationUserKeyValuePair(applicationUserData)
        if applicationUserKeyValuePair[PASSWORD] == self.application.password :
            return self.buildApplicationUser(applicationUserKeyValuePair)

    def getApplicationUserData(self):
        for applicationUser in self.applicationUsers :
            if applicationUser.strip().split('\n')[0] == self.application.registration :
                return f'{REGISTRATION}{COLON}{applicationUser}'.split('\n')

    def getApplicationUserKeyValuePair(self,applicationUserData):
        applicationUserKeyValuePair = {}
        for keyValuePair in applicationUserData :
            keyValuePairSplited = keyValuePair.split(COLON)
            applicationUserKeyValuePair[keyValuePairSplited[0].strip()] = keyValuePairSplited[1].strip()
        return applicationUserKeyValuePair

    def buildApplicationUser(self,applicationUserKeyValuePair):
        applicationUser = ApplicationUser.ApplicationUser(
            applicationUserKeyValuePair[REGISTRATION],
            applicationUserKeyValuePair[PASSWORD],
            self.application
        )
        for courseName in applicationUserKeyValuePair[COURSES].split(COMA) :
            applicationUser.courses[courseName.strip()] = {}

            for moduleName in self.getModulesFromCourseFile(courseName) :
                moduleName = moduleName.strip()
                if f'__{moduleName}__' in applicationUserKeyValuePair.keys() :
                    applicationUser.courses[moduleName] = {}

                    for lessonName in self.getLessonsFromModuleDirectory(moduleName) :
                        if f'__{moduleName}__{lessonName}__' in applicationUserKeyValuePair.keys() :
                            applicationUser.courses[moduleName][lessonName] = {}

                            for pageData in self.getPagesFromLessonData(applicationUserKeyValuePair[f'__{moduleName}__{lessonName}__']) :
                                applicationUser.courses[moduleName][lessonName][pageData.split(PAGE_DATA_SEPARATOR)[0]] = pageData.split(PAGE_DATA_SEPARATOR)[1:]
        return applicationUser

    def getModulesFromCourseFile(self,courseName):
        with open(self.getCoursePath(courseName),"r",encoding="utf-8") as courseFile :
            moduleNames = []
            for module in courseFile :
                moduleNames.append(module.strip())
            return moduleNames

    def getCoursePath(self,courseName):
        courseNameParsed = coursePathFunction.parseName(courseName)
        return f'''{self.pathMannanger.getApiModulePath('course')}resourse\\courses\\{courseNameParsed}.{self.application.extension}'''

    def getLessonsFromModuleDirectory(self,moduleName):
        return os.listdir(self.getLessonsPath(moduleName))

    def getLessonsPath(self,moduleName):
        moduleNameParsed = coursePathFunction.parseName(moduleName)
        return f'''{self.pathMannanger.getApiModulePath('course')}resourse\\modules\\{moduleNameParsed}\\'''

    def getLessonPath(self,moduleName,lessonName):
        print(f'CourseRepository.getLessonName() = {self.application.repository.getLessonsPath(moduleName)}{lessonName}\\')
        return f'{self.application.repository.getLessonsPath(moduleName)}{lessonName}\\'

    def getPagesFromLessonData(self,lessonData):
        return lessonData.strip().split(COMA)

    def getAllImagePageNames(self,moduleName,lessonName):
        return imageFunction.getImageFileNames(f'{self.getLessonPath(moduleName,lessonName)}\\image','png')

    def getPageNamesFromLessonScriptPath(self,lessonScriptPath):
        return list(self.loadScript(lessonScriptPath).pages.keys()) ###- setting.sortItNumerically()

    def loadScript(self,lessonScriptPath):
        lessonScriptPath = self.completeLessonScriptPath(lessonScriptPath)
        courseName = self.getCourseNameFromLessonScriptPath(lessonScriptPath)
        course = Course.Course(courseName,self.application)

        lessonName = self.getLessonNameFromLessonScriptPath(lessonScriptPath)
        lesson = Lesson.Lesson(lessonName,course,self.application)

        with open(lessonScriptPath,"r",encoding="utf-8") as scriptFile :
            for lessonScriptLine in scriptFile :
                if lessonScriptLine != '\n' :
                    pageName = self.getPageNameFromLessonScriptLine(lessonScriptLine)
                    pageScript = lessonScriptLine.strip()
                    lesson.pages[pageName] = Page.Page(pageName,lesson,pageScript,self.application)

        return lesson

    def completeLessonScriptPath(self,lessonScriptPath):
        ###- C:\Users\Samuel Jansen\Courses\course\api\src\resourse\Robótica 1\Aula 03\Robótica 1.Aula 03.ht
        lessonScriptPath = lessonScriptPath.strip()
        try :
            if (
                lessonScriptPath.split('\\')[-1].split('.')[-2] == lessonScriptPath.split('\\')[-2] and
                lessonScriptPath.split('\\')[-1].split('.')[-3] == lessonScriptPath.split('\\')[-3]
            ) :
                return lessonScriptPath
        except :
            if lessonScriptPath.split('\\')[-1] == f'''{lessonScriptPath.split(self.pathMannanger.BACK_SLASH)[-3]}.{lessonScriptPath.split(self.pathMannanger.BACK_SLASH)[-2]}.{self.application.extension}''' :
                return lessonScriptPath
        return f'''{lessonScriptPath}{lessonScriptPath.split(self.pathMannanger.BACK_SLASH)[-3]}.{lessonScriptPath.split(self.pathMannanger.BACK_SLASH)[-2]}.{self.application.extension}'''

    def getCourseNameFromLessonScriptPath(self,lessonScriptPath):
        return lessonScriptPath.strip().split('\\')[-2]

    def getLessonNameFromLessonScriptPath(self,lessonScriptPath):
        return lessonScriptPath.strip().split('\\')[-1]

    def getPageNameFromLessonScriptLine(self,lessonScriptLine):
        pageScriptElements = lessonScriptLine.strip().split(COMA)
        for pageScriptElement in pageScriptElements :
            key = pageScriptElement.split(COLON)[0]
            if key == PAGE :
                return pageScriptElement.split(COLON)[1]

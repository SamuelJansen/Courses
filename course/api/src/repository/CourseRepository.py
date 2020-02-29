import os

from tokenRepoitory import *

import imageFunction

import ApplicationUser
import coursePathFunction

class CourseRepository:

    def __init__(self,application):
        self.application = application
        applicationUserFilePath = f'''{self.application.pathMannanger.getApiModulePath('course')}resourse\\application_users\\application_users.{self.application.extension}'''
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
        return f'''{self.application.pathMannanger.getApiModulePath('course')}resourse\\courses\\{courseNameParsed}.{self.application.extension}'''

    def getLessonsFromModuleDirectory(self,moduleName):
        return os.listdir(self.getLessonsPath(moduleName))

    def getLessonsPath(self,moduleName):
        moduleNameParsed = coursePathFunction.parseName(moduleName)
        return f'''{self.application.pathMannanger.getApiModulePath('course')}resourse\\modules\\{moduleNameParsed}\\'''

    def getLessonPath(self,moduleName,lessonName):
        print(f'CourseRepository.getLessonName() = {self.application.repository.getLessonsPath(moduleName)}{lessonName}\\')
        return f'{self.application.repository.getLessonsPath(moduleName)}{lessonName}\\'

    def getPagesFromLessonData(self,lessonData):
        return lessonData.strip().split(COMA)

    def getAllPageNames(self,moduleName,lessonName):
        return imageFunction.getImageFileNames(f'{self.getLessonPath(moduleName,lessonName)}\\image','png')

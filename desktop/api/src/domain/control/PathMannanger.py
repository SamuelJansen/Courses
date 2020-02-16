from domain.control import PathMannanger

print('PathMannanger library imported')

class PathMannanger:
    BASE_API_PATH = 'api\\src\\'
    API_NAME = 'Courses'
    GLOBALS = 'globals'
    COURSE = 'course'
    APPLICATION = 'application'
    DESKTOP = 'desktop'
    EDITOR = 'editor'
    API_MODULES = [
        GLOBALS,
        COURSE,
        APPLICATION,
        DESKTOP,
        EDITOR
    ]

    def __init__(self):

        from pathlib import Path

        self.currentPath = str(Path(__file__).parent.absolute())
        self.localPath = f'{str(Path.home())}\\'

        self.apiName = PathMannanger.API_NAME
        self.baseApiPath = PathMannanger.BASE_API_PATH
        self.apiPath = f'{self.currentPath.split(self.apiName)[0]}{self.apiName}\\'
        self.apiModules = PathMannanger.API_MODULES

        self.importMannangerRootInsideBaseApiPath = 'domain\\control\\PathMannanger.py'
        self.globalsModule = PathMannanger.GLOBALS
        self.globalsModulePath = f'{self.getApiModulePath(self.globalsModule)}{self.importMannangerRootInsideBaseApiPath}'

        self.update()
        self.newApplicationHandler()

    def getApiModulePath(self,apiModuleName):
        return f'{self.apiPath}{apiModuleName}\\{self.baseApiPath}'

    def update(self) :

        globalsScript = []
        with open(self.globalsModulePath,"r",encoding="utf-8") as globalsFile :
            for line in globalsFile :
                globalsScript.append(line)

        for apiModule in self.apiModules :
            updatingModulePath =f'{self.getApiModulePath(apiModule)}{self.importMannangerRootInsideBaseApiPath}'
            if apiModule != self.globalsModule :
                with open(updatingModulePath,"w+",encoding="utf-8") as moduleFile :
                    moduleFile.write(''.join(globalsScript))

        # https://stackabuse.com/how-to-copy-a-file-in-python/
        # import shutil
        # shutil.copy2('file1.txt', 'file2.txt')
        self.makeAplicationLibrariesAvaliable()

    def makeAplicationLibrariesAvaliable(self) :

        import sys
        # https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
        from pathlib import Path

        for apiModule in self.apiModules :
            if apiModule != self.globalsModule :
                apiModulePath = f'{self.apiPath}{apiModule}\\{self.baseApiPath}'
                print(f'new path: {apiModulePath}')
                sys.path.append(apiModulePath)

        from function import applicationPathFunction
        applicationPathList = applicationPathFunction.getPathList()
        apiModulePath = self.getApiModulePath(PathMannanger.APPLICATION)
        for path in applicationPathList :
            print(f'new path: {apiModulePath}{path}')
            sys.path.append(f'{apiModulePath}{path}')

    def newApplicationHandler(self):
        import ApplicationHandler
        self.applicationHandler = ApplicationHandler.ApplicationHandler(self)

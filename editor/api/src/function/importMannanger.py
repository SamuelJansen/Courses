print('PathMannanger library imported')

class PathMannanger:
    BASE_API_PATH = 'api\\src\\'
    API_NAME = 'Courses'
    GLOBALS_MODULE = 'globals'
    API_MODULES = [
        GLOBALS_MODULE,
        'course',
        'application',
        'desktop',
        'editor'
    ]

    def __init__(self):

        from pathlib import Path

        self.currentPath = str(Path(__file__).parent.absolute())
        self.localPath = f'{str(Path.home())}\\'

        self.apiName = PathMannanger.API_NAME
        self.baseApiPath = PathMannanger.BASE_API_PATH
        self.apiPath = f'{self.currentPath.split(self.apiName)[0]}{self.apiName}\\'
        self.apiModules = PathMannanger.API_MODULES

        self.importMannangerRootInsideBaseApiPath = 'function\\importMannanger.py'
        self.globalsModule = PathMannanger.GLOBALS_MODULE
        self.globalsModulePath = f'{self.getApiModulePath(self.globalsModule)}{self.importMannangerRootInsideBaseApiPath}'

    def getApiModulePath(self,apiModuleName):
        return f'{self.apiPath}{apiModuleName}\\{self.baseApiPath}'



def updateImportMannger() :

    pathMannanger = PathMannanger()
    globalsScript = []
    with open(pathMannanger.globalsModulePath,"r",encoding="utf-8") as globalsFile :
        for line in globalsFile :
            globalsScript.append(line)

    for apiModule in pathMannanger.apiModules :
        updatingModulePath =f'{pathMannanger.getApiModulePath(apiModule)}{pathMannanger.importMannangerRootInsideBaseApiPath}'
        if apiModule != pathMannanger.globalsModule :
            with open(updatingModulePath,"w+",encoding="utf-8") as moduleFile :
                moduleFile.write(''.join(globalsScript))

    # https://stackabuse.com/how-to-copy-a-file-in-python/
    # import shutil
    # shutil.copy2('file1.txt', 'file2.txt')

    return makeAplicationLibrariesAvaliable()

def makeAplicationLibrariesAvaliable() :

    import sys
    # https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
    from pathlib import Path

    newPathMannanger = PathMannanger()

    for apiModule in newPathMannanger.apiModules :
        if apiModule != newPathMannanger.globalsModule :
            apiModulePath = f'{newPathMannanger.apiPath}{apiModule}\\{newPathMannanger.baseApiPath}'
            print(f'new path: {apiModulePath}')
            sys.path.append(apiModulePath)

    from function import applicationPathFunction
    applicationPathList = applicationPathFunction.getPathList()
    apiModulePath = newPathMannanger.getApiModulePath('application')
    for path in applicationPathList :
        print(f'new path: {apiModulePath}{path}')
        sys.path.append(f'{apiModulePath}{path}')

    return newPathMannanger

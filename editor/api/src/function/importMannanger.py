class PathMannanger:
    API_NAME = 'Courses'
    GLOBALS_MODULE = 'globals'
    API_MODULES = [
        GLOBALS_MODULE,
        'course',
        'aplication',
        'desktop',
        'editor'
    ]

    def __init__(self,baseApiPath):

        from pathlib import Path

        self.currentPath = str(Path(__file__).parent.absolute())
        self.localPath = str(Path.home()) + '\\'

        self.apiName = PathMannanger.API_NAME
        self.apiPath = self.currentPath.split(self.apiName)[0] + self.apiName + '\\'
        self.baseApiPath = baseApiPath
        self.apiModules = PathMannanger.API_MODULES

        self.importMannangerRootInsideBaseApiPath = 'function\\importMannanger.py'
        self.globalsModule = PathMannanger.GLOBALS_MODULE
        self.globalsModulePath = self.getApiModulePath(self.globalsModule) + self.importMannangerRootInsideBaseApiPath

    def getApiModulePath(self,apiModuleName):
        return self.apiPath + apiModuleName + '\\' + self.baseApiPath

def makeAplicationLibrariesAvaliable() :
    import sys
    # https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
    from pathlib import Path

    baseApiPath = 'api\\src\\'
    pathMannanger = PathMannanger(baseApiPath)

    for apiModule in pathMannanger.apiModules :
        if apiModule != pathMannanger.globalsModule :
            sys.path.append(pathMannanger.apiPath + apiModule + '\\' + pathMannanger.baseApiPath)

            modulePath = pathMannanger.apiPath + apiModule + '\\' + pathMannanger.baseApiPath + pathMannanger.importMannangerRootInsideBaseApiPath

            globalsScript = []
            with open(pathMannanger.globalsModulePath,"r",encoding="utf-8") as globalsFile :
                for line in globalsFile :
                    globalsScript.append(line)
                with open(modulePath,"w+",encoding="utf-8") as moduleFile :
                    moduleFile.write(''.join(globalsScript))

    # https://stackabuse.com/how-to-copy-a-file-in-python/
    # import shutil
    # shutil.copy2('file1.txt', 'file2.txt')

    return pathMannanger

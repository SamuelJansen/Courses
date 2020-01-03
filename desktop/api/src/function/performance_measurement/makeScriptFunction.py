from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from function import pathFunction

class Button:
    def __init__(self,previousPagePoints,nextPagePoints):
        self.previousPagePoints = previousPagePoints
        self.nextPagePoints = nextPagePoints

def makeAScript(courseName,moduleName,lessonName,amountOfPagesToMake,plataform) :
    ###- Course will need some work later on
    courseNameParsed = pathFunction.parseName(courseName)

    moduleNameParsed = pathFunction.parseName(moduleName)
    lessonNameParsed = pathFunction.parseName(lessonName)
    pagesPath = pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+lessonNameParsed+'/'

    previousPagePoints = '0x495x83x560'
    nextPagePoints = '901x497x996x562'
    framesPerPage = '0..29'
    button = Button(previousPagePoints,nextPagePoints)
    scriptList = []
    for pageIndex in range(amountOfPagesToMake) :
        scriptList.append(f'page={pageIndex} frames={framesPerPage} button.previousPage={button.previousPagePoints} button.nextPage={button.nextPagePoints}')

    with open(pagesPath+'script.ht',"w+",encoding="utf-8") as script :
        script.write('\n'.join(scriptList))

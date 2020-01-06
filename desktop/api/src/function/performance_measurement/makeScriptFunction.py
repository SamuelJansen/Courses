from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from function import pathFunction

def goNextPage(input) :
    print(f'    function called: goNextPage({input})')
    pass

def goPreviousPage(input) :
    print(f'    function called: goPreviousPage({input})')
    pass

class Button:
    functionDictionary = {
        'PREVIOUS_PAGE' : goNextPage,
        'NEXT_PAGE' : goPreviousPage
    }
    def __init__(self,position,functionIndex):
        self.position = position
        self.function = Button.functionDictionary[functionIndex]


def makeAScript(courseName,moduleName,lessonName,amountOfPagesToMake,plataform) :
    ###- Course will need some work later on
    courseNameParsed = pathFunction.parseName(courseName)

    moduleNameParsed = pathFunction.parseName(moduleName)
    lessonNameParsed = pathFunction.parseName(lessonName)
    pagesPath = pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+lessonNameParsed+'/'

    previousPagePosition = '0x495x83x560'
    nextPagePosition = '901x497x996x562'
    framesPerPage = '0..29'
    previousPageButtom = Button(previousPagePosition,'PREVIOUS_PAGE')
    nextPageButton = Button(nextPagePosition,'NEXT_PAGE')
    scriptList = []
    for pageIndex in range(amountOfPagesToMake) :
        scriptList.append(f'page={pageIndex} frames={framesPerPage} button={previousPageButtom.position} button={nextPageButton.position}')

    scriptPath = pagesPath+'script.ht'
    with open(scriptPath,"w+",encoding="utf-8") as scriptFile :
        scriptFile.write('\n'.join(scriptList))

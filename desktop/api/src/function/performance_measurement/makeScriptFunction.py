import Button

import coursePathFunction

def makeAScript(courseName,moduleName,lessonName,amountOfPagesToMake,plataform) :
    ###- Course will need some work later on
    courseNameParsed = coursePathFunction.parseName(courseName)

    moduleNameParsed = coursePathFunction.parseName(moduleName)
    lessonNameParsed = coursePathFunction.parseName(lessonName)
    pagesPath = plataform.pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+lessonNameParsed+'/'

    previousPagePosition = '0x495x83x560'
    nextPagePosition = '901x497x996x562'
    framesPerPage = '0..29'
    # previousPageButtom = Button.Button(previousPagePosition,'PREVIOUS_PAGE')
    # nextPageButton = Button.Button(nextPagePosition,'NEXT_PAGE')
    scriptList = []
    for pageIndex in range(amountOfPagesToMake) :
        #scriptList.append(f'page={pageIndex} frames={framesPerPage} button={previousPageButtom.position} button={nextPageButton.position}')
        scriptList.append(f'page={pageIndex} frames={framesPerPage} button={previousPagePosition} button={nextPagePosition}')

    scriptPath = pagesPath+'script.ht'
    with open(scriptPath,"w+",encoding="utf-8") as scriptFile :
        scriptFile.write('\n'.join(scriptList))

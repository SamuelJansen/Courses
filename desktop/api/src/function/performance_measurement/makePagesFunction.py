import pygame as pg

import imageFunction

import coursePathFunction

def makeSoManyPages(courseName,moduleName,lessonName,amountOfPagesToMake,plataform) :
    ###- Course will need some work later on
    courseNameParsed = coursePathFunction.parseName(courseName)

    moduleNameParsed = coursePathFunction.parseName(moduleName)
    lessonNameParsed = coursePathFunction.parseName(lessonName)
    pagesPath = plataform.pathMannanger.getApiModulePath('course')+'resourse/modules/'+moduleNameParsed+'/'+lessonNameParsed+'/image/'
    basePageImage = imageFunction.getImage(pagesPath+'performance_measurement.png',plataform.size,plataform)

    for page in range(amountOfPagesToMake) :
        newPageName = str(page)
        for frame in range(plataform.fps) :
            newImage = basePageImage.copy()

            pg.font.init()
            myfont = pg.font.SysFont('Comic Sans MS', 24)

            courseNameSurface = myfont.render('Assistente Administrativo', False, (0, 0, 0))
            newImage.blit(courseNameSurface,(24,24))

            myfont = pg.font.SysFont('Comic Sans MS', 14)
            frameSurface = myfont.render('    frame '+str(frame), False, (0, 0, 0))
            newImage.blit(frameSurface,(24,72))

            newPagePath = pagesPath+newPageName+' '+str(frame)+'.png'
            imageFunction.saveImage(newImage,newPagePath)

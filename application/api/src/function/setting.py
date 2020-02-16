import pygame as pg

def getSettings(path) :
    settings = {}
    with open(path,'r',encoding='utf-8') as settingsFile :
        allSettings = settingsFile.readlines()
    for line,setting in enumerate(allSettings) :
        ###- print(f'setting = {setting}, line = {line}')
        if setting.startswith('screenSize') :
            screenSize = setting.split()[1].rstrip().split('x')
            screenSize = [int(screenSize[0]),int(screenSize[1])]
            settings['screenSize'] = screenSize
        #elif setting.startswith('*') :
        #    settings.append(Setting(setting.rstrip()[2:].split()))
    return settings

def getAplicationSize(aplication) :
    if aplication.settings['screenSize']==[0,0] :
        temporaryScreen = pg.display.set_mode([0,0],pg.FULLSCREEN)
        screenSizeX, screenSizeY = temporaryScreen.get_size()
        size = [screenSizeX, screenSizeY]
    else :
        size = aplication.settings['screenSize']
    return size

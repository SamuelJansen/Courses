import pygame as pg
import os

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

def getFileNames(path,fileExtension) :
    fileNames = []
    names = os.listdir(path)
    for name in names :
        if fileExtension == name.split('.')[-1] :
            fileNames.append(name[:-(len(fileExtension) + 1)])
    return sortItNumerically(fileNames)

def sortItNumerically(fileNames) :
    sortedFileNamesWhichAreNumbers = sorted(numberfyIt(fileNames))
    return stringfyIt(sortedFileNamesWhichAreNumbers,fileNames)

def numberfyIt(numersAsStrings) :
    numbers = []
    for index in range(len(numersAsStrings)) :
        ###- '4'
        ###- '4_1'
        ###- '4_2'
        try :
            numberAsString = numersAsStrings[index]
            splitedNumberAsString = numberAsString.split('-')
            if len(splitedNumberAsString) == 1 :
                number = int(splitedNumberAsString[0])
                numbers.append(number)
        except : pass
    return numbers

def stringfyIt(sortedNumbers,numbersAsStrings) :
    sortedNumbersAsStrings = []
    for index in range(len(sortedNumbers)) :
        ###- 4
        ###- 4.1
        ###- 4.2
        sortedNumberAsString = str(sortedNumbers[index]).replace('.','_')
        sortedNumbersAsStrings.append(sortedNumberAsString)
    for numberAsString in numbersAsStrings :
        if numberAsString not in sortedNumbersAsStrings :
            sortedNumbersAsStrings.append(numberAsString)
    return sortedNumbersAsStrings

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
        splitedName = name.split('.')
        if fileExtension == splitedName[-1] :
            fileNames.append(''.join(splitedName[:-1]))
    return sortItNumerically(fileNames)

def sortItNumerically(fileNames) :
    sortedFileNamesWhichAreNumbers = sorted(numberfyIt(fileNames))
    return stringfyIt(sortedFileNamesWhichAreNumbers,fileNames)

def numberfyIt(numbersAsStrings) :
    numbers = []
    for string in numbersAsStrings :
        numberAsString = string
        ###- '4'
        ###- '4_1'
        ###- '4_2'
        floatNumber = None
        if 'i' not in numberAsString :
            floatNumber = getFloatNumberSplitingNumberAsTringBySeparatorList(numberAsString,['_','-','.'])
            if str(floatNumber) :
                numbers.append(floatNumber)
    return numbers

def getFloatNumberSplitingNumberAsTringBySeparatorList(numberAsString,separatorList) :
    if separatorList :
        splitedNumberAsString = numberAsString.split(separatorList[0])
        if len(splitedNumberAsString) == 1 :
            try :
                return float(f'{splitedNumberAsString[0]}.0')
            except : pass
        elif len(splitedNumberAsString) == 2 :
            try :
                return float(f'{splitedNumberAsString[0]}.{splitedNumberAsString[1]}')
            except : pass
        return getFloatNumberSplitingNumberAsTringBySeparatorList(splitedNumberAsString[0],separatorList[1:])
    else :
        return numberAsString

def stringfyIt(sortedNumbers,numbersAsStrings) :
    sortedNumbersAsStrings = []
    for floatNumber in sortedNumbers :
        ###- 4
        ###- 4.1
        ###- 4.2
        sortedNumberAsString = str(floatNumber)
        if int(sortedNumberAsString.split('.')[1]) != 0 :
            sortedNumberAsString.replace('.','_')
        else :
            sortedNumberAsString = sortedNumberAsString.split('.')[0]
        sortedNumbersAsStrings.append(sortedNumberAsString)
    for numberAsString in numbersAsStrings :
        if numberAsString not in sortedNumbersAsStrings :
            sortedNumbersAsStrings.append(numberAsString)
    return sortedNumbersAsStrings

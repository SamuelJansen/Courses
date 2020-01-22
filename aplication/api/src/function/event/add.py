from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model.course import Module

def addFunction(object) :
    modulesPath = pathMannanger.getApiModulePath('course') + Module.Module.MODULES_FILE
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for line in modulesFile :
            modules.append(line.strip())
    print(modules)
    print(f'    EventFunction called: add({object.aplication.name})')

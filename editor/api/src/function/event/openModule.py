from model.course import Module

def openModule(event) :
    modulesPath = f'{event.object.aplication.pathMannanger.getApiModulePath("course")}{Module.Module.MODULES_FILE}'
    modules = []
    with open(modulesPath,"r",encoding="utf-8") as modulesFile :
        for line in modulesFile :
            modules.append(line.strip())
    print(modules)






    print(f'    EventFunction called: open({event.object.aplication.name})')
    pass

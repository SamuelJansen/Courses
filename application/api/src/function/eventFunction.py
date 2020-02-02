from function.event.exit import *
from function.event.openModule import *
from function.event.save import *
from function.event.close import *
from function.event.add import *
from function.event.launch import *
from function.event.update import *
from function.event.unlaunch import *
from function.event.nextPage import *
from function.event.previousPage import *
from function.event.resolveSelection import *

eventFunctions = {}
EventFunction = (lambda eventFunctions=eventFunctions : lambda EventFunction:eventFunctions.setdefault(EventFunction.__name__,EventFunction))()

def getFunctionKey(functionKey) :
    return functionKey + 'Function'

@EventFunction
def exitFunction(event) :
    return exit(event)

@EventFunction
def openModuleFunction(event) :
    return openModule(event)

@EventFunction
def saveFunction(event) :
    return save(event)

@EventFunction
def closeFunction(event) :
    return close(event)

@EventFunction
def addFunction(event) :
    return add(event)

@EventFunction
def launchFunction(event) :
    return launch(event)

@EventFunction
def updateFunction(event) :
    return update(event)

@EventFunction
def unlaunchFunction(event) :
    return unlaunch(event)

@EventFunction
def nextPageFunction(event) :
    return nextPage(event)

@EventFunction
def previousPageFunction(event) :
    return previousPage(event)

@EventFunction
def resolveSelectionFunction(event) :
    return resolveSelection(event)

from function.event.exit import *
from function.event.open import *
from function.event.save import *
from function.event.close import *
from function.event.add import *
from function.event.launch import *
from function.event.update import *
from function.event.unlaunch import *
from function.event.nextPage import *
from function.event.previousPage import *

eventFunctions = {}
EventFunction = (lambda eventFunctions=eventFunctions : lambda EventFunction:eventFunctions.setdefault(EventFunction.__name__,EventFunction))()

@EventFunction
def exit(event) :
    return exitFunction(event)

@EventFunction
def open(event) :
    return openFunction(event)

@EventFunction
def save(event) :
    return saveFunction(event)

@EventFunction
def close(event) :
    return closeFunction(event)

@EventFunction
def add(event) :
    return addFunction(event)

@EventFunction
def launch(event) :
    return launchFunction(event)

@EventFunction
def update(event) :
    return updateFunction(event)

@EventFunction
def unlaunch(event) :
    return unlaunchFunction(event)

@EventFunction
def nextPage(event) :
    return nextPageFunction(event)

@EventFunction
def previousPage(event) :
    return previousPageFunction(event)

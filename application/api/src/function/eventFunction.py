from function.event.exit import exit
from function.event.openModule import openModule
from function.event.save import save
from function.event.close import close
from function.event.add import add
from function.event.launch import launch
from function.event.update import update
from function.event.unlaunch import unlaunch
from function.event.nextPage import nextPage
from function.event.previousPage import previousPage
from function.event.resolveModuleClick import resolveModuleClick
from function.event.resolveLessonClick import resolveLessonClick

class EventStatus:

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'

    def resolve(event):
        # print(f'ClickEvent.resolve(): event.name = {event.name}')
        if event.name in event.object.tutor.handler.events :
            event.status = EventStatus.RESOLVED
            # event.mouse.removeFocus()
            event.object.tutor.handler.deleteEvent(event.name)
        else :
            debugText = f'Event: {event.name}.resolve()\n'
            debugText += f'{event.name} not found in event.object.tutor.handler.events'
            self.application.holdForDebug(debugText)
        print(f'    END OF RESOLVE EVENT')

    def forceResolve(event):
        # print(f'ClickEvent.forceResolve(): event.name = {event.name}')
        event.status = EventStatus.RESOLVED
        event.object.tutor.handler.deleteEvent(event.name)
        # print(f'    END OF FORCE RESOLVE EVENT')

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
def resolveModuleClickFunction(event) :
    return resolveModuleClick(event)

@EventFunction
def resolveLessonClickFunction(event) :
    return resolveLessonClick(event)

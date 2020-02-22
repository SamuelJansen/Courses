import eventFunction

print('Event library imported')

class Event:

    def update(self):
        # print(f'Event() - {self.type}.update() - {getObjectFocusDebugText(self)}')
        self.object.handleEvent(self)

    def __init__(self,object,
        name = None,
        type = eventFunction.Type.EVENT,
        inherited = False
    ):

        if object :
            self.object = object
            self.application = self.object.application
            self.inherited = inherited

            if type :
                self.type = type
            else :
                self.type = eventFunction.Type.EVENT

            if name :
                self.name = name
            else :
                self.name = f'{self.type}.{object.name}'
            self.targetClass = object.__class__.__name__

            self.status = eventFunction.Status.NOT_RESOLVED

            if self.name not in self.object.handler.events :
                # print(f"Event(): {self.name} added in Event.__init__()")
                self.object.handler.addEvent(self)
            else :
                # print(f'{self.type} felt in Event.update()')
                self.object.handler.events[self.name].update()

            self.execute()

        else :
            applicationFunction.holdForDebug(getObjectHitDebugText(object))

    def resolve(self):
        self.object.handler.removeEvent(self)
        # print(f'{self.type}.update() resolved -{getObjectFocusDebugText(self)}')

    def execute(self):
        if not self.inherited :
            # print(f'{self.type}.execute()')
            self.update()
            if self.status == eventFunction.Status.RESOLVED :
                self.resolve()


def getObjectFocusDebugText(self):
    debugText = f' {self.name}, application.focus = {id(self.application.focus)}-{self.application.focus}'
    try :
        debugText += f', name = {self.application.focus.name}'
    except : pass
    return debugText

def getObjectHitDebugText(object) :
    debugText = ' -- Event:\n'
    debugText += '''Event(object): object = None\n'''
    debugText += f'mouse.objectHit = {object.application.mouse.objectHit}\n'
    try :
        debugText += f'mouse.objectHit.name = {object.application.mouse.objectHit.name}\n'
    except : pass
    debugText += f'mouse.objectHitDown = {object.application.mouse.objectHitDown}\n'
    try :
        debugText += f'mouse.objectHitDown.name = {object.application.mouse.objectHitDown.name}\n'
    except : pass
    debugText += f'mouse.objectHitUp = {object.application.mouse.objectHitUp}\n'
    try :
        debugText += f'mouse.objectHitUp.name = {object.application.mouse.objectHitUp.name}\n'
    except : pass
    debugText += f'     Application.focus = {object.application.mouse.application.focus}\n'
    try :
        debugText += f'     Application.focus.name = {mouse.application.focus.name}\n'
    except : pass

    return debugText

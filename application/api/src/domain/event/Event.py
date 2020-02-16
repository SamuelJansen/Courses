import Button, Surface
import eventFunction

print('Event library imported')

class Event:

    def __init__(self,object,
        name = None,
        autoUpdate = True
    ):

        if object :
            self.object = object
            self.application = self.object.application

            if name :
                self.name = name
            else :
                self.name = object.name
            self.targetClass = object.__class__.__name__

            self.status = eventFunction.Status.NOT_RESOLVED
            self.autoUpdate = autoUpdate

            if self.object.name not in self.object.tutor.handler.events :
                self.object.tutor.handler.addEvent(self)

            if self.autoUpdate :
                self.update()
                if self.status == eventFunction.Status.RESOLVED :
                    self.resolve()

    def update(self):
        print(f'------- START OF RESOLVE EVENT -------{getObjectFocusDebugText(self)}')
        self.object.handleEvent(self)

    def resolve(self):
        # if self.name in self.object.tutor.handler.events :
        #     self.status = eventFunction.Status.RESOLVED
        # else :
        #     debugText = f'Event: {self.name}.resolve()\n'
        #     debugText += f'{self.name} not found in event.object.tutor.handler.events'
        #     self.application.holdForDebug(debugText)
        print(f'-------- END OF RESOLVE EVENT --------{getObjectFocusDebugText(self)}')


def getObjectFocusDebugText(self):
    debugText = f' {self.name}, application.focus = {self.object.application.focus}'
    try :
        debugText += f', name = {self.object.application.focus.name}'
    except : pass
    return debugText

import Button, Surface
import eventFunction

print('Event library imported')

class Event:

    BUTTON = Button.Button.__name__
    SURFACE = Surface.Surface.__name__

    def __init__(self,object,
        name = None,
        autoUpdate = False
    ):

        self.object = object
        self.application = self.object.application

        if name :
            self.name = name
        else :
            self.name = object.name
        # self.name = object.name
        self.targetClass = object.__class__.__name__

        self.status = eventFunction.EventStatus.NOT_RESOLVED
        self.autoUpdate = autoUpdate

        if self.object.name not in self.object.tutor.handler.events :
            self.object.tutor.handler.addEvent(self)
            # print('Event.object.tutor.handler.events.values()')
            # for event in self.object.tutor.handler.events.values() : print(f'   event.name = {event.name}')
        else :
            self.update()

        if self.autoUpdate :
            self.update(self)
            if self.status == eventFunction.EventStatus.RESOLVED :
                eventFunction.EventStatus.resolve(self)
            # else :
            #     print(f'Event.__init__(): {self.name} not resolved')

    def update(self,event):
        event.object.handleEvent(event)

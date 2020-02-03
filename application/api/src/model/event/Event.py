import Button, Surface

print('Event library imported')

class Event:

    BUTTON = Button.Button.__name__
    SURFACE = Surface.Surface.__name__

    RESOLVED = 'RESOLVED'
    NOT_RESOLVED = 'NOT_RESOLVED'

    def __init__(self,object):

        self.name = object.name
        self.object = object
        self.type = object.__class__.__name__

        self.status = Event.NOT_RESOLVED

        if self.object.name not in self.object.handler.events :
            self.object.handler.addEvent(self)
            self.mustUpdate = False
        else :
            self.mustUpdate = True

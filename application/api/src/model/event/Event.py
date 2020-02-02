import Button, Surface

print('Event library imported')

class Event:

    BUTTON = Button.Button.__name__
    SURFACE = Surface.__name__

    def __init__(self,object):
        self.object = object
        self.className = object.__class__.__name__

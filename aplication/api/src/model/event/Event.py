from model.object.user_interface import Button

class Event:

    BUTTON = Button.Button.__name__

    def __init__(self,object):
        self.object = object
        self.className = object.__class__.__name__

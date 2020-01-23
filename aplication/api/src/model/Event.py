from function import importMannanger
pathMannanger = importMannanger.makeAplicationLibrariesAvaliable()
from model import Button

class Event:

    BUTTON = Button.Button.__name__

    def __init__(self,object):
        self.object = object
        self.className = object.__class__.__name__

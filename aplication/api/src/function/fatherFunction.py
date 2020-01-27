from model import Aplication
from model.object import Object

TAB = '         '

def isNotAplication(object) :
    return object.type!=Object.ObjectTypes.APLICATION

def absoluteFather(aplication):
    return aplication

def fatherMustUpdateNextFrame(object) :
    if isNotAplication(object) and not object.father.screen.mustUpdate :
        object.father.screen.mustUpdateNextFrame()

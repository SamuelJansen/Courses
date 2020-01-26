from model import Aplication
from model.object import Object

TAB = '         '

def isNotAplication(object) :
    # print(f'{TAB}{object.name}.screen.fatherFunction.isNotAplication(object) --> object.name = {object.name}')
    # print(f'{TAB}   isNotAplication = {object.name!=object.father.name}')
    # print(f'{TAB}      object.name = {object.name}')
    # print(f'{TAB}      object.father.name = {object.father.name}')
    return object.type!=Object.ObjectTypes.APLICATION

def absoluteFather(aplication):
    return aplication

def fatherMustUpdateNextFrame(object) :
    if isNotAplication(object) and not object.father.screen.mustUpdate :
        object.father.screen.mustUpdateNextFrame()

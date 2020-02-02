import Object

def isNotAplication(object) :
    return object.type!=Object.ObjectType.APPLICATION

def absoluteFather(aplication):
    return aplication

def fatherMustUpdateNextFrame(object) :
    if isNotAplication(object) and not object.father.screen.mustUpdate :
        object.father.screen.mustUpdateNextFrame()

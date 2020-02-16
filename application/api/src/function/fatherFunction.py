import objectFunction

def isNotAplication(object) :
    return object.type != objectFunction.Type.APPLICATION

def absoluteFather(aplication):
    return aplication

def fatherMustUpdateNextFrame(object) :
    if isNotAplication(object) and not object.father.screen.mustUpdate :
        object.father.screen.mustUpdateNextFrame()

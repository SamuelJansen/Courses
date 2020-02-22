import objectFunction

def isNotAplication(object) :
    return object.type != objectFunction.Type.APPLICATION

def absoluteFather(application):
    return application

def fatherMustUpdateNextFrame(object) :
    if isNotAplication(object) and not object.father.screen.mustUpdate :
        object.father.screen.mustUpdateNextFrame()

def getAbsoluteFather(application):
    if application.floor :
        return application.floor
    return application

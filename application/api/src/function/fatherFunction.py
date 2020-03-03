import objectFunction

def isNotAplication(object) :
    return object.type != objectFunction.Type.APPLICATION

def absoluteFather(application):
    return application

def getAbsoluteFather(application):
    if application.floor :
        return application.floor
    return application

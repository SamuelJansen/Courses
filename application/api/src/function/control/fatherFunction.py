import objectFunction, applicationFunction

def isNotAplication(object) :
    return object.type != objectFunction.Type.APPLICATION

def absoluteFather(application):
    return application

def getAbsoluteFather(application):
    if application.session :
        return application.session.desk
    if application.floor :
        return application.handler.objects[applicationFunction.getFloorName(application)]
    return application

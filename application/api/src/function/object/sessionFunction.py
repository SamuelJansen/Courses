import headerFunction

class Attribute:

    NAME = 'Session'


class Page:

    HOME = 'HomePage'


def getDeskPosition(application,
        header = None
    ) :
    if not header :
        header = tryGetHeader(application)
    if header :
        return [0,header.size[1] + 1]
    else :
        return [0,0]

def getDeskSize(application,
        header = None
    ) :
    if not header :
        header = tryGetHeader(application)
    if header :
        applicationSize = application.size.copy()
        applicationHeaderSize = header.size.copy()
        return [
            applicationSize[0],
            applicationSize[1] - applicationHeaderSize[1]
        ]
    else :
        return application.size.copy()

def tryGetHeader(application) :
    try :
        return application.findObjectByName(headerFunction.Attribute.NAME)
    except : pass

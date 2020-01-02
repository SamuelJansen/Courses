def makeAplicationLibrariesAvaliable() :
    baseApiPath = 'api/src/'
    from pathlib import Path
    userPath = str(Path.home())
    import sys
    sys.path.append(userPath+'/Morgs/')
    sys.path.append(userPath+'/Courses/course/'+baseApiPath)
    return userPath + '/'

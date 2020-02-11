def stashPadding(padding,father) :
    if padding :
        originalPadding = padding.copy()
    else :
        try :
            originalPadding = father.padding.copy()
        except :
            originalPadding = [0,0]
    padding = [0,0]
    return padding,originalPadding

import applicationFunction

class ItemDto:

    def __init__(self,name,
        position = None,
        size = None,
        text = None,
        textPosition = None,
        onLeftClick = None,
        onMenuResolve = None,
        onHovering = None,
        imagePath = None,
        audioPath = None,
        priority = applicationFunction.Priority.NO_PRIORITY
    ):
        self.name = name
        self.position = self.getCopy(position)
        self.size = self.getCopy(size)
        self.text = text
        self.textPosition = self.getCopy(textPosition)
        self.onLeftClick = onLeftClick
        self.onMenuResolve = onMenuResolve
        self.onHovering = onHovering
        self.imagePath = imagePath
        self.audioPath = audioPath
        self.priority = priority

    def getCopy(self,list):
        if list :
            return list.copy()
        else :
            return None


BUTTON_SIZE = [85,45]

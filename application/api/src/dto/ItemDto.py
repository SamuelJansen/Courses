import applicationFunction

class ItemDto:

    def __init__(self,name,
        position = None,
        size = None,
        text = None,
        textPosition = None,
        onLeftClick = None,
        onMenuResolve = None,
        priority = applicationFunction.Priority.NO_PRIORITY
    ):
        self.name = name
        self.position = position
        self.size = size
        self.text = text
        self.textPosition = textPosition
        self.onLeftClick = onLeftClick
        self.onMenuResolve = onMenuResolve
        self.priority = priority

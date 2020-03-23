import sessionFunction

print('Session library imported')

class Session:

    def __init__(self,desk,
        onDeskUpdate = None,
        onClose = None
    ):

        self.desk = desk
        self.application = self.desk.application
        self.name = f'{sessionFunction.Attribute.NAME}.{desk.name}'

        self.updatePage(sessionFunction.Page.HOME)
        self.itemNames = {}

        self.mustClose = False

        self.onDeskUpdate = onDeskUpdate
        self.onClose = onClose

    def updatePage(self,page):
        self.page = page

    def updateDesk(self,itemsSessionDtoList,
        onDeskUpdate = None
    ):

        if onDeskUpdate :
            self.onDeskUpdate = onDeskUpdate
        self.resetOldDesk()

        itemsDto,itemsClass,priority = self.onDeskUpdate(itemsSessionDtoList,self)
        self.application.memoryOptimizer.newObjects(itemsDto,itemsClass,
            priority = priority,
            afterBuildObject = self.addItemName
        )

    def resetOldDesk(self):
        self.resetItemNames()
        self.desk.handler.removeObjectTree()

    def resetItemNames(self):
        self.itemNames = {}

    def addItemName(self,itemDto):
        if self.page not in self.itemNames :
            self.itemNames[self.page] = []
        if itemDto.name not in self.itemNames[self.page] :
            self.itemNames[self.page].append(itemDto.name)

    def removeItemNames(self,itemNames):
        for itemName in itemNames :
            for page in self.itemNames :
                pageItemNames = self.itemNames[page].copy()
                if itemName in pageItemNames :
                    self.itemNames[page].remove(itemName)

    def removeItemNamesFromPage(self,page):
        if page in self.itemNames :
            del self.itemNames[page]

    def revealDeskItems(self,itemNames):
        self.desk.screen.reveaObjects(itemNames)

    def hideAllDeskItems(self):
        self.desk.screen.hideAllObjects()

    def removeDesk(self):
        self.application.getFloor().handler.removeObject(self.desk)

    def getNamesFromItemsDto(self,itemsSessionDtoList):
        return [itemDto.name for itemDto in itemsSessionDtoList]

    def keepCurrentSession(self):
        pass

    def close(self,event,
        onClose = None
    ):
        if onClose :
            self.onClose = onClose

        self.mustClose = True
        if self.onClose :
            self.onClose(event)
        if self.mustClose :
            self.removeDesk()
            self.application.session = None
            self.application.memoryOptimizer.reset()

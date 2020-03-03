import ItemSet, ItemDto, Event
import eventFunction, itemSetFunction, applicationFunction

print('MenuEvent library imported')

class MenuEvent(Event.Event):

    def update(self):
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,apiModule,itemsPackage,itemsPathTree,onLeftClick,onMenuResolve,
        name = None,
        type = eventFunction.Type.MENU_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        self.apiModule = apiModule
        self.itemsPackage = itemsPackage
        self.itemsPathTree = itemsPathTree
        self.itemsPathTreePointer = self.getItemsPathTreePointer()
        self.itemsPath = self.getItemsPath()
        self.itemNamesFilePath = self.getItemNamesFilePath()
        self.itemNames = eventFunction.getItemNames(self.itemsPath)
        self.itemsDto = []
        for index in range(len(self.itemNames)) :
            self.itemsDto.append(ItemDto.ItemDto(
                self.itemNames[index],
                text = self.itemNames[index],
                onLeftClick = onLeftClick,
                onMenuResolve = onMenuResolve
            ))

        self.execute()

    def getItemsPathTreePointer(self):
        BACK_SLASH = self.application.pathMannanger.backSlash
        return len(self.itemsPathTree[:-1].split(BACK_SLASH)) - 1

    def getItemsPath(self):
        itemsPath = ''
        BACK_SLASH = self.application.pathMannanger.backSlash
        for itemNameIndex in range(self.itemsPathTreePointer+1) :
            itemsPath += f'{self.itemsPathTree[:-1].split(BACK_SLASH)[itemNameIndex]}{BACK_SLASH}'
        return f'{self.object.application.pathMannanger.getApiModulePath(self.apiModule)}{self.itemsPackage}{itemsPath}'

    def getItemNamesFilePath(self):
        BACK_SLASH = self.application.pathMannanger.backSlash
        return f'{self.getItemsPath()}{self.getItemsPath()[:-1].split(BACK_SLASH)[-1]}.{self.application.extension}'

    def buildItems(self,itemsDirection):
        itemSetName = f'{itemSetFunction.Attribute.NAME}'
        itemSetFather = self.object

        ItemSet.ItemSet(itemSetName,itemSetFather,
            itemsDto = self.itemsDto,
            itemsDirection = itemsDirection,
            itemsPriority = applicationFunction.Priority.HIGHT,
            noImage = True,
        )

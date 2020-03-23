import ItemSet, ItemDto, Event
import eventFunction, itemSetFunction, applicationFunction

print('MenuEvent library imported')

class MenuEvent(Event.Event):

    def update(self):
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,itemsPathTree,onLeftClick,onMenuResolve,
        name = None,
        itemSize = None,
        type = eventFunction.Type.MENU_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        self.itemsPathTree = itemsPathTree
        self.itemNames = list(self.itemsPathTree.keys())
        self.itemSize = itemSize
        self.itemsDto = []
        for index in range(len(self.itemNames)) :
            self.itemsDto.append(ItemDto.ItemDto(
                self.itemNames[index],
                text = self.itemNames[index],
                onLeftClick = onLeftClick,
                onMenuResolve = onMenuResolve
            ))

        self.execute()

    def buildItems(self,itemsDirection):
        itemSetName = f'{itemSetFunction.Attribute.NAME}'
        itemSetFather = self.object

        ItemSet.ItemSet(itemSetName,itemSetFather,
            itemsDto = self.itemsDto,
            itemsDirection = itemsDirection,
            itemsPriority = applicationFunction.Priority.HIGHT,
            itemSize = self.itemSize,
            noImage = True,
        )

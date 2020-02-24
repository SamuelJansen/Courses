import MenuEvent, MenuNavigationEvent
import eventFunction, itemSetFunction

print('MenuAccessEvent library imported')

class MenuAccessEvent(MenuEvent.MenuEvent):

    def update(self):
        self.buildItems(itemSetFunction.Type.DOWN,MenuNavigationEvent.MenuNavigationEvent)
        self.updateStatus(eventFunction.Status.NOT_RESOLVED)

    def __init__(self,object,apiModule,itemsPackage,itemsPathTree,
        name = None,
        type = eventFunction.Type.MENU_ACCESS_EVENT,
        inherited = False
    ):

        MenuEvent.MenuEvent.__init__(self,object,apiModule,itemsPackage,itemsPathTree,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()
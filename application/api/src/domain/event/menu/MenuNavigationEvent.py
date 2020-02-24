import MenuEvent
import eventFunction, itemSetFunction

print('MenuNavigationEvent library imported')

class MenuNavigationEvent(MenuEvent.MenuEvent):

    def update(self):
        self.removeFatherPreviousMenuNavigationEvent(self.object.father)
        self.buildItems(itemSetFunction.Type.RIGHT,MenuNavigationEvent)
        self.updateStatus(eventFunction.Status.NOT_RESOLVED)

    def __init__(self,event,
            name = None,
            type = eventFunction.Type.MENU_NAVIGATION_EVENT,
            inherited = False
    ):
    
        event.updateStatus(eventFunction.Status.RESOLVED)

        fatherTutorEventType = self.getFatherTutorEventType(event)
        fatherTutorMenuNavigationEvent = event.object.father.tutor.handler.events[f'{fatherTutorEventType}.{event.object.father.tutor.name }']
        object = event.object
        apiModule = fatherTutorMenuNavigationEvent.apiModule
        itemsPackage = fatherTutorMenuNavigationEvent.itemsPackage
        itemsPathTree = f'{fatherTutorMenuNavigationEvent.itemsPathTree}{eventFunction.getObjectName(event)}\\'

        MenuEvent.MenuEvent.__init__(self,object,apiModule,itemsPackage,itemsPathTree,
            name = None,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()

    def removeFatherPreviousMenuNavigationEvent(self,father):
        father.handler.removeAllEvents()
        for objectSon in father.handler.objects.values() :
            objectSon.handler.removeStudentTree()

    def getFatherTutorEventType(self,event):
        fatherTutorEventList = list(event.object.father.tutor.handler.events.values())
        for fatherTutorEvent in fatherTutorEventList :
            fatherTutorEventType = eventFunction.getEventType(fatherTutorEvent)
            if (
                fatherTutorEventType == eventFunction.Type.MENU_ACCESS_EVENT or
                fatherTutorEventType == eventFunction.Type.MENU_NAVIGATION_EVENT
            ) :
                return fatherTutorEventType

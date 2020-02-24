import MenuEvent, EventError, ExecussionEvent, RemoveFocusEvent
import eventFunction, itemSetFunction

print('MenuNavigationEvent library imported')

class MenuNavigationEvent(MenuEvent.MenuEvent):

    def update(self):
        self.removeFatherPreviousMenuNavigationEvent(self.object.father)
        self.applicationScriptFile = self.getApplicationScript()
        print(f'MenuNavigationEvent.update(): MenuNavigationEvent.applicationScriptFile = {self.applicationScriptFile}')
        if self.applicationScriptFileIsValid() :
            self.object.updateExecussionFunction(self.externalFunction)
            ExecussionEvent.ExecussionEvent(self)
            self.updateStatus(eventFunction.Status.RESOLVED)
            RemoveFocusEvent.RemoveFocusEvent(self.application)
        else :
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
        externalFunction = self.getExecussionFunction(fatherTutorMenuNavigationEvent)

        object = event.object
        apiModule = fatherTutorMenuNavigationEvent.apiModule
        itemsPackage = fatherTutorMenuNavigationEvent.itemsPackage
        itemsPathTree = f'{fatherTutorMenuNavigationEvent.itemsPathTree}{eventFunction.getObjectName(event)}\\'

        MenuEvent.MenuEvent.__init__(self,object,apiModule,itemsPackage,itemsPathTree,externalFunction,
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
        return eventFunction.findEventByType(
            [eventFunction.Type.MENU_ACCESS_EVENT,eventFunction.Type.MENU_NAVIGATION_EVENT],
            event.object.father.tutor.handler.events.values()
        ).type

    def getApplicationScript(self):
        for itemName in self.itemNames :
            if itemName.strip().split('.')[-1].strip() == self.application.extension :
                return itemName

    def applicationScriptFileIsValid(self):
        if self.applicationScriptFile :
            applicationScriptFileIsValid = (self.applicationScriptFile == f'{self.object.father.tutor.name}.{self.object.name}.{self.application.extension}')
            if not applicationScriptFileIsValid :
                EventError.EventError(self,
                    message = 'errorMessage'
                )
            return applicationScriptFileIsValid

    def getExecussionFunction(self,fatherTutorMenuNavigationEvent):
        return fatherTutorMenuNavigationEvent.externalFunction

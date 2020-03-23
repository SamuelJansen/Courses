import MenuEvent, ErrorEvent, ExecussionEvent, RemoveFocusEvent, NewSessionEvent
import eventFunction, itemSetFunction, textFunction

print('MenuNavigationEvent library imported')

class MenuNavigationEvent(MenuEvent.MenuEvent):

    def update(self):
        self.removeFatherPreviousMenuNavigationEvent()
        self.applicationScriptFile = self.getApplicationScript()
        if self.itemsPathTree :
            self.buildItems(itemSetFunction.Type.RIGHT)
            self.updateStatus(eventFunction.Status.NOT_RESOLVED)
        else :
            if not self.application.session :
                NewSessionEvent.NewSessionEvent(self)
            ExecussionEvent.ExecussionEvent(self)
            self.updateStatus(eventFunction.Status.RESOLVED)
            RemoveFocusEvent.RemoveFocusEvent(self.application)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.MENU_NAVIGATION_EVENT,
        inherited = False
    ):

        event.updateStatus(eventFunction.Status.RESOLVED)

        fatherTutorEventType = self.getFatherTutorEventType(event)
        fatherTutorMenuNavigationEvent = event.object.father.tutor.handler.events[f'{fatherTutorEventType}.{event.object.father.tutor.name}']

        object = event.object
        itemsPathTree = fatherTutorMenuNavigationEvent.itemsPathTree[event.object.name]
        onLeftClick = event.object.onLeftClick
        onMenuResolve = event.object.onMenuResolve

        MenuEvent.MenuEvent.__init__(self,object,itemsPathTree,onLeftClick,onMenuResolve,
            name = None,
            itemSize = fatherTutorMenuNavigationEvent.itemSize,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        if fatherTutorEventType == eventFunction.Type.MENU_NAVIGATION_EVENT :
            self.navigationHistory = f'{fatherTutorMenuNavigationEvent.navigationHistory}{event.object.name}\\'
        else :
            self.navigationHistory = f'{event.object.name}\\'

        self.execute()

    def removeFatherPreviousMenuNavigationEvent(self):
        self.object.father.handler.removeAllEvents()
        for objectSon in self.object.father.handler.objects.values() :
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
                ErrorEvent.ErrorEvent(self,
                    message = 'errorMessage'
                )
            return applicationScriptFileIsValid

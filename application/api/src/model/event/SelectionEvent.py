import Event, Mouse

print('SelectionEvent library imported')

class SelectionEvent:

    def __init__(self,mouse):

        self.application = mouse.application
        self.mouse = self.application.mouse
        object = self.getObject(self.mouse)

        if object :
            Event.Event.__init__(self,object)

            self.state = self.mouse.state
            self.objectSelected = self.mouse.objectSelected
            self.selectionTime = self.object.application.timeNow

            if self.mustUpdate :
                self.update(self)
            else :
                self.lastSelectionTime = self.object.application.timeNow

    def update(self,newEvent):
        if self.object.singleClickSelectable :
            self.proceedSelection(newEvent)
        elif self.object.doubleClickSelectable :
            if newEvent.selectionTime - self.lastSelectionTime < 1 :
                self.proceedSelection(newEvent)
            else :
                self.lastSelectionTime = newEvent.selectionTime

    def proceedSelection(self,newEvent):
        if newEvent.state == Mouse.Mouse.LEFT_CLICK_DOWN :
            self.deleteEvent()
            SelectionEvent(self.mouse)

        elif (newEvent.state == Mouse.Mouse.LEFT_CLICK_UP) and newEvent.objectSelected :
            print(f'  !! !! !! newEvent.objectSelected.name = {newEvent.objectSelected.name}')

            if self.application.focus and (self.application.focus != newEvent.objectSelected) :
                self.mouse.removeFocus()#self.deleteEvent()
            self.select(newEvent.objectSelected)

    def select(self,object):
        event = Event.Event(object)
        print()
        if event.type == Event.Event.BUTTON :
            if object.handleEvent(event) == Event.Event.RESOLVED :
                self.deleteEvent()

    def getObject(self,mouse):
        if mouse.objectHitClickDown :
            return mouse.objectHitClickDown
        if mouse.objectHitClickUp :
            return mouse.objectHitClickUp

    def deleteEvent(self):
        print(f'    DELETE EVENT CALL')
        self.status = Event.Event.RESOLVED
        self.mouse.removeFocus()
        self.object.handler.deleteEvent(self.name)
        print(f'    END OF DELETE EVENT')

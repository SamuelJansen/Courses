import Event
import eventFunction, mouseFunction, objectFunction

print('FocusEvent library imported')

class FocusEvent(Event.Event):

    def update(self):
        if self.application.mouse.state == mouseFunction.State.LEFT_CLICK_DOWN :
            if self.inFocusTree(self.object) :
                self.updateFocus()
            elif self.object != self.application.focus :
                self.removeFocus()
        elif self.application.mouse.state == mouseFunction.State.LEFT_CLICK_UP :
            if not self.application.focus :
                self.setFocus()
            else :
                if self.inFocusTree(self.object) :
                    self.updateFocus()
                else :
                    self.removeFocus()
        else :
            self.removeFocus()

        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,
        name = None,
        type = eventFunction.Type.FOCUS_EVENT,
        inherited = False
    ):

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited
        self.execute()

    def inFocusTree(self,object):
        if object.type == objectFunction.Type.APPLICATION :
            return False
        elif object == self.application.focus :
            return True
        return self.inFocusTree(object.tutor)

    def setFocus(self):
        # print()
        # print('............................................................................................................................................................')
        # print(f'FocusEvent.setFocus(): {self.object.name}')
        if not self.application.focus :
            self.application.focus = self.object
        else :
            debugText = 'Application already in focus\n'
            debugText += f'     actual focus = {self.application.focus.name}\n'
            debugText += f'     new focus = {self.object.name}'
            self.application.holdForDebug(debugText)
        # print('............................................................................................................................................................')
        # print()

    def updateFocus(self):
        ###- Just that simple for now
        pass

    def removeFocus(self):
        # print()
        # print('............................................................................................................................................................')
        # print(f'FocusEvent.removeFocus():',end='')
        if self.application.focus :
            # print(f' {self.application.focus.name}')
            self.application.focus.handler.removeAllEvents()
            self.application.focus.handler.removeStudentTree()
            self.application.focus.handler.removeObjectTree()
            self.application.focus = None


        else :
            # print()
            pass
        # print('............................................................................................................................................................')
        # print()

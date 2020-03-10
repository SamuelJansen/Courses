import Event, ErrorEvent
import eventFunction, applicationFunction

print('ExecussionEvent library imported')

class ExecussionEvent(Event.Event):

    def update(self):
        if self.event.type == eventFunction.Type.CLICK_EVENT and self.object.onLeftClick :
            if self.object.onLeftClick :
                self.object.onLeftClick(self.event)
        elif self.event.type == eventFunction.Type.MENU_NAVIGATION_EVENT :
            if self.object.onMenuResolve :
                self.object.onMenuResolve(self.event)
        elif self.event.type == eventFunction.Type.HOVER_EVENT :
            if self.object.onHovering :
                self.object.onHovering(self.event)
        else :
            ErrorEvent.ErrorEvent(self.event,
                message = f'{self.name}.update(): {self.object.type} funcion handler not implemented'
            )
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.EXECUSSION_EVENT,
        inherited = False
    ):
        object = event.object
        name = f'{event.type}.{type}.{event.object.name}'

        Event.Event.__init__(self,object,
        name = name,
        type = type,
        inherited = True
        )
        self.inherited = inherited

        self.event = event

        self.execute()

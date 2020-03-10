import eventFunction

print('Event library imported')

class Event:

    def update(self,*args,**kargs):
        import ErrorEvent
        ErrorEvent.ErrorEvent(self.object,
            message = f'{self.type}.update() method not implemented'
        )
        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,object,
        name = None,
        type = eventFunction.Type.EVENT,
        inherited = False
    ):

        if object :
            self.object = object
            self.application = self.object.application
            self.inherited = inherited
            self.newEvent = True

            if type :
                self.type = type
            else :
                self.type = eventFunction.Type.EVENT

            if name :
                self.name = name
            else :
                self.name = f'{self.type}.{object.name}'
            self.targetClass = object.__class__.__name__

            self.status = eventFunction.Status.NOT_RESOLVED

            if self.name not in self.object.handler.events :
                # print(f'{self.name} event added to {self.object.name}.handler.events')
                self.object.handler.addEvent(self)
            elif self.object.handler.events[self.name].status == eventFunction.Status.NOT_RESOLVED :
                # print(f'{self.name} event not added to {self.object.name}.handler.events')
                self.object.handler.events[self.name].update()
                self.newEvent = False

            self.execute()

        else :
            import ErrorEvent
            ErrorEvent.ErrorEvent(None,
                message = getObjectHitDebugText(object)
            )
            

    def resolve(self,*args,**kargs):
        if self.status == eventFunction.Status.RESOLVED :
            self.object.handler.removeEvent(self)

    def execute(self,*args,**kargs):
        if not self.inherited and self.newEvent :
            self.update(*args,**kargs)
            self.resolve(*args,**kargs)

    def updateStatus(self,status):
        initialStatus = self.status
        if self.status != eventFunction.Status.REMOVED :
            self.status = status
        # print(f'{self.name}.updateStatus() from {initialStatus} to {self.status}')


def getObjectFocusDebugText(self):
    debugText = f' {self.name}, application.focus = {id(self.application.focus)}-{self.application.focus}'
    try :
        debugText += f', name = {self.application.focus.name}'
    except : pass
    return debugText

def getObjectHitDebugText(object) :
    debugText = ' -- Event:\n'
    debugText += '''Event(object): object = None\n'''
    debugText += f'mouse.objectHit = {object.application.mouse.objectHit}\n'
    try :
        debugText += f'mouse.objectHit.name = {object.application.mouse.objectHit.name}\n'
    except : pass
    debugText += f'mouse.objectHitDown = {object.application.mouse.objectHitDown}\n'
    try :
        debugText += f'mouse.objectHitDown.name = {object.application.mouse.objectHitDown.name}\n'
    except : pass
    debugText += f'mouse.objectHitUp = {object.application.mouse.objectHitUp}\n'
    try :
        debugText += f'mouse.objectHitUp.name = {object.application.mouse.objectHitUp.name}\n'
    except : pass
    debugText += f'     Application.focus = {object.application.mouse.application.focus}\n'
    try :
        debugText += f'     Application.focus.name = {mouse.application.focus.name}\n'
    except : pass

    return debugText

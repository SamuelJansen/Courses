import ExecussionEvent, Desk
import eventFunction, headerFunction, deskFunction, sessionFunction

print('NewSessionEvent library imported')

class NewSessionEvent(ExecussionEvent.ExecussionEvent):

    def update(self):
        if self.desk :
            self.application.session.removeDesk()

        deskName = self.buildName()
        deskPosition = sessionFunction.getDeskPosition(self.application,
            header = self.header
        )
        deskSize = sessionFunction.getDeskSize(self.application,
            header = self.header
        )
        itemsDeskPerLine = 7
        deskFather = self.application.getFloor()

        self.application.newSession(
            Desk.Desk(deskName,deskSize,itemsDeskPerLine,deskFather,
                position = deskPosition,
                padding = [2,2],
                noImage = True
            ),
            self.event.navigationHistory
        )

        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.SESSION_EVENT,
        inherited = False
    ):

        ExecussionEvent.ExecussionEvent.__init__(self,event,
            name = name,
            type = type,
            inherited = True
        )

        if self.event.application.session and self.buildName() == self.event.application.session.name :
            self.keepCurrentSession()
        else :
            self.inherited = inherited

            self.header = self.application.getFloor().handler.objects[headerFunction.Attribute.NAME]
            self.desk = self.getDesk()

            self.execute()

    def getDesk(self):
        for objectName in self.application.getFloor().handler.objects.keys() :
            if deskFunction.Attribute.FIRST_NAME in objectName: ###- .split('.')[0] :
                return self.application.getFloor().handler.objects[objectName]

    def buildName(self):
        return f'{deskFunction.Attribute.FIRST_NAME}.{self.event.name}'

    def keepCurrentSession(self):
        self.updateStatus(eventFunction.Status.RESOLVED)

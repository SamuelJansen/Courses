import ExecussionEvent, Desk
import eventFunction, headerFunction

print('NewSessionEvent library imported')

class NewSessionEvent(ExecussionEvent.ExecussionEvent):

    DESK_NAME = 'Desk'

    def update(self):
        if self.desk :
            self.application.session.removeDesk()

        deskName = self.buildName()
        deskPosition = [0,self.header.size[1] + 1]
        deskSize = [self.application.size[0],self.application.size[1] - self.header.size[1]]
        itemsDeskPerLine = 7
        deskFather = self.application.getFloor()

        self.application.newSession(
            Desk.Desk(deskName,deskSize,itemsDeskPerLine,deskFather,
                position = deskPosition,
                padding = [2,2],
                noImage = True
            ),
            self.event.itemsPath
        )

        self.updateStatus(eventFunction.Status.RESOLVED)

    def __init__(self,event,
        name = None,
        type = eventFunction.Type.SESSION_EVENT,
        message = None,
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
            if NewSessionEvent.DESK_NAME in objectName.split('.')[0] :
                return self.application.getFloor().handler.objects[objectName]

    def buildName(self):
        return f'{NewSessionEvent.DESK_NAME}.{self.event.name}'

    def keepCurrentSession(self):
        self.updateStatus(eventFunction.Status.RESOLVED)

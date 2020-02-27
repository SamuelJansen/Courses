import ExecussionEvent, Desk
import eventFunction, headerFunction

print('NewSessionEvent library imported')

class NewSessionEvent(ExecussionEvent.ExecussionEvent):

    DESK_NAME = 'Desk'

    def update(self):

        if self.desk :
            self.application.session.removeDesk()

        name = f'{NewSessionEvent.DESK_NAME}.{self.event.name}'
        position = [0,self.header.size[1] + 1]
        size = [self.application.size[0],self.application.size[1] - self.header.size[1]]
        itemsPerLine = 7
        father = self.application.getFloor()

        self.desk = Desk.Desk(name,size,itemsPerLine,father,
            position = position,
            padding = [2,2],
            noImage = True
        )

        path = self.event.itemsPath
        application = self.application
        self.application.newSession(self.desk,path)

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
        self.inherited = inherited

        self.header = self.application.getFloor().handler.objects[headerFunction.Attribute.NAME]
        self.desk = self.getDesk()

        self.execute()

    def getDesk(self):
        for objectName in self.application.getFloor().handler.objects.keys() :
            if NewSessionEvent.DESK_NAME in objectName.split('.')[0] :
                return self.application.getFloor().handler.objects[objectName]

import Session, Message
import sessionFunction

print('EditorSession library imported')

class EditorSession(Session.Session):

    GOLDEN_RATIO = 1.57

    def __init__(self,desk,navigationHistory):

        Session.Session.__init__(self,desk)

        self.pathMannanger = self.application.pathMannanger
        self.path = f'{self.pathMannanger.getApiModulePath(self.pathMannanger.COURSE)}resourse\\modules\\{navigationHistory}'
        self.deskItemSize = [
            self.desk.size[0] // self.desk.itemsPerLine,
            int(self.desk.size[0] // self.desk.itemsPerLine / EditorSession.GOLDEN_RATIO)
        ]

    def save(self):
        Message.Message(self.desk,f'{self.name}.save()',
            fontSize = 18
        )

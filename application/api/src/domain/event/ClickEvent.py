import Event
import eventFunction, mouseFunction

print('ClickEvent library imported')

class ClickEvent(Event.Event):

    def update(self):
        print(f'ClickEvent() - {self.type}.update() - {self.name}')
        if self.object :
            self.updateClickTimes()

            if self.object.singleClickable :
                self.proceedClick()
            elif self.object.doubleClickable :
                if self.clickTime - self.lastclickTime < 1 and self.clickTime != self.lastclickTime:
                    self.proceedClick()

        self.status = eventFunction.Status.RESOLVED

    def __init__(self,mouse,
        object = None,
        name = None,
        type = eventFunction.Type.CLICK_EVENT,
        inherited = False
    ):

        if not object :
            object = mouse.objectHit

        Event.Event.__init__(self,object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        self.mouse = mouse
        self.clickTime = self.application.timeNow
        self.objectClicked = self.getObjectClicked()

        self.execute()

    def getObjectClicked(self):
        if self.mouse.objectHitDown == self.mouse.objectHitUp :
            return self.mouse.objectHit

    def updateClickTimes(self):
        self.lastclickTime = self.clickTime
        self.clickTime = self.application.timeNow

    def proceedClick(self):
        if self.mouse.state == mouseFunction.State.LEFT_CLICK_DOWN :
            pass
        if self.mouse.state == mouseFunction.State.LEFT_CLICK_UP :
            if self.objectClicked :
                self.click(self.objectClicked)

    def click(self,object):
        Event.Event(object)

import Event, Mouse
import eventFunction

print('ClickEvent library imported')

class ClickEvent:

    NAME = 'ClickEvent'

    def __init__(self,mouse):

        # print(f'ClickEvent.NAME = {ClickEvent.NAME}')
        self.mouse = mouse
        self.mouseObjectHit = self.getMouseObjectHit()

        if self.mouseObjectHit :
            # print(f'ClickEvent.mouseObjectHit.name = {self.mouseObjectHit.name}')
            Event.Event.__init__(self,self.mouseObjectHit,
                name = ClickEvent.NAME
            )

            if self.status == eventFunction.EventStatus.NOT_RESOLVED :
                self.mouseState = self.mouse.state
                self.clickTime = self.application.timeNow
                self.update()

    def getMouseObjectHit(self):
        if self.mouse.objectHitDown == self.mouse.objectHitUp :
            self.objectClicked = self.mouse.objectHitUp
            # print(f'-- ClickEvent.objectClicked.name = {self.objectClicked.name}')
        else :
            self.objectClicked = None
        if self.mouse.objectHitDown :
            if self.mouse.application.focus :
                self.mouse.removeFocus()
            return self.mouse.objectHitDown
        elif self.mouse.objectHitUp :
            return self.mouse.objectHitUp

    def update(self):
        self.updateClickTimes()
        if self.object.singleClickable :
            # print(f'ClickEvent.object.singleClickable = {self.object.singleClickable}')
            self.proceedClick()
        elif self.object.doubleClickable :
            # print(f'ClickEvent.object.doubleClickable = {self.object.doubleClickable}')
            if event.clickTime - self.lastclickTime < 1 :
                # print('ClickEvent.update(): Event.Click.mouse.removeFocus()')
                self.proceedClick()
        eventFunction.EventStatus.resolve(self)

    def updateClickTimes(self):
        self.lastclickTime = self.clickTime
        self.clickTime = self.application.timeNow

    def proceedClick(self):
        # print(f'ClickEvent.state = {self.mouseState}')
        # print(f'ClickEvent.state == Mouse.Mouse.LEFT_CLICK_UP = {self.mouseState == Mouse.Mouse.LEFT_CLICK_UP}')
        if (self.mouseState == Mouse.Mouse.LEFT_CLICK_UP) and self.mouseObjectHit :
            if self.application.focus and (self.application.focus != self.mouseObjectHit) :
                # print('ClickEvent.proceeedClick(): Event.Click.mouse.removeFocus()')
                self.mouse.removeFocus()#self.deleteEvent()
            if self.objectClicked :
                # print(f'ClickEvent.objectClicked.name = {self.objectClicked.name}')
                self.clickIt(self.objectClicked)

    def clickIt(self,object):
        # print(f'object.name = {object.name}')
        Event.Event(object,
            autoUpdate = True
        )
        self.mouseObjectHit = None
        self.objectClicked = None

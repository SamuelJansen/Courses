import Event
import eventFunction, mouseFunction

print('ClickEvent library imported')

class ClickEvent(Event.Event):

    def __init__(self,mouse):

        object = mouse.objectHit

        if not object :
            mouse.application.holdForDebug(getObjectHitDebugText(mouse))

        if object :
            Event.Event.__init__(self,object,
                name = eventFunction.Type.CLICK_EVENT,
                autoUpdate = False
            )

            self.mouse = mouse
            self.clickTime = self.application.timeNow
            self.objectClicked = self.getObjectClicked()
            self.update()
            self.resolve()

    def getObjectClicked(self):
        if self.mouse.objectHitDown == self.mouse.objectHitUp :
            return self.mouse.objectHit

    def update(self):
        print(f'------- START OF RESOLVE EVENT ------- {self.name}')
        if self.object :
            self.updateClickTimes()

            if self.object.singleClickable :
                self.proceedClick()
            elif self.object.doubleClickable :
                if self.clickTime - self.lastclickTime < 1 and self.clickTime != self.lastclickTime:
                    self.proceedClick()

    def updateClickTimes(self):
        self.lastclickTime = self.clickTime
        self.clickTime = self.application.timeNow

    def proceedClick(self):
        if self.mouse.state == mouseFunction.State.LEFT_CLICK_DOWN :
            pass
        if self.mouse.state == mouseFunction.State.LEFT_CLICK_UP :
            if self.objectClicked :
                self.clickIt(self.objectClicked)

    def clickIt(self,object):
        Event.Event(object)


def getObjectHitDebugText(mouse) :

    debugText = ' -- ClickEvent:\n'
    debugText += '''Mouse didn't hit any object\n'''
    debugText += f'mouse.objectHit = {mouse.objectHit}\n'
    try :
        debugText += f'mouse.objectHit.name = {mouse.objectHit.name}\n'
    except : pass
    debugText += f'mouse.objectHitDown = {mouse.objectHitDown}\n'
    try :
        debugText += f'mouse.objectHitDown.name = {mouse.objectHitDown.name}\n'
    except : pass
    debugText += f'mouse.objectHitUp = {mouse.objectHitUp}\n'
    try :
        debugText += f'mouse.objectHitUp.name = {mouse.objectHitUp.name}\n'
    except : pass
    debugText += f'     Application.focus = {mouse.application.focus}\n'
    try :
        debugText += f'     Application.focus.name = {mouse.application.focus.name}\n'
    except : pass

    return debugText

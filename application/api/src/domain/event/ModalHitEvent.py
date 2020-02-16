import Event
import eventFunction, mouseFunction

print('ModalHitEvent library imported')

class ModalHitEvent(Event.Event):

    def update(self):
        pass
        
    def __init__(self,mouse):

        object = mouse.objectHit

        if object :
            Event.Event.__init__(self,object,
                name = eventFunction.Type.MODAL_HIT_EVENT,
                autoUpdate = False
            )

            self.mouse = mouse
            self.clickTime = self.application.timeNow
            self.objectClicked = self.getObjectClicked()
            self.update()
            self.resolve()

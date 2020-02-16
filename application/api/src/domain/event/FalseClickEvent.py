import ClickEvent
import eventFunction, mouseFunction, modalFunction

print('FalseClickEvent library imported')

class FalseClickEvent(ClickEvent.ClickEvent):

    def update(self):
        if self.mouse.state == mouseFunction.State.LEFT_CLICK_DOWN :
            if eventFunction.Type.MODAL in self.object.handler.inheritanceTree :
                print(f'FalseClickEvent(): {self.type}.update() - {self.name}')
                print(f'FalseClickEvent(): {self.name}.mouse.objectHit.handler.inheritanceTree = {self.object.handler.inheritanceTree}')
                self.object.father.handler.removeObjectTree(self.object)
        self.status = eventFunction.Status.RESOLVED

    def __init__(self,mouse,object,
        name = None,
        type = eventFunction.Type.FALSE_CLICK_EVENT,
        inherited = False
    ):

        ClickEvent.ClickEvent.__init__(self,mouse,
            object = object,
            name = name,
            type = type,
            inherited = True
        )
        self.inherited = inherited

        self.execute()




    # def hittingFocusChild(self,object):
    #     if object.father == self.application.focus :
    #         return True
    #     elif (
    #             object.father.type == objectFunction.Type.APPLICATION and
    #             object.father.tutor.type == objectFunction.Type.APPLICATION
    #         ) :
    #         return False
    #     elif (
    #             object.father.type == objectFunction.Type.APPLICATION and
    #             object.father.tutor.type != objectFunction.Type.APPLICATION
    #         ) :
    #         return self.hittingApplicationFocusChild(object.father)
    #     else :
    #         return self.hittingApplicationFocusChild(object.tutor)

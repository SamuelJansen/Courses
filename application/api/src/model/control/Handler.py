import Object
import imageFunction, fatherFunction

print('Handler library imported')

class Handler:

    def __init__(self,object):
        self.object = object
        self.objects = {}
        self.collidableObjects = {}
        self.collidableObjectsRect = []

        self.updateOriginalAttributes()

        if fatherFunction.isNotAplication(self.object) :
            self.object.father.handler.addObject(self.object)

    def updateOriginalAttributes(self):
        self.originalPosition = self.object.position.copy()
        self.originalSize = self.object.size.copy()
        self.originalImage = self.object.image.copy()
        self.originalSurface = self.object.screen.surface.copy()

    def update(self):
        pass

    def itColided(self,object):
        if object.collides :
            colisionIndexes = object.collidableRect.collidelistall(self.collidableObjectsRect)
            if list(self.collidableObjects.keys()).index(object.name) in colisionIndexes :
                return len(colisionIndexes)>1
            return len(colisionIndexes)>0
        return False

    def isSelected(self,selectionPoint):
        print(f'handler.object.name = {self.object.name}')
        if self.object.selectable :
            try :
                notSelected = True
                pixelColor = self.object.screen.surface.get_at(selectionPoint)
                notSelected = (pixelColor[0] == Object.Object.NOT_SELECTABLE_COLOR[0]) and notSelected
                notSelected = (pixelColor[1] == Object.Object.NOT_SELECTABLE_COLOR[1]) and notSelected
                notSelected = (pixelColor[2] == Object.Object.NOT_SELECTABLE_COLOR[2]) and notSelected
                notSelected = (pixelColor[3] == Object.Object.NOT_SELECTABLE_COLOR[3]) and notSelected
                print(f'object hit name = {self.object.name}, pixelColor = {pixelColor}')
                print(f'    notSelected = {notSelected}')
                return not notSelected
            except :
                print(f'    selected = {notSelected}')
                return True
        print(f'    notSelected = {notSelected}')
        return False

    def updateCollidableObjects(self):
        self.collidableObjects = {object.name:object for object in sorted(self.objects.values(),key=self.renderOrder) if object.collides}
        self.collidableObjectsRect = [object.collidableRect for object in self.collidableObjects.values()]

    def renderOrder(self,object):
        return object.blitOrder,object.collidableRect.bottom

    def addObject(self,object):
        self.object.father.screen.reset()
        self.objects[object.name] = object
        self.object.screen.mustUpdateNextFrame()

    def deleteObject(self,objectName):
        print(f'ObjectHandler.object.name = {self.object.name}, ObjectHandler.deleteObject({objectName})')
        del self.objects[objectName]
        self.object.screen.mustUpdateNextFrame()

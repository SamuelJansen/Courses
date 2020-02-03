import fatherFunction

print('Handler library imported')

class Handler:

    def __init__(self,object):
        self.object = object
        self.objects = {}
        self.events = {}
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
        print(f'---------------> Handler.object.name = {self.object.name}, Handler.deleteObject({objectName}), Handler.object.father.name = {self.object.father.name}')
        del self.objects[objectName]
        self.object.screen.mustUpdateNextFrame()

    def addEvent(self,newEvent):
        self.events[newEvent.name] = newEvent

    def updateEvent(self,newEvent):
        self.events[newEvent.name].update(newEvent)

    def deleteEvent(self,eventName):
        del self.events[eventName]

import fatherFunction, eventFunction

print('Handler library imported')

class Handler:

    def __init__(self,object):
        self.object = object
        self.application = self.object.application
        self.objects = {}
        self.relatives = {}
        self.events = {}
        self.collidableObjects = {}
        self.collidableObjectsRect = []

        self.updateObjectOriginalAttributes()

        if fatherFunction.isNotAplication(self.object) :
            self.object.father.handler.addObject(self.object)

    def updateObjectOriginalAttributes(self):
        self.originalPosition = self.object.position.copy()
        self.originalSize = self.object.size.copy()
        self.originalImage = self.object.image.copy()
        self.originalSurface = self.object.screen.surface.copy()

    def updateOriginalSurface(self):
        self.originalSurface = self.object.screen.surface.copy()

    def getOriginalPosition(self):
        return self.originalPosition

    def getOriginalSize(self):
        return self.originalSize

    def fixOriginalPosition(self):
        try :
            if self.object.padding :
                self.originalPosition = [
                    self.originalPosition[0] - self.object.padding[0],
                    self.originalPosition[1] - self.object.padding[1]
                ]
            elif self.object.tutor.padding :
                self.originalSize = [
                    self.originalPosition[0] + (2 * self.object.tutor.padding[0]),
                    self.originalPosition[1] + (2 * self.object.tutor.padding[1])
                ]
        except : pass

    def fixOriginalSize(self):
        try :
            if self.object.padding :
                self.originalSize = [
                    self.originalSize[0] + (2 * self.object.padding[0]),
                    self.originalSize[1] + (2 * self.object.padding[1])
                ]
            elif self.object.tutor.padding :
                self.originalSize = [
                    self.originalSize[0] + (2 * self.object.tutor.padding[0]),
                    self.originalSize[1] + (2 * self.object.tutor.padding[1])
                ]
        except : pass

    def update(self):
        pass

    def itColided(self,object):
        if object.collides :
            colisionIndexes = object.collidableRect.collidelistall(self.collidableObjectsRect)
            if list(self.collidableObjects.keys()).index(object.name) in colisionIndexes :
                return len(colisionIndexes) > 1
            return len(colisionIndexes) > 0
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
        # print(f'---------------> Handler.object.name = {self.object.name}, Handler.deleteObject({objectName}), Handler.object.father.name = {self.object.father.name}')
        self.objects[objectName].handler.deleteChildren()
        self.objects[objectName].handler.deleteRelativeChildren()
        if objectName in self.objects :
            if self.objects[objectName].handler.events :
                debugText = f'Handler.objects[{objectName}].handler.event:\n'
                for event in self.objects[objectName].handler.events.values() :
                    debugText += f'    {event.name}\n'
                self.application.holdForDebug(debugText)
            self.deleteItFromItsRelative(objectName)
            del self.objects[objectName]
            self.object.screen.mustUpdateNextFrame()
        else :
            self.application.holdForDebug(
                f'Handler.deleteObject(): {objectName} not found in {self.object.name}.handler.objects'
            )

    def forceDeleteObject(self,objectName):
        if objectName in self.objects :
            if self.objects[objectName].handler.relatives :
                for relative in self.objects[objectName].handler.relatives.values() :
                    self.objects[objectName].handler.forceDeleteObject(relative)
            for son in self.objects[objectName].handler.objects.values() :
                if son.name in self.objects[objectName].tutor.handler.events :
                    eventFunction.EventStatus.forceResolve(self.objects[objectName].tutor.handler.events[son.name])
            if self.objects[objectName].tutor.name in self.objects[objectName].tutor.tutor.handler.events :
                eventFunction.EventStatus.forceResolve(self.objects[objectName].tutor.tutor.handler.events[self.objects[objectName].tutor.name])

            self.objects[objectName].father.handler.deleteObject(objectName)

    def deleteChildren(self):
        if self.objects :
            childrenNames = self.objects.fromkeys(self.objects.keys(),None)
            for childName in childrenNames :
                if self.objects[childName].handler.objects :
                    self.objects[childName].handler.deleteChildren()
                else :
                    self.deleteObject(childName)

    def deleteRelativeChildren(self):
        if self.relatives :
            relativeChildrenNames = self.relatives.fromkeys(self.relatives.keys(),None)
            for relativeChildName in relativeChildrenNames :
                if self.relatives[relativeChildName].handler.relatives :
                    self.relatives[relativeChildName].handler.deleteRelativeChildren()
                else :
                    self.deleteRelative(relativeChildName)

    def addTutor(self,tutor,tutorPosition):
        self.object.screen.surface.blit(tutor.image,tutorPosition.copy())
        if tutor.textList :
            self.object.screen.surface.blit(
                tutor.textList[0],
                [
                    tutor.textPositionList[0][0] + tutorPosition[0],
                    tutor.textPositionList[0][1] + tutorPosition[1]
                ]
            )
        self.updateOriginalSurface()
        self.object.screen.mustUpdateNextFrame()

    def deleteItFromItsRelative(self,objectName):
        pass

    def deleteRelative(self,objectName):
        pass

    def addEvent(self,newEvent):
        self.events[newEvent.name] = newEvent

    def updateEvent(self,newEvent):
        self.events[newEvent.name].update(newEvent)

    def deleteEvent(self,eventName):
        if eventName in self.events :
            del self.events[eventName]
        else :
            self.application.holdForDebug(
                f'Handler.deleteEvent(): {eventName} not found in {self.object.name}.handler.objects'
            )

import ErrorEvent
import fatherFunction, eventFunction, handlerFunction, applicationFunction

print('Handler library imported')

class Handler:

    def update(self):
        pass

    def __init__(self,object):
        self.object = object
        self.inheritanceTree = self.getInheritanceTree()
        self.application = self.object.application
        self.objects = {}
        self.students = {}
        self.events = {}
        self.collidableObjects = {}
        self.collidableObjectsRect = []

        self.updateObjectOriginalAttributes()

        if fatherFunction.isNotAplication(self.object) :
            self.object.father.handler.addObject(self.object)

    def getInheritanceTree(self):
        inheritanceTree = []
        for inheritance in self.object.__class__.mro() :
            inheritanceTree.append(inheritance.__name__)
        return inheritanceTree

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

    def itColided(self,object):
        if object.collides :
            colisionIndexes = object.collidableRect.collidelistall(self.collidableObjectsRect)
            if list(self.collidableObjects.keys()).index(object.name) in colisionIndexes :
                return len(colisionIndexes) > 1
            return len(colisionIndexes) > 0
        return False

    def updateCollidableObjects(self):
        self.collidableObjects = {object.name:object for object in sorted(self.objects.values(),key=handlerFunction.renderOrder) if object.collides}
        self.collidableObjectsRect = [object.collidableRect for object in self.collidableObjects.values()]

    def addObject(self,object):
        self.object.father.screen.reset()
        self.objects[object.name] = object
        self.object.screen.mustUpdateNextFrame()

    def removeObject(self,object):
        if object.name in self.objects :
            object.handler.removeAllEvents()
            object.handler.removeStudentTree()
            object.handler.removeObjectTree()
            # object.tutor.handler.removeStudent(object)
            object.screen.remove()
            del self.objects[object.name]
            self.object.screen.mustUpdateNextFrame()
        else :
            ErrorEvent.ErrorEvent(None,
                message = f'Handler.removeObject():\n' +
                f'      {object.name} not found in {self.object.name}.handler.objects'
            )

    def removeObjectTree(self):
        self.removeStudentTree()
        objectNames = list(self.objects.keys())
        for objectName in objectNames :
            self.removeObject(self.objects[objectName])

    def setTutor(self,tutor):
        self.object.tutor = tutor
        self.object.tutor.handler.addStudent(self.object)
        self.object.blitOrder = self.object.tutor.blitOrder + 1
        try :
            self.object.userInterfaceSurface = self.object.tutor.userInterfaceSurface
        except : pass

    def addTutorImage(self,tutor,tutorPosition):
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

    def addStudent(self,student):
        self.object.father.screen.reset()
        self.students[student.name] = student
        self.object.screen.mustUpdateNextFrame()

    ###- TODO samuel.jansen 2020-02-17 - refactor handlerFunction.parseStudentName()
    def removeStudent(self,student):
        if student.name in self.students :
            if student.name in self.students[student.name].father.handler.objects :
                student.handler.removeAllEvents()
                student.handler.removeStudentTree()
                student.handler.removeObjectTree()
                del self.students[student.name].father.handler.objects[student.name]
                self.object.screen.mustUpdateNextFrame()
        else :
            ErrorEvent.ErrorEvent(None,
                message = f'Handler.removeStudent():\n' +
                f'      {student.name} not found in {self.object.name}.handler.students'
            )

    def removeStudentTree(self):
        studentNames = list(self.students.keys())
        for studentName in studentNames :
            self.removeStudent(self.students[studentName])

    def addEvent(self,event):
        if event.name not in self.events :
            self.events[event.name] = event
        else :
            ErrorEvent.ErrorEvent(None,
                message = f'Handler.addEvent():\n' +
                f'      {event.name} already exists in {self.object.name}.handler.events'
            )

    def removeEvent(self,event):
        if event.name in self.events :
            event.updateStatus(eventFunction.Status.REMOVED)
            del self.events[event.name]
        else :
            ErrorEvent.ErrorEvent(None,
                message = f'Handler.removeEvent():\n' +
                f'      {event.name} not found in {self.object.name}.handler.events'
            )

    def removeAllEvents(self):
        eventNames = list(self.events.keys())
        for eventName in eventNames :
            self.removeEvent(self.events[eventName])

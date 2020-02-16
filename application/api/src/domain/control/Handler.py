import fatherFunction, eventFunction

print('Handler library imported')

class Handler:

    def __init__(self,object):
        self.object = object
        self.application = self.object.application
        self.objects = {}
        self.students = {}
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

    def deleteObject(self,object):
        if object.name in self.objects :
            del self.objects[object.name]
            self.object.screen.mustUpdateNextFrame()
        else :
            self.application.holdForDebug(
                f'Handler.deleteObject():\n' +
                f'      {object.name} not found in {self.object.name}.handler.objects'
            )

    def deleteObjectTree(self,object):
        childrenNames = object.handler.objects.keys()
        for childName in childrenNames:
            if object.handler.objects[childName].handler.students :
                studentSonNames = list(object.handler.objects[childName].handler.students.keys())
                for studentSonName in studentSonNames :
                    object.handler.objects[childName].handler.deleteStudentTree(object.handler.objects[childName].handler.students[studentSonName])
            if object.handler.objects[childName].handler.objects :
                objectSonNames = list(object.handler.objects[childName].handler.objects.keys())
                for objectSonName in objectSonNames :
                    object.handler.objects[childName].handler.deleteObjectTree(object.handler.objects[childName].handler.objects[objectSonName])
        self.deleteObject(self.objects[object.name])

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

    def deleteStudent(self,student):
        if student.name in self.students :
            del self.students[student.name].father.handler.objects[student.name]
            self.object.screen.mustUpdateNextFrame()
        else :
            self.application.holdForDebug(
                f'Handler.deleteStudent():\n' +
                f'      {student.name} not found in {self.object.name}.handler.students'
            )

    def deleteStudentTree(self,student):
        studentNames = student.handler.students.keys()
        for studentName in studentNames:
            if student.handler.students[studentName].handler.students :
                studentSonNames = list(student.handler.students[studentName].handler.students.keys())
                for studentSonName in studentSonNames :
                    student.handler.students[studentName].handler.deleteStudentTree(student.handler.students[studentName].handler.students[studentSonName])
            if student.handler.students[studentName].handler.objects :
                objectSonNames = list(student.handler.students[studentName].handler.objects.keys())
                for objectSonName in objectSonNames :
                    student.handler.students[studentName].handler.deleteObjectTree(student.handler.students[studentName].handler.objects[objectSonName])
        self.deleteStudent(self.students[student.name])

    def addEvent(self,event):
        self.events[event.name] = event

    # def updateEvent(self,event):
    #     self.events[event.name].update(event)

    # def deleteEvent(self,event):
    #     if event.name in self.events :
    #         del self.events[event.name]
    #     else :
    #         self.application.holdForDebug(
    #             f'Handler.deleteEvent():\n' +
    #             f'      {event.name} not found in {self.object.name}.handler.events'
    #         )

    def forceDeleteEvent(self): pass

import applicationFunction

class MemoryOptimizer:

    FAST_NEW_OBJECT_RANGE = 20
    OBJECT_DEPLOY_RATE = 2
    FIRST_MEMORY_PACKAGE = 0
    FIRST_NEW_OBJECT_DTO = 0

    def update(self):
        memoryPackageTree = self.getMemoryPackageTree()
        if memoryPackageTree :
            memoryPackage = memoryPackageTree[MemoryOptimizer.FIRST_MEMORY_PACKAGE]
            self.newObject(memoryPackage)
            if not memoryPackage.newObjectsDto :
                del memoryPackageTree[MemoryOptimizer.FIRST_MEMORY_PACKAGE]

    def __init__(self,application):
        self.application = application
        self.reset()

    def reset(self):
        self.memoryPackageTree = {
            applicationFunction.Priority.NO_PRIORITY : {},
            applicationFunction.Priority.LOW : {},
            applicationFunction.Priority.MEDIUM : {},
            applicationFunction.Priority.HIGHT : {}
        }
        self.application.sessionPage = self.application.name

    def newObject(self,memoryPackage):
        self.fastNewObject(memoryPackage.newObjectsDto[:MemoryOptimizer.OBJECT_DEPLOY_RATE],memoryPackage.objectClass)
        del memoryPackage.newObjectsDto[:MemoryOptimizer.OBJECT_DEPLOY_RATE]

    def fastNewObject(self,newObjectsDto,objectClass):
        while newObjectsDto :
            objectClass(
                *newObjectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO][0],
                **newObjectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO][1]
            )
            del newObjectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO]

    def newObjects(self,newObjectsDto,objectClass,
        priority = applicationFunction.Priority.NO_PRIORITY
    ):
        if len(newObjectsDto) < MemoryOptimizer.FAST_NEW_OBJECT_RANGE :
            self.fastNewObject(newObjectsDto,objectClass)
        else :
            self.application.sessionPage = self.getSessionPage()
            self.updateMemoryPackageTree(priority)
            self.memoryPackageTree[priority][self.application.sessionPage].append(
                MemoryPackage(newObjectsDto,objectClass,
                    priority = priority
                )
            )
            ###- TODO - sort by item priority too

    def getMemoryPackageTree(self):
        for priorityKey in sorted(self.memoryPackageTree.keys(),reverse=True) :
            self.updateMemoryPackageTree(priorityKey)
            if self.memoryPackageTree[priorityKey][self.application.sessionPage] :
                return self.memoryPackageTree[priorityKey][self.application.sessionPage]

    def getSessionPage(self):
        if self.application.session :
            self.updatePresentMemoryPackage()
            return self.application.session.page
        else :
            return self.application.name

    def updatePresentMemoryPackage(self):
        if self.application.session and self.application.sessionPage == self.application.session.page :
            self.deletePresentMemoryPackage()

    def deletePresentMemoryPackage(self):
        del self.getMemoryPackageTree()[0]

    def updateMemoryPackageTree(self,priorityKey):
        if self.application.sessionPage not in self.memoryPackageTree[priorityKey].keys() :
            self.memoryPackageTree[priorityKey][self.application.sessionPage] = []


class MemoryPackage:

    def __init__(self,newObjectsDto,objectClass,
        priority = applicationFunction.Priority.NO_PRIORITY
    ):
        self.objectClass = objectClass
        self.newObjectsDto = newObjectsDto
        self.priority = priority

import applicationFunction

class MemoryOptimizer:

    FAST_NEW_OBJECT_RANGE = 20
    OBJECT_DEPLOY_RATE = 1
    FIRST_MEMORY_PACKAGE = 0
    FIRST_NEW_OBJECT_DTO = 0

    def update(self):
        memoryPackageTree = self.getMemoryPackageTree()
        if memoryPackageTree :
            memoryPackage = memoryPackageTree[MemoryOptimizer.FIRST_MEMORY_PACKAGE]
            self.buildObjects(memoryPackage)
            if not memoryPackage.objectsDto :
                del memoryPackageTree[MemoryOptimizer.FIRST_MEMORY_PACKAGE]

    def __init__(self,application):
        self.application = application
        self.afterBuildObject = None
        self.reset()

    def reset(self):
        self.memoryPackageTree = {
            applicationFunction.Priority.NO_PRIORITY : {},
            applicationFunction.Priority.LOW : {},
            applicationFunction.Priority.MEDIUM : {},
            applicationFunction.Priority.HIGHT : {}
        }
        self.application.sessionPage = self.application.name

    def newObjects(self,objectsDto,objectClass,
        priority = applicationFunction.Priority.NO_PRIORITY,
        afterBuildObject = None
    ):
        self.afterBuildObject = afterBuildObject

        if len(objectsDto) < MemoryOptimizer.FAST_NEW_OBJECT_RANGE :
            self.instantlyBuildObjects(objectsDto,objectClass)
        else :
            self.application.sessionPage = self.getSessionPage()
            self.updateMemoryPackageTree(priority)
            self.memoryPackageTree[priority][self.application.sessionPage].append(
                MemoryPackage(objectsDto,objectClass,
                    priority = priority
                )
            )
            ###- TODO - sort by item priority too

    def buildObjects(self,memoryPackage):
        self.instantlyBuildObjects(memoryPackage.objectsDto[:MemoryOptimizer.OBJECT_DEPLOY_RATE],memoryPackage.objectClass)
        del memoryPackage.objectsDto[:MemoryOptimizer.OBJECT_DEPLOY_RATE]

    def instantlyBuildObjects(self,objectsDto,objectClass):
        # print(f'+++++++++++++++++++++++++++++{self.application.name}.memoryOptimizer.instantlyBuildObjects() method call++++++++++++++++')
        while objectsDto :
            object = objectClass(
            # objectClass(
                *objectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO][0],
                **objectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO][1]
            )
            # print(f'{object.name}.father.name = {object.father.name}, {object.name}.tutor.name = {object.tutor.name}')
            # object.tutor.screen.mustUpdateNextFrame()
            # object.father.screen.mustUpdateNextFrame()
            # object.father.tutor.screen.mustUpdateNextFrame()
            del objectsDto[MemoryOptimizer.FIRST_NEW_OBJECT_DTO]
            if self.afterBuildObject :
                self.afterBuildObject(object)
        # print(f'+++++++++++++++++++++++++++++{self.application.name}.memoryOptimizer.instantlyBuildObjects() method resolve++++++++++++++++')

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
        memoryPackageTree = self.getMemoryPackageTree()
        if memoryPackageTree :
            del memoryPackageTree[0]

    def updateMemoryPackageTree(self,priorityKey):
        if self.application.sessionPage not in self.memoryPackageTree[priorityKey].keys() :
            self.memoryPackageTree[priorityKey][self.application.sessionPage] = []


class MemoryPackage:

    def __init__(self,objectsDto,objectClass,
        priority = applicationFunction.Priority.NO_PRIORITY
    ):
        self.objectClass = objectClass
        self.objectsDto = objectsDto
        self.priority = priority

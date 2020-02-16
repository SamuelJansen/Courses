import os

print('ApplicationHandler library imported')

class ApplicationHandler:

    def __init__(self,pathMannanger):
        self.pathMannanger = pathMannanger
        self.apiModuleName = self.pathMannanger.currentPath.split(f'{self.pathMannanger.apiName}\\')[1].split('\\')[0]
        self.getEventList()
        self.updateEventFunction()

    def getEventList(self):
        self.eventList = []
        eventList = os.listdir(f'{self.pathMannanger.getApiModulePath(self.apiModuleName)}event\\')
        for event in eventList :
            self.eventList.append(event.strip().split('.')[0])

    def updateEventFunction(self):
        for event in self.eventList :
            print(event)

import os
clear = lambda: os.system('cls')

class TimeErrorControl:
    '''
    It calculates unexpected time errors'''
    def __init__(self,frame,aplication) :
        '''
        TimeErrors(frame,aplication)'''
        self.aplication = aplication
        self.frame = frame
        self.now = self.aplication.timeNow
        self.before = self.aplication.timeNow
        self.innerLoops = 0

    def checkTimeError(self,
        mustPrint = False
    ):
        '''
        It checks any time errors each frame.fps frames
        TimeError.checkErrors(aplication,frame)'''
        self.innerLoops += 1

        if self.frame.newSecond :
            self.frame.timeOveralError = 0
            self.before = self.now
            self.now = self.aplication.timeNow
            self.frame.timeOveralError += self.frame.correctionFactor * ( self.now - self.before - 1 - self.frame.timeOveralError )
            if self.frame.timeOveralError < 0 :
                self.frame.timeOveralError = 0

            if mustPrint :
                clear()
                print(f'''      Main loop -- It should be 1: {self.now-self.before}
                aplication.timeNow      = {self.aplication.timeNow}, frame.timeNext = {self.frame.timeNext}
                frame.timeError         = {self.frame.timeError}
                frame.timeOveralError   = {self.frame.timeOveralError}
                frame.apfTimeError      = {self.frame.apfTimeError}
                frame.fpsCounter        = {self.frame.fpsCounter}
                frame.apsCounter        = {self.frame.apsCounter}
                innerLoops              = {self.innerLoops}''')

            self.innerLoops = 0

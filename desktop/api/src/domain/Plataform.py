import Application

print('Plataform library imported')

class Plataform(Application.Application):
    
    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

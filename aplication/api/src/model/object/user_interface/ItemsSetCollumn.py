from model.object.user_interface import Modal

class ItemsSetCollumn(Modal.Modal):
    def __init__(self,name,position,size,father,
        scale = None,
        padding = [0,0],
        noImage = False,
        imagePath = None,
        soundPath = None
    ):

        Modal.Modal.__init__(
            self,
            name,
            position,
            size,
            father,
            scale = scale,
            padding = padding,
            noImage = noImage,
            imagePath = imagePath,
            soundPath = imagePath
        )

        self.previousChildrenPosition = [0,0]

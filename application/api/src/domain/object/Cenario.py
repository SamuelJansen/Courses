import pygame as pg

import Game, Object
import imageFunction

import numpy as np

print('Cenario library imported')

class OneImageCenario(Object.Object):
    def __init__(self,name,velocity,father,
            imagePath = None,
            audioPath = None'
    ):
        cenarioPosition = [0,0]
        Object.Object(
            name,
            cenarioPosition,
            aplication.size,
            aplication.scaleRange,
            velocity,
            father,
            type=Object.ObjectTypes.CENARIO,
            imagePath = imagePath,
            audioPath = audioPath'
        )

class Cenario(Object.Object):
    def __init__(self,name,longitudes,latitudes,initialCoordinate,velocity,father,
            imagePath = None,
            audioPath = None'
    ):
        '''
        longitudes = columns
        latitudes = lines
        initialCoordinate = [longitude,latitude]'''
        self.name = name
        self.longitudes = longitudes
        self.latitudes = latitudes
        self.coordinateSize = [aplication.size[0]//aplication.longitudesImageOnScreen,aplication.size[1]//aplication.latitudesImageOnScreen]
        self.scale = aplication.scaleRange/aplication.latitudesImageOnScreen
        self.coordinatesIndex = self.longitudes * self.latitudes
        ###- the variable below needs some work
        initialPosition = [
            initialCoordinate[0],
            initialCoordinate[1]
        ]
        self.imagePath = aplication.imagePath + self.name + '.png'
        self.size = [
            self.coordinateSize[0]*self.longitudes,
            self.coordinateSize[1]*self.latitudes
        ]
        self.cenarioImage = imageFunction.getImage(self.imagePath,self.size,aplication)
        self.rect = pg.Rect(0,0,self.size[0],self.size[1])
        self.cenarioImageSurface = imageFunction.newImageSurface(self.cenarioImage,self.size)
        self.coordinatesName = []
        for coordinateIndex in range(self.coordinatesIndex) :
            coordinatePosition = [
                initialPosition[0]+int(np.ceil((coordinateIndex%self.longitudes)*self.coordinateSize[0])),
                initialPosition[1]+int(np.ceil((coordinateIndex%self.latitudes)*self.coordinateSize[1]))
            ]
            cenarioSubImage = self.cenarioImageSurface.subsurface((
                coordinatePosition[0], coordinatePosition[1], self.coordinateSize[0], self.coordinateSize[1]))
            cenarioSubImageName = self.name + str(coordinateIndex)
            cenarioSubImagePath = aplication.imagePath + Object.ObjectTypes.getType(Object.ObjectTypes.CENARIO) + '/' + cenarioSubImageName  + '.png'
            imageFunction.saveImage(cenarioSubImage,cenarioSubImagePath)

            ###- the line bellow actually creates these objects
            self.coordinatesName.append(Object.Object(
                cenarioSubImageName,
                coordinatePosition,
                self.coordinateSize,
                self.scale,
                velocity,
                father,
                type=Object.ObjectTypes.CENARIO,
                imagePath = imagePath,
                audioPath = audioPath'
            ).name)

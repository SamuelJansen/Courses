from domain.control import PathMannanger
pathMannanger = PathMannanger.PathMannanger()

import ArrowKey

import Editor
import Course, ApplicationUser

import numpy as np

print('editor api')

editorName = 'editor'
colors =    {
'black' : (0,0,0),
'white' : (255,255,255),
'backgroundColor' : (237,201,202),
'red' : (255,0,0),
'niceBlue' : (0,0,150)
}
fps = 30
aps = 30
editor = Editor.Editor(editorName,fps,aps,colors,pathMannanger,
    position = [960,0],
    floor = True
)

arrow = ArrowKey.ArrowKey()
move = [np.random.randint(3)-1,np.random.randint(3)-1]

editor.run(arrow)

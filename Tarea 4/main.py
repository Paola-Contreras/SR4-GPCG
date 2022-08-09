#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213
#SR3 - OBJ objects 

from gl import Renderer, color, V3, V2
from texture import Texture
import shader as s 

w = 700
h = 600

rend = Renderer(w, h)
rend.active_shader = s.flat
rend.active_texture = Texture("earthDay.bmp")

rend.glLoadModel("Penguin.obj",
                 translate = V3(w/2, h/9, 0),
                 rotate = V3(0, 190, 0),
                 scale = V3(400, 400, 400))

rend.glFinish("output.bmp")


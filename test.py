from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *

inv = Picture._invColor('.', BLACK)

print("El color inverso es " , inv)

#prueba del metodo verticalMirror
draw(Picture.negative(knight))




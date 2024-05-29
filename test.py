from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *

inv = Picture._invColor('.', BLACK)

print("El color inverso es " , inv)

#prueba del metodo verticalMirror

tablero = Picture.join(rock, knight)

draw(tablero.join(bishop, queen))




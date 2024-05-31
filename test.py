from chessPictures import *
from interpreter import draw
from picture import Picture
from colors import *


img = knight
img = Picture.join(img, rock)
img = Picture.join(img, bishop)
img = Picture.join(img, queen)
img = Picture.join(img, king)

img2 = pawn
img2 = Picture.join(img2, pawn)

draw(Picture.up(img, img2))



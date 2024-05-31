from colors import *

class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])

    return vertical


  def horizontalMirror(self):

    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for value in reversed(self.img):
      horizontal.append(value[::1])
    return horizontal


  def negative(self):
    """ Devuelve un negativo de la imagen """
    nuevaImagen = []
    for value in self.img:
      row = []
      for caracter in value:
        row.append(self._invColor(caracter))
      nuevaImagen.append(row)    
    return nuevaImagen


  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento p al lado derecho de la figura actual """
    nuevaImagen = []
    index = 0

    for value in self.img:
      nuevaImagen.append(value + p.img[index])
      index = index + 1

    return Picture(nuevaImagen)
  
  def up(self, p):
    """Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual"""
    nuevaImagen = []
    #copiar todo p a nueva imange
    for value in p.img:
      nuevaImagen.append(value[::1])
    
    for value in self.img:
      nuevaImagen.append(value[::1])
    return Picture(nuevaImagen)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p  la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

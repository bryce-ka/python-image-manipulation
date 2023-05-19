"""
A program that demonstrates various attempts at creating a collages.

Author: Isaac Bynum and Bryce Anthony
"""
#pip install csc121
from csc121.image import get_channel, write_jpg

def gradient_blend():
  """
  smoothly blends the images of bryce and jack 
  """
  bryce_red = get_channel('bryce.jpeg', 'red')
  bryce_green = get_channel('bryce.jpeg', 'green')
  bryce_blue = get_channel('bryce.jpeg', 'blue')

  jack_red = get_channel('jack.jpeg', 'red')
  jack_green = get_channel('jack.jpeg', 'green')
  jack_blue = get_channel('jack.jpeg', 'blue')

  height = len(jack_red)
  width = len(jack_red[0])

  for r in range(height):
    for c in range(width):
      b_r = float(r)/height
      b_c = float(c)/width
      if (b_r > b_c):
        beta = b_r
      else:
        beta = b_c
      bryce_red[r][c] = int((beta * bryce_red[r][c]) + ((1-beta) * jack_red[r][c]))
      bryce_green[r][c] = int((beta * bryce_green[r][c]) + ((1-beta) * (jack_green[r][c])))
      bryce_blue[r][c] = int((beta * bryce_blue[r][c]) + ((1-beta) * jack_blue[r][c]))

  write_jpg(bryce_red, bryce_green, bryce_blue, 'blended.jpeg')
 

def mirror():
  """
  images appear to be mirrored across the y axis
  """
  image = input("Enter name of file: ")
  
  red = get_channel(image, 'red')
  green = get_channel(image, 'green')
  blue = get_channel(image, 'blue')

  height = len(red)
  width = len(red[0])
  fake_width= width-1
  mirror_column = width // 2

  for r in range(height):
    for c in range(mirror_column):
      red[r][fake_width - c ] = red[r][c]
      green[r][fake_width - c ] = green[r][c]
      blue[r][fake_width - c ] = blue[r][c]
    
  write_jpg(red, green, blue, 'mirrored.jpeg')

def pencil_sketch():
  """
  Makes images appear as if they were drawn with pencil.
  """
  image_name = input("Enter name of file: ")

  red = get_channel(image_name, 'red')
  green = get_channel(image_name, 'green')
  blue = get_channel(image_name, 'blue')
  
  height = len(red)
  width = len(red[0])

  for r in range(height-1):
    for c in range(width-1):
      grayscale = (red[r][c] + green[r][c] + blue[r][c]) // 3
      right_grayscale = (red[r][c+1] + green[r][c+1] + blue[r][c+1]) // 3
      below_grayscale = (red[r+1][c] + green[r+1][c] + blue[r+1][c]) // 3
      if (abs(grayscale - right_grayscale) > 8) and (abs(grayscale - below_grayscale) > 8):
        red[r][c] = 0
        green[r][c] = 0
        blue[r][c] = 0
      else:
        red[r][c] = 255
        green[r][c] = 255
        blue[r][c] = 255

  write_jpg(red, green, blue, 'sketched.jpeg')
  
# pencil_sketch()
# mirror()
gradient_blend()

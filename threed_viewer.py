from kandinsky import *
from math import *
from time import *
from random import *
from ion import *

zoom = 250
camx = 157
camy = 117
projection_matrix = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]]

repere = [n for n in range(4)]
repere[0] = [[0], [0], [0]]
repere[1] = [[0.08], [0], [0]]
repere[2] = [[0], [0.08], [0]]
repere[3] = [[0], [0], [0.08]]

cube_points = [n for n in range(8)]
cube_points[0] = [[-0.1], [-0.1], [0.1]]
cube_points[1] = [[0.1], [-0.1], [0.1]]
cube_points[2] = [[0.1], [0.1], [0.1]]
cube_points[3] = [[-0.1], [0.1], [0.1]]
cube_points[4] = [[-0.1], [-0.1], [-0.1]]
cube_points[5] = [[0.1], [-0.1], [-0.1]]
cube_points[6] = [[0.1], [0.1], [-0.1]]
cube_points[7] = [[-0.1], [0.1], [-0.1]]


rotation=False
error=0
def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])
    # Dot product matrix dimensions = a_rows x b_cols
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("INCOMPATIBLE MATRIX SIZES")
    return product



fill_rect(0,0,320,240,(255,255,255))

def rcolordef():
  if rcolor == 1:
    return (255,255,255)
  elif rcolor == 2:
    return (255,0,0)
  elif rcolor == 3:
    return (0,0,255)
  if rcolor == 4:
    return (0,255,0)

draw_string("PRESS OK TO START",75,110)
#Main loop
angle_x = angle_y = angle_z = 0
while True:
    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    
    refresh=False
    if keydown(KEY_SEVEN):
      angle_x += 0.1
      refresh = True
    elif keydown(KEY_OK):
      refresh=True
    elif keydown(KEY_NINE):
      angle_x -= 0.1
      refresh = True
    elif keydown(KEY_SIX):
      angle_y -= 0.1
      refresh = True
    elif keydown(KEY_FOUR):
      angle_y += 0.1
      refresh = True
    elif keydown(KEY_ONE):
      angle_z += 0.1
      refresh = True
    elif keydown(KEY_THREE):
      angle_z -= 0.1
      refresh = True
    elif keydown(KEY_PLUS):
      zoom += 12
      refresh = True
    elif keydown(KEY_MINUS):
      zoom -= 12
      refresh = True
    elif keydown(KEY_LEFT):
      camx -= 12
      refresh = True
    elif keydown(KEY_RIGHT):
      camx += 12
      refresh = True
    elif keydown(KEY_UP):
      camy -= 12
      refresh = True
    elif keydown(KEY_DOWN):
      camy += 12
      refresh = True
    

    else:
      refresh=False
      
    if keydown(KEY_BACKSPACE):
      if rotation == True:
        rotation=False
      else:
        rotation=True
      sleep(0.1)
         
    if rotation == True:
      angle_x += 0.08
      angle_y += 0.08
      angle_z += 0.08
      refresh=True
    if refresh == True:
      fill_rect(0,0,320,240,(80,80,80))
      rcolor = 1
      for point in repere:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)

        x = int((point_2d[0][0] * zoom))
        y = int((point_2d[1][0] * zoom))
        
        fill_rect(x+camx+1,y+camy,3,5,rcolordef())
        fill_rect(x+camx,y+camy+1,5,3,rcolordef())
        rcolor+=1
      for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)

        x = int((point_2d[0][0] * zoom))
        y = int((point_2d[1][0] * zoom))
        
        fill_rect(x+camx+1,y+camy,3,5,(255,0,255))
        fill_rect(x+camx,y+camy+1,5,3,(255,0,255))
    elif refresh == False:
      pass
#      error=error+1
#      print("erreur num:"+str(error))
    sleep(0.02)
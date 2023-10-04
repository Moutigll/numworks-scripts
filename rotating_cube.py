from kandinsky import *
from math import *
from time import *
projection_matrix = [[1, 0, 0],[0, 1, 0],[0, 0, 0]]
cube_points = [n for n in range(8)]
cube_points[0] = [[-1], [-1], [1]]
cube_points[1] = [[1], [-1], [1]]
cube_points[2] = [[1], [1], [1]]
cube_points[3] = [[-1], [1], [1]]
cube_points[4] = [[-1], [-1], [-1]]
cube_points[5] = [[1], [-1], [-1]]
cube_points[6] = [[1], [1], [-1]]
cube_points[7] = [[-1], [1], [-1]]
def multiply_m(a, b):
  a_rows = len(a)
  a_cols = len(a[0])
  b_rows = len(b)
  b_cols = len(b[0])
  product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
  if a_cols == b_rows:
    for i in range(a_rows):
      for j in range(b_cols):
        for k in range(b_rows):
          product[i][j] += a[i][k] * b[k][j]
  return product
angle_x = angle_y = angle_z = 0
while True:
  rotation_x = [[1, 0, 0],[0, cos(angle_x), -sin(angle_x)],[0, sin(angle_x), cos(angle_x)]]
  rotation_y = [[cos(angle_y), 0, sin(angle_y)],[0, 1, 0],[-sin(angle_y), 0, cos(angle_y)]]
  rotation_z = [[cos(angle_z), -sin(angle_z), 0],[sin(angle_z), cos(angle_z), 0],[0, 0, 1]]
  angle_x += 0.1
  angle_y += 0.1
  angle_z += 0.1
  fill_rect(0,0,500,500,(0,0,0))    
  for point in cube_points:
    rotate_x = multiply_m(rotation_x, point)
    rotate_y = multiply_m(rotation_y, rotate_x)
    rotate_z = multiply_m(rotation_z, rotate_y)
    point_2d = multiply_m(projection_matrix, rotate_z)
    x = int((point_2d[0][0] * 50)+120)
    y = int((point_2d[1][0] * 50)+120)
    fill_rect(x,y,4,4,(255,0,255))
  sleep(0.03)
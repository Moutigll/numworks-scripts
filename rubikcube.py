from kandinsky import *
from time import *
from ion import *
c=0
cube=[]
facing=[0,3,1,2,4,5]
col=[(255,0,0),(0,0,255),(255,150,0),(0,255,100),(255,255,0),(255,)*3]
fill_rect(131,58,155,155,(50,)*3)
fill_rect(50,93,30,120,(50,)*3)
fill_rect(20,153,90,30,(50,)*3)
def draw_face(f):
  x,y=136,63
  c=0
  for i in range(3):
    for i in range(3):
      fill_rect(x,y,45,45,col[f[c]])
      c+=1
      x+=50
    x=136
    y+=50
for i in range(6):
  a=[c,]*9
  cube.append(a)
  c+=1
col=[(255,0,0),(0,0,255),(255,150,0),(0,255,0),(255,255,0),(255,)*3]
while True:
  if keydown(KEY_LEFT):
    facing[0],facing[1],facing[2],facing[3]=facing[2],facing[0],facing[3],facing[1]
    sleep(0.2)
  if keydown(KEY_RIGHT):
    facing[0],facing[1],facing[2],facing[3]=facing[1],facing[3],facing[0],facing[2]
    sleep(0.2)
  if keydown(KEY_UP):
    facing[0],facing[4],facing[3],facing[5]=facing[5],facing[0],facing[4],facing[3]
    sleep(0.2)
  if keydown(KEY_DOWN):
    facing[0],facing[4],facing[3],facing[5]=facing[4],facing[3],facing[5],facing[0]
    sleep(0.1)
  draw_face(cube[facing[0]])
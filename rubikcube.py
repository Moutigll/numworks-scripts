from kandinsky import *
from time import *
from ion import *
c=0
cube=[]
facing=[0,3,1,2,4,5]
col=[(255,0,0),(0,0,255),(255,150,0),(0,255,100),(255,255,0),(255,)*3]
fill_rect(131,58,155,155,(50,)*3)
fill_rect(49,182,31,31,(50,)*3)
fill_rect(49,148,31,31,(50,)*3)
fill_rect(15,148,31,31,(50,)*3)
fill_rect(83,148,31,31,(50,)*3)
fill_rect(49,114,31,31,(50,)*3)
fill_rect(49,80,31,31,(50,)*3)
patron_co=[50,149,16,149,50,81,84,149,50,115,50,183]
def draw_cursor(x,y,o):
  if o:
    fill_rect(x,y,45,8,(0,150,255))
    fill_rect(x+8,y+8,29,8,(0,150,255))
    fill_rect(x+16,y+16,13,8,(0,150,255))
  else:
    fill_rect(x,y,8,45,(0,150,255))
    fill_rect(x-8,y+8,8,29,(0,150,255))
    fill_rect(x-16,y+16,8,13,(0,150,255))
draw_cursor(10,10,True)
draw_cursor(120,10,False)
def patron_face(f,c):
  x,y=patron_co[f*2],patron_co[(f*2)+1]
  fill_rect(x-4,y-4,36,3,c)
  fill_rect(x-4,y-1,3,31,c)
  fill_rect(x-4,y+30,37,3,c)
  fill_rect(x+30,y-4,3,35,c)
def draw_patron_faces():
  c=0
  for i in range(6):
    x,y=patron_co[c*2],patron_co[(c*2)+1]
    a=0
    for i in range(3):
      for i in range(3):
        fill_rect(x,y,9,9,col[cube[c][a]])
        a+=1
        x+=10
      x=patron_co[c*2]
      y+=10
    c+=1     
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
patron_face(facing[0],(0,150,255))
draw_face(cube[facing[0]])
draw_patron_faces()
while True:
  if keydown(KEY_LEFT):
    patron_face(facing[0],(255,)*3)
    facing[0],facing[1],facing[2],facing[3]=facing[2],facing[0],facing[3],facing[1]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    sleep(0.2)
  if keydown(KEY_RIGHT):
    patron_face(facing[0],(255,)*3)
    facing[0],facing[1],facing[2],facing[3]=facing[1],facing[3],facing[0],facing[2]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    sleep(0.2)
  if keydown(KEY_UP):
    patron_face(facing[0],(255,)*3)
    facing[0],facing[4],facing[3],facing[5]=facing[5],facing[0],facing[4],facing[3]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    sleep(0.2)
  if keydown(KEY_DOWN):
    patron_face(facing[0],(255,)*3)
    facing[0],facing[4],facing[3],facing[5]=facing[4],facing[3],facing[5],facing[0]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    sleep(0.1)
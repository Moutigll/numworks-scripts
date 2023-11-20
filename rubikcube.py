from kandinsky import *
from time import *
from ion import *
from os import *
from random import *
c=0
dl=0.15
cursor=[132,30,True,185,30,True,238,30,True,307,61,False,307,114,False,307,167,False,0]
cube=[]
facing=[0,3,1,2,4,5]
col=[(255,0,0),(0,0,255),(255,150,0),(0,255,100),(255,255,0),(255,)*3]
fill_rect(131,58,155,155,(50,)*3);fill_rect(49,182,31,31,(50,)*3);fill_rect(49,148,31,31,(50,)*3);fill_rect(15,148,31,31,(50,)*3);fill_rect(83,148,31,31,(50,)*3);fill_rect(49,114,31,31,(50,)*3);fill_rect(49,80,31,31,(50,)*3)
patron_co=[50,149,16,149,50,81,84,149,50,115,50,183]
reading=False
seedc=0
seed=[]
def scramble():
  global seed, seedc, reading, dl
  seedc=0
  dl=0
  reading=True
  seed=[]
  for i in range(100):
    seed.append(randint(0,15))
def compress_cube(c):
  a=0
  b=0
  d=""
  for i in range(6):
    for i in range(9):
      d+=str(c[a][b])
      b+=1
    b=0
    a+=1
  return d
def decompress_cube(b):
  c=[]
  d=[]
  e=0
  for i in range(6):
    for i in range(9):
      d.append(int(b[e]))
      e+=1
    c.append(d)
    d=[]
  return c
def rotate_face(f,d):
  if d:
    f[0],f[1],f[2],f[3],f[5],f[6],f[7],f[8]=f[2],f[5],f[8],f[1],f[7],f[0],f[3],f[6]
  else:
    f[0],f[1],f[2],f[3],f[5],f[6],f[7],f[8]=f[6],f[3],f[0],f[7],f[1],f[8],f[5],f[2]
  return f
def draw_cursor(x,y,o,c):
  if o:
    fill_rect(x,y,45,8,c)
    fill_rect(x+8,y+8,29,8,c)
    fill_rect(x+16,y+16,13,8,c)
  else:
    fill_rect(x,y,8,45,c)
    fill_rect(x-8,y+8,8,29,c)
    fill_rect(x-16,y+16,8,13,c)
draw_cursor(cursor[0],cursor[1],cursor[2],(0,150,255))
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
cube=[[1,4,1,2,5,0,3,4,3],[0,2,0,1,3,1,2,0,2],[1,5,1,0,4,2,3,5,3],[0,2,0,3,1,3,2,0,2],[5,3,4,4,2,5,5,1,4],[4,3,5,5,0,4,4,1,5]]
col=[(255,0,0),(0,0,255),(255,150,0),(0,255,0),(255,255,0),(255,)*3]
patron_face(facing[0],(0,150,255))
draw_face(cube[facing[0]])
draw_patron_faces()
while True:
  t=monotonic()
  if keydown(KEY_OK):
    scramble()
  if keydown(KEY_LEFT) or (reading and seed[seedc] == 0):
    patron_face(facing[0],(255,)*3)
    rotate_face(cube[facing[1]],True);rotate_face(cube[facing[1]],True);rotate_face(cube[facing[3]],True);rotate_face(cube[facing[3]],True)
    rotate_face(cube[facing[4]],True)
    rotate_face(cube[facing[5]],False)
    facing[0],facing[1],facing[2],facing[3]=facing[2],facing[0],facing[3],facing[1]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    draw_patron_faces()
    sleep(dl)
  if keydown(KEY_RIGHT) or (reading and seed[seedc] == 1):
    patron_face(facing[0],(255,)*3)
    rotate_face(cube[facing[2]],True);rotate_face(cube[facing[2]],True);rotate_face(cube[facing[3]],True);rotate_face(cube[facing[3]],True)
    rotate_face(cube[facing[4]],False)
    rotate_face(cube[facing[5]],True)
    facing[0],facing[1],facing[2],facing[3]=facing[1],facing[3],facing[0],facing[2]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    draw_patron_faces()
    sleep(dl)
  if keydown(KEY_DOWN) or (reading and seed[seedc] == 2):
    patron_face(facing[0],(255,)*3)
    rotate_face(cube[facing[2]],True)
    rotate_face(cube[facing[1]],False)
    facing[3],facing[4],facing[0],facing[5]=facing[4],facing[0],facing[5],facing[3]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    draw_patron_faces()
    sleep(dl)
  if keydown(KEY_UP) or (reading and seed[seedc] == 3):
    patron_face(facing[0],(255,)*3)
    rotate_face(cube[facing[2]],False)
    rotate_face(cube[facing[1]],True)
    facing[3],facing[4],facing[0],facing[5]=facing[5],facing[3],facing[4],facing[0]
    patron_face(facing[0],(0,150,255))
    draw_face(cube[facing[0]])
    draw_patron_faces()
    sleep(dl)
  if keydown(KEY_SHIFT) and cursor[18] > 0:
    draw_cursor(cursor[cursor[18]*3],cursor[(cursor[18]*3)+1],cursor[(cursor[18]*3)+2],(255,)*3);cursor[18]-=1;draw_cursor(cursor[cursor[18]*3],cursor[(cursor[18]*3)+1],cursor[(cursor[18]*3)+2],(0,150,255));sleep(0.2)
  if keydown(KEY_ALPHA) and cursor[18] < 5:
    draw_cursor(cursor[cursor[18]*3],cursor[(cursor[18]*3)+1],cursor[(cursor[18]*3)+2],(255,)*3);cursor[18]+=1;draw_cursor(cursor[cursor[18]*3],cursor[(cursor[18]*3)+1],cursor[(cursor[18]*3)+2],(0,150,255));sleep(0.2)
  if (keydown(18) or keydown(19)) or reading:
    z=[
      0,[2,False],[0,4,3,5,[0,3,6],[0,3,6],[0,3,6],[0,3,6]],
      1,0,[0,4,3,5,[1,4,7],[1,4,7],[1,4,7],[1,4,7]],
      2,[1,True],[0,4,3,5,[2,5,8],[2,5,8],[2,5,8],[2,5,8]],
      3,[4,False],[0,1,3,2,[0,1,2],[0,1,2],[8,7,6],[0,1,2]],
      4,0,[0,1,3,2,[3,4,5],[3,4,5],[5,4,3],[3,4,5]],
      5,[5,True],[0,1,3,2,[6,7,8],[6,7,8],[2,1,0],[6,7,8]],
      0,[2,True],[0,5,3,4,[0,3,6],[0,3,6],[0,3,6],[0,3,6]],
      1,0,[0,5,3,4,[1,4,7],[1,4,7],[1,4,7],[1,4,7]],
      2,[1,False],[0,5,3,4,[2,5,8],[2,5,8],[2,5,8],[2,5,8]],
      3,[4,True],[0,2,3,1,[0,1,2],[0,1,2],[8,7,6],[0,1,2]],
      4,0,[0,2,3,1,[3,4,5],[3,4,5],[5,4,3],[3,4,5]],
      5,[5,False],[0,2,3,1,[6,7,8],[6,7,8],[2,1,0],[6,7,8]]]
    k=18
    c=0
    for i in range(2):
      for i in range(6):
        if (keydown(k) and cursor[18] == z[c]) or (reading and seed[seedc] == a):
          if z[c+1] != 0:
            rotate_face(cube[facing[z[c+1][0]]],z[c+1][1])
          cube[facing[z[c+2][0]]][z[c+2][4][0]],cube[facing[z[c+2][0]]][z[c+2][4][1]],cube[facing[z[c+2][0]]][z[c+2][4][2]],cube[facing[z[c+2][1]]][z[c+2][5][0]],cube[facing[z[c+2][1]]][z[c+2][5][1]],cube[facing[z[c+2][1]]][z[c+2][5][2]],cube[facing[z[c+2][2]]][z[c+2][6][0]],cube[facing[z[c+2][2]]][z[c+2][6][1]],cube[facing[z[c+2][2]]][z[c+2][6][2]],cube[facing[z[c+2][3]]][z[c+2][7][0]],cube[facing[z[c+2][3]]][z[c+2][7][1]],cube[facing[z[c+2][3]]][z[c+2][7][2]]=cube[facing[z[c+2][1]]][z[c+2][5][0]],cube[facing[z[c+2][1]]][z[c+2][5][1]],cube[facing[z[c+2][1]]][z[c+2][5][2]],cube[facing[z[c+2][2]]][z[c+2][6][0]],cube[facing[z[c+2][2]]][z[c+2][6][1]],cube[facing[z[c+2][2]]][z[c+2][6][2]],cube[facing[z[c+2][3]]][z[c+2][7][0]],cube[facing[z[c+2][3]]][z[c+2][7][1]],cube[facing[z[c+2][3]]][z[c+2][7][2]],cube[facing[z[c+2][0]]][z[c+2][4][0]],cube[facing[z[c+2][0]]][z[c+2][4][1]],cube[facing[z[c+2][0]]][z[c+2][4][2]]
        c+=3
      k=19
    draw_patron_faces()
    draw_face(cube[facing[0]])
    sleep(dl)
  if keydown(22):
    a=open("cube.py","w")
    a.write(compress_cube(cube))
    a.close()
    draw_string("cube saved !",0,20)
  if keydown(23):
    try:
      a=open("cube.py","r")
      cube=decompress_cube(list(a.readline()))
      a.close()
      draw_patron_faces()
      draw_face(cube[facing[0]])
      draw_string("cube loaded !",0,20)
    except:
      pass
  if seedc+1 == len(seed):
    reading=False
    seedc=0
    dl=0.1
  else:
    seedc+=1
  draw_string(str(1/(monotonic()-t)),0,0)
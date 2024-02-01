from kandinsky import *
from ion import *
from ressources import *
from time import *
from random import *
fill_rect(0,0,320,222,(35,)*3)
fill_rect(96,47,128,128,(0,0,20))
palet=[(255,0,77),(255,204,170),(29,43,83),(0,135,81),(255,241,232),(41,173,255),(95,87,79)]
wa=[[0,1,3,4],[0,2,3,5]]
wac=rft=dir=0
player=[10,99,[0,0,8,6],[7,0,-1,6],False]
run=True
def draw_obj(b,x,y,s,r):
  x1,y1,x2,y2=b[0],b[1],b[2],b[3]
  a=b=1
  l,h=x2-x1,y2-y1
  if s == 1:
    x1,x2=x2-1,x1-1
  elif s == 2:
    y1,y2=y2-1,y1-1
  elif s == 3:
    x1,x2,y1,y2=x2-1,x1-1,y2-1,y1-1
  if x1 > x2:
    a=-1
    l=x1-x2
  if y1 > y2:
    b=-1
    h=y1-y2
  for i in range(h):
    for j in range(l):
      if r == 0:
        if sprite[y1+(b*i)][x1+(a*j)] != 0:
          set_pixel(96+j+x,47+i+y,palet[(sprite[y1+(b*i)][x1+(a*j)]-1)])
      else:
        if sprite[y1+(b*j)][x1+(a*i)] != 0:
          set_pixel(96+j+x,47+i+y,palet[(sprite[y1+(b*j)][x1+(a*i)]-1)])

def walkf(b):
  global wac, player, wa
  if wac == 4:
      wac=0
  a=0
  if wac == 2:
    a=-1
  ref_pl()
  draw_obj(player[b+2],player[0]-2,player[1]+a-2,0,0)
  draw_obj(walk[wa[b][wac]],player[0]-1,player[1]+3+a,0,0)
  wac+=1
  player[4]=True

def ntl(l,j):
  a=[int(x) for x in str(l[j])]
  if len(a) == 1:
    a.append(0)
    a.append(0)
  elif len(a) == 2:
    a[0]=int(str(a[0])+str(a[1]))
    a.remove(a[1])
    a.append(0)
    a.append(0)
  elif len(a) > 3:
    a[0]=int(str(a[0])+str(a[1]))
    a.remove(a[1])
  return a

def ref_pl():
  global rft,player
  fill_rect(player[0]+93,player[1]+44,10,8,(0,0,20))
  if rft == 1:
    a=ntl(lvl[0][player[1]//8],(player[0]//8)+1)
    draw_obj(tiles[a[0]-1],((player[0]//8)+1)*8,(player[1]//8)*8,a[1],a[2])
  if rft == 2:
    a=ntl(lvl[0][player[1]//8],(player[0]//8)-1)
    print(a)
    draw_obj(tiles[a[0]-1],((player[0]//8)-1)*8,(player[1]//8)*8,a[1],a[2])
  rft=0
draw_obj([0,0,8,6],player[0]-2,player[1]-2,0,0)
draw_obj(walk[wa[0][0]],player[0]-1,player[1]+3,0,0)
t=monotonic()
for i in range(16):
  l=lvl[0][i]
  for j in range(16):
    a=ntl(l,j)
    if a[0] != 0:
      draw_obj(tiles[a[0]-1],j*8,i*8,a[1],a[2])
print(monotonic()-t)
while run:
  if keydown(KEY_DOWN):
    ref_pl()
    draw_obj(updown[0+dir],player[0]-2,player[1]-2,0,0)
    player[4]=True
  elif keydown (KEY_UP):
    ref_pl()
    draw_obj(updown[2+dir],player[0]-2,player[1]-2,0,0)
    player[4]=True
  if player[0]%8 >= 2 and lvl[0][player[1]//8][(player[0]//8)+1] != 0:
    rft=1
  elif player[0]%8 <= 2 and lvl[0][player[1]//8][(player[0]//8)-1] != 0:
    rft=2
  if keydown(KEY_RIGHT):
    if player[0] < 119 and not (player[0]%8 > 2 and lvl[0][player[1]//8][(player[0]//8)+1] != 0):
      player[0]+=1
    dir=0
    if not keydown(KEY_DOWN) and not keydown(KEY_UP):
      walkf(0)
  elif keydown(KEY_LEFT):
    if player[0] > 0 and not (player[0]%8 < 2 and lvl[0][player[1]//8][(player[0]//8)-1] != 0):
      player[0]-=1
    dir=1
    if not keydown(KEY_DOWN) and not keydown(KEY_UP):
      walkf(1)
  elif player[4] and not keydown(KEY_DOWN)and not keydown(KEY_UP) and not keydown(KEY_LEFT) and not keydown(KEY_RIGHT):
    player[4]=False
    ref_pl()
    draw_obj(player[dir+2],player[0]-2,player[1]-2,0,0)
    draw_obj(walk[wa[0][0]],player[0]-1,player[1]+3,0,0)
  if keydown(KEY_BACK):
    pass
  if keydown(KEY_ZERO):
    run=False
from kandinsky import *
from ion import *
from ressources import *
from time import *
fill_rect(0,0,320,222,(0,)*3)
fill_rect(96,47,128,128,(0,0,125))
palet=[(255,0,77),(255,204,170),(29,43,83),(0,135,81),(255,)*3]
wa=[[0,1,3,4],[0,2,3,5]]
wac=0
dir=0
player=[30,30,[0,0,8,6],[7,0,-1,6],False]
def draw_obj(b,x,y):
  x1,y1,x2,y2=b[0],b[1],b[2],b[3]
  a=b=1
  l,h=x2-x1,y2-y1
  if x1 > x2:
    a=-1
    l=x1-x2
  if y1 > y2:
    b=-1
    h=y1-y2
  for i in range(h):
    for j in range(l):
      if sprite[y1+(b*i)][x1+(a*j)] != 0:
        set_pixel(96+j+x,47+i+y,palet[(sprite[y1+(b*i)][x1+(a*j)]-1)])

def walkf(b):
  global wac, player, wa
  if wac == 4:
      wac=0
  a=0
  if wac == 2:
    a=-1
  fill_rect(player[0]+95,player[1]+46,10,10,(0,0,125))
  draw_obj(player[b+2],player[0],player[1]+a)
  draw_obj(walk[wa[b][wac]],player[0]+1,player[1]+5+a)
  wac+=1
  player[4]=True
  sleep(0.1)

draw_obj([0,0,8,6],player[0],player[1])
draw_obj(walk[wa[0][0]],player[0]+1,player[1]+5)

while True:
  if keydown(KEY_DOWN):
    fill_rect(player[0]+95,player[1]+46,10,10,(0,0,125))
    draw_obj(updown[0+dir],player[0],player[1])
    player[4]=True
    sleep(0.1)
  elif keydown (KEY_UP):
    fill_rect(player[0]+95,player[1]+46,10,10,(0,0,125))
    draw_obj(updown[2+dir],player[0],player[1])
    player[4]=True
    sleep(0.1)
  if keydown(KEY_RIGHT):
    if not keydown(KEY_DOWN) and not keydown(KEY_UP):
      walkf(0)
    dir=0
  elif keydown(KEY_LEFT):
    if not keydown(KEY_DOWN) and not keydown(KEY_UP):
      walkf(1)
    dir=1
  elif player[4] and not keydown(KEY_DOWN) and not keydown(KEY_UP):
    player[4]=False
    fill_rect(player[0]+95,player[1]+46,10,10,(0,0,125))
    draw_obj(player[dir+2],player[0],player[1])
    draw_obj(walk[wa[0][0]],player[0]+1,player[1]+5)
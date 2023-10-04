from kandinsky import *
from ion import *
from time import *
turn=1
jet_x=153
jet_y=18
set_pixel(0,0,(255,210,0))
jne=get_pixel(0,0)
cp=[[-20,0,-40,0,-60,0],[-40,0,-20,0,20,0],[-20,0,20,0,40,0],[20,0,40,0,60,0],[20,20,40,40,60,60],[-20,-20,20,20,40,40],[-40,-40,-20,-20,20,20],[-60,-60,-40,-40,-20,-20],[20,-20,40,-40,60,-60],[-20,20,20,-20,40,-40],[-40,40,-20,20,20,-20],[-60,60,-40,40,-20,20],[0,20,0,40,0,60]]
fjetx=153
fjety=173
colorjf=(255,100,100)
colorj=(255,0,0)
colorjf=(255,100,100)
w=False
trnc=False
b=(255,255,255)
def circle(x,y,color):
  fill_rect(x+4,y,4,12,color)
  fill_rect(x+3,y+1,6,10,color)
  fill_rect(x+2,y+2,8,8,color)
  fill_rect(x+1,y+3,10,6,color)
  fill_rect(x,y+4,12,4,color)
def start(c):
  turn=1
  jet_y=18
  fill_rect(25,25,270,172,(0,0,255))
  fill_rect(25,197,270,10,(0,0,0))
  draw_x=33
  draw_y=33
  for i in range(8):
    for i in range(13):
      circle(draw_x,draw_y,c)
      draw_x+=20
    draw_y+=20
    draw_x=33
start(b)
circle(153,173,colorjf)
def chek(cx,cy):
  rc=0
  for i in range(len(cp)):
    if get_pixel(cx+cp[rc][0],cy+cp[rc][1]) == colorj and get_pixel(cx+cp[rc][2],cy+cp[rc][3]) == colorj and get_pixel(cx+cp[rc][4],cy+cp[rc][5]) == colorj:
      if turn == 1:
        plyr="red"
        ca=(255,0,0)
      else:
        plyr="yellow"
        ca=(255,210,0)
      draw_string("GG, player "+plyr+" win !",50,2);sleep(3.75)
      while not keydown(KEY_OK):
        fill_rect(0,207,320,25,b)
        fill_rect(0,25,25,182,b)
        fill_rect(295,25,25,182,b)
        start(ca)
        sleep(0.4)
        draw_string("Press ok to rematch !",45,207)
        fill_rect(0,25,25,182,ca)
        fill_rect(295,25,25,182,ca)
        start(b)
        sleep(0.4)
      fill_rect(0,0,320,240,b)
      start(b)
      sleep(0.35)
      return True
    rc+=1
while True:
  circle(jet_x,5,colorj)
  if keydown(KEY_LEFT) and jet_x > 33:
    circle(jet_x,5,b)
    circle(fjetx,fjety,b)
    jet_x-=20
    circle(jet_x,5,(colorj))
    while get_pixel(jet_x+10,jet_y+20) == b:
      jet_y+=20
    circle(jet_x,jet_y-5,colorjf)
    fjetx=jet_x
    fjety=jet_y-5
    jet_y=18
    sleep(0.1)
  elif keydown(KEY_RIGHT) and jet_x < 270:
    circle(jet_x,5,b)
    circle(fjetx,fjety,b)
    jet_x+=20
    circle(jet_x,5,colorj)
    while get_pixel(jet_x+10,jet_y+20) == (255,255,255):
      jet_y+=20
    circle(jet_x,jet_y-5,colorjf)
    fjetx=jet_x
    fjety=jet_y-5
    jet_y=18
    sleep(0.1)
  if keydown(KEY_OK) or keydown(KEY_EXE):
    while get_pixel(jet_x+10,jet_y+20) == b:
      circle(jet_x,jet_y-5,b)
      circle(jet_x,5,colorj)
      fill_rect(jet_x+6,25,3,3,(0,0,255))
      jet_y+=20
      circle(jet_x,jet_y-5,colorj)
      sleep(0.07)
      trnc=True
    circle(jet_x,jet_y-5,b)
    circle(jet_x,5,colorj)
    fill_rect(jet_x+6,25,3,3,(0,0,255))
    jet_y+=20
    circle(jet_x,jet_y-5,colorj)
    sleep(0.07)
    w=chek(jet_x+7,jet_y+2)
    jet_y=18
    if turn == 1 and trnc == True:
      turn=2
    elif turn == 2 and trnc == True:
      turn=1
    else:
      fjetx=fjety=0
    if turn == 1:
      colorj=(255,0,0)
      colorjf=(255,100,100)
    else:
      colorj=jne
      colorjf=(235,235,160)
    while get_pixel(jet_x+10,jet_y+20) == b:
      jet_y+=20
    if trnc == True:
      circle(jet_x,jet_y-5,colorjf)
      fjetx=jet_x
      fjety=jet_y-5
      jet_y=18
      sleep(0.1)
      trnc=False
    if w == False:
      jet_x=153
      w=False
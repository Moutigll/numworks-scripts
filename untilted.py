from kandinsky import *
from time import *
from ion import *
def start():
  global plyra,plyrb,bg,frames,inputs,bl,bgc,intrf,intrfc,health
  plyra=[50,101,(0,0,255),33,134]
  plyrb=[250,101,(255,0,0),166,267]
  health=[6,6]
  bg=(255,255,255)
  intrf=(255,0,255)
  frames=0
  inputs=["4",1,-3,"0",1,3,"1",0,-3,"2",0,3,"/",1,-3,"EXE",1,3,"+",0,-3,"-",0,3]
  bl=[False,0,False,0,0,False,0,0,False,0,0,False,0,False,0,0,False,0,0,False,0,0]
  fill_rect(0,0,320,222,bg)
  bgc=get_pixel(1,1)
  draw_plyr(plyrb[0],plyrb[1],plyrb[2])
  draw_plyr(plyra[0],plyra[1],plyra[2])
  fill_rect(157,0,6,222,intrf)
  intrfc=get_pixel(158,1)
  fill_rect(29,0,1,222,intrf)
  fill_rect(290,0,1,222,intrf)
  draw_bla(14,17,True)
  draw_bla(306,199,False)
  fill_rect(4,3,7,32,intrf)
  fill_rect(310,187,7,32,intrf)
  draw_health(True,health[0])
  draw_health(False,health[1])
def draw_plyr(x,y,c):
  fill_rect(x,y,20,20,c)
def draw_bla(x,y,d):
  if d:
    fill_rect(x,y,11,5,(0,0,0))
    fill_rect(x+11,y+1,1,3,(0,0,0))
    fill_rect(x+12,y+2,1,1,(0,0,0))
  else:
    fill_rect(x-11,y,11,5,(0,0,0))
    fill_rect(x-12,y+1,1,3,(0,0,0))
    fill_rect(x-13,y+2,1,1,(0,0,0))
def draw_health(p,n):
  if not p:
    x,y,d=10,130,15
  else:
    x,y,d=301,82,-15
  fill_rect(x,y,10,d*10,bg)
  for i in range(n):
    fill_rect(x,y,10,10,(250,100,100))
    y+=d
start()
while True:
  lag=0.01
  fps=monotonic()
  if not bl[0]:
    if bl[1]+30 > frames:
      fill_rect(5,round(frames-bl[1])+4,5,1,(0,255,0))
    else:
      bl[0]=True
  if not bl[11]:
    if bl[12]+30 > frames:
      fill_rect(311,round(frames-bl[12])+188,5,1,(0,255,0))
    else:
      bl[11]=True
  if keydown(KEY_SINE) and bl[0]:
    bl[0]=False
    bl[1]=frames
    fill_rect(4,3,7,32,intrf)
    fill_rect(5,4,5,1,(0,255,0))
    if not bl[2]:
      bl[2]=True
      bl[3]=plyra[0]+25
      bl[4]=plyra[1]+8
    elif not bl[5]:
      bl[5]=True
      bl[6]=plyra[0]+25
      bl[7]=plyra[1]+8
    elif not bl[8]:
      bl[8]=True
      bl[9]=plyra[0]+25
      bl[10]=plyra[1]+8
  if keydown(KEY_SQUARE) and bl[11]:
    bl[11]=False
    bl[12]=frames
    fill_rect(310,187,7,32,intrf)
    fill_rect(311,188,5,1,(0,255,0))
    if not bl[13]:
      bl[13]=True
      bl[14]=plyrb[0]-5
      bl[15]=plyrb[1]+8
    elif not bl[16]:
      bl[16]=True
      bl[17]=plyrb[0]-5
      bl[18]=plyrb[1]+8
    elif not bl[19]:
      bl[19]=True
      bl[20]=plyrb[0]-5
      bl[21]=plyrb[1]+8
  c=2
  a=[3,True,13,0,"a"]
  for i in range(2):
    for i in range(3):
      if bl[c]:
        lag-=0.0005
        fill_rect(bl[c+1],bl[c+2],-a[0],5,bg)
        bl[c+1]+=a[0]
        draw_bla(bl[c+1],bl[c+2],a[1])
        col=get_pixel(bl[c+1]+a[2],bl[c+2]+2)
        if bl[c+1] > 274 or bl[c+1] < 45:
          bl[c]=False
          fill_rect(bl[c+1],bl[c+2],-a[0],5,bg)
          fill_rect(bl[c+1],bl[c+2],a[2],5,bg)
        elif col != bgc and col != intrfc and col != (0,0,0):
          health[a[3]]-=1
          draw_health(a[1],health[a[3]])
          fill_rect(bl[c+1]+a[3],bl[c+2],a[2],5,bg)
          fill_rect(bl[c+1],bl[c+2],-a[0],5,bg)
          bl[c]=False
          if health[a[3]] == 0:
            fill_rect(0,0,320,222,bg)
            draw_string("END Player "+a[4]+" win !",50,110)
            while not keydown(KEY_OK):
              pass
            start()
      c+=3
    c=13
    a=[-3,False,-14,1,"b"]
  keys=list(get_keys())
  b=0
  for i in range(len(keys)):
    c=0
    d=True
    co=plyra
    for i in range(2):
      for i in range(4):
        if str(keys[b]) == inputs[c] and (co[0] >= co[3] or inputs[c+2] == 1 or inputs[c+1] == 1) and (co[0] <= co[4] or inputs[c+2] == -1 or inputs[c+1] == 1) and (co[1] >= 0 or inputs[c+2] == 1 or inputs[c+1] == 0) and (co[1] <= 202 or inputs[c+2] == -1 or inputs[c+1] == 0):
          lag-=0.001
          fill_rect(co[0],co[1],22,22,bg)
          co[inputs[c+1]]+=inputs[c+2]
          if co[1] > 202:
            co[1]=202
          if co[1] < 0:
            co[1]=0
          print(co[0])
          print(co[3])
          print(co[4])
          if co[0] < co[3]:
            co[0]=co[3]
          if co[0] > co[4]:
            co[0]=co[4]
          draw_plyr(co[0],co[1],co[2])
        c+=3
      if d:
        plyra=co
        co=plyrb
        d=False
    plyrb=co
    b+=1
  frames+=1
  sleep(lag)
#  draw_string(str(1/(monotonic()-fps)),0,0)
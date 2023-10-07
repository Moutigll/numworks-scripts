from kandinsky import *
from time import *
from ion import *
plyra=[50,101,(0,0,255),33,134]
plyrb=[250,101,(255,0,0),166,267]
bg=(255,255,255)
frames=0
inputs=["4",1,-1,"0",1,1,"1",0,-1,"2",0,1,"/",1,-1,"EXE",1,1,"+",0,-1,"-",0,1]
bl=[False,0,False,0,0,False,0,0,False,0,0,False,0,False,0,0,False,0,0,False,0,0]
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
draw_plyr(plyrb[0],plyrb[1],plyrb[2])
draw_plyr(plyra[0],plyra[1],plyra[2])
fill_rect(157,0,6,222,(0,0,0))
fill_rect(29,0,1,222,(0,0,0))
fill_rect(290,0,1,222,(0,0,0))
draw_bla(14,17,True)
draw_bla(306,199,False)
fill_rect(4,3,7,33,(0,0,0))
fill_rect(310,186,7,33,(0,0,0))
while True:
  fps=monotonic()
  if not bl[0]:
    if bl[1]+90 > frames:
      fill_rect(5,round((frames-bl[1])/3)+4,5,1,(0,255,0))
    else:
      bl[0]=True
  if not bl[11]:
    if bl[12]+90 > frames:
      fill_rect(311,round((frames-bl[12])/3)+187,5,1,(0,255,0))
    else:
      bl[11]=True
  if keydown(KEY_SINE) and bl[0]:
    bl[0]=False
    bl[1]=frames
    fill_rect(4,3,7,33,(0,0,0))
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
    fill_rect(310,186,7,33,(0,0,0))
    fill_rect(311,187,5,1,(0,255,0))
    if not bl[13]:
      bl[13]=True
      bl[14]=plyrb[0]-25
      bl[15]=plyrb[1]+8
    elif not bl[16]:
      bl[16]=True
      bl[17]=plyrb[0]-25
      bl[18]=plyrb[1]+8
    elif not bl[19]:
      bl[19]=True
      bl[20]=plyrb[0]-25
      bl[21]=plyrb[1]+8
  c=2
  a=[1,True]
  for i in range(2):
    for i in range(3):
      if bl[c]:
        fill_rect(bl[c+1],bl[c+2],1,5,(255,255,255))
        bl[c+1]+=a[0]
        draw_bla(bl[c+1],bl[c+2],a[1])
        if bl[c+1] > 276 or bl[c+1] < 43:
          bl[c]=False
          if a[1]:
            fill_rect(bl[c+1],bl[c+2],13,5,bg)
          else:
            fill_rect(bl[c+1]-12,bl[c+2],13,5,bg)
      c+=3
    c=13
    a=[-1,False]
  keys=list(get_keys())
  b=0
  for i in range(len(keys)):
    c=0
    d=True
    co=plyra
    for i in range(2):
      for i in range(4):
        if str(keys[b]) == inputs[c] and (co[0] > co[3] or inputs[c+2] == 1 or inputs[c+1] == 1) and (co[0] < co[4] or inputs[c+2] == -1 or inputs[c+1] == 1) and (co[1] > 0 or inputs[c+2] == 1 or inputs[c+1] == 0) and (co[1] < 202 or inputs[c+2] == -1 or inputs[c+1] == 0):
          fill_rect(co[0]-2,co[1]-2,24,2,bg)
          fill_rect(co[0]-2,co[1]+21,24,2,bg)
          fill_rect(co[0]-2,co[1]-2,2,24,bg)
          fill_rect(co[0]+21,co[1]-2,2,24,bg)
          co[inputs[c+1]]+=inputs[c+2]
          draw_plyr(co[0],co[1],co[2])
        c+=3
      if d:
        plyra=co
        co=plyrb
        d=False
    plyrb=co
    b+=1
  frames+=1
  draw_string(str(1/(monotonic()-fps)),0,0)
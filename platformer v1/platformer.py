from kandinsky import *
from math import *
from random import *
from kandinsky import *
from ion import *
from time import *
try:
  from level import *
except:
  draw_string("Vous avez besoin du fichier ",0,0)
  draw_string("level.py pour jouer!",0,19)
  sleep(999999)
player_x=130
advencement=lvlx=unpa=cfl=blcfrm=spwn=bjpc=sjpc=0
pu=jw=dcd=terf=bjp=sjp=False
pu=True
lvly=-333
player_y=117
green=(0,255,0)
yellow=(255,250,50)
blue=(0,255,255)
red=(255,0,0)
dblue=(0,0,255)
fill_rect(0,0,1,1,green)
fill_rect(1,0,1,1,yellow)
fill_rect(2,0,1,1,red)
fill_rect(3,0,1,1,dblue)
cgreen=get_pixel(0,0)
cyellow=get_pixel(1,0)
cblue=get_pixel(3,0)
cred=get_pixel(2,0)
def player(px,py):
  fill_rect(px,py,30,5,red)
  fill_rect(px,py,5,30,red)
  fill_rect(px+25,py,5,30,red)
  fill_rect(px,py+25,30,5,red)
  fill_rect(px+10,py+10,10,10,red)
def get_color(idc):
  if idc == 0:
    return blue
  if idc == 2:
    return red
  if idc == 3:
    return yellow
  if idc == 4:
    return dblue
  if idc == 5:
    return (randint(0,255),randint(0,255),randint(0,255))
  else:
    return green
def load_level(x,y,a,bf):
  nblvl=round(a/3)
  if bf == 1:
    x-=10
  elif bf == 2:
    x+=10
  xb=x
  for dyl in range(18):
    for dxl in range(11):
      fill_rect(x,y,30,30,get_color(level[int(nblvl)]))
      x+=30
      nblvl+=1
    x=xb
    y+=30
    nblvl=nblvl-11+(len(level)/18)
    player(player_x,player_y)
while True:
  a=monotonic()
  load_level(lvlx,lvly,advencement,blcfrm)
  cbg=get_pixel(player_x,player_y+30)
  cbd=get_pixel(player_x+29,player_y+30)
  chd=get_pixel(player_x+29,player_y-1)
  chg=get_pixel(player_x,player_y-1)
  cchd=get_pixel(player_x+30,player_y)
  ccbd=get_pixel(player_x+30,player_y+29)
  cchg=get_pixel(player_x-1,player_y)
  ccbg=get_pixel(player_x-1,player_y+29)
  cdhg=get_pixel(player_x+5,player_y+5)
  cdbd=get_pixel(player_x+24,player_y+24)
  cdbg=get_pixel(player_x+5,player_y+24)
  cdhd=get_pixel(player_x+24,player_y+5)
  acl = [cdbd,cdbg,cdhg]
  aclc=0
  for x in range(len(acl)):
    if acl[aclc] == cred:
      if spwn == 0:
        advencement=0
        lvly=-318
      elif spwn == 1:
        lvly=checpoint1[1]
        advencement=checpoint1[0]
      elif spwn == 2:
        lvly=checpoint2[1]
        advencement=checpoint2[0]
        dcd=True
      blcfrm=0
    if acl[aclc] == cblue:
      sleep(0.018)
      jw=True
    elif cdhd == cblue:
      sleep(0.018)
      jw=True
    else:
      if jw == True:
        jw=False
        pu=True
        sleep(0.018)
    aclc+=1
  if advencement == checpoint1[0] and lvly == checpoint1[1]:
    spwn=1
  if advencement == checpoint2[0] and lvly == checpoint2[1]:
    spwn=2
  if cdhg == cgreen or cdhd == cgreen or cdhg == (cyellow) or cdhd == cyellow:
    lvly-=15
  elif cdbd == cgreen or cdbg == cgreen or cdbg == cyellow or cdbd == cyellow:
    lvly+=15
  if keydown(KEY_RIGHT) and dcd == False:
    if ccbd == cgreen or cchd == cgreen or ccbd == cyellow or cchd == cyellow:
      pass
    else:
      advencement+=1
      blcfrm+=1
  if keydown(KEY_LEFT) and dcd == False:
    if ccbg == cgreen or cchg == cgreen or ccbg == cyellow or cchg == cyellow:
      pass
    else:
      blcfrm-=1
      advencement-=1
  if blcfrm < 0:
    blcfrm=2
  elif blcfrm > 2:
    blcfrm=0
  fall=True
  if unpa == 5:
    pu=True
  if jw == True:
    pu=False
  if keydown(KEY_UP) and pu == False and bjp == False and sjp == False and dcd == False:
    if chd == cgreen or chg == cgreen or chd == cyellow or chg == cyellow:
      pu=True
    else:
      lvly+=15
      unpa+=1
      fall=False
  if sjp == True:
    if sjpc < 2:
      lvly+=15
      fall=False
      sjpc+=1
    elif sjpc == 2:
      lvly+=15
      fall=False
      sjpc=0
      pu=True
      sjp=False
  elif bjp == True:
    if bjpc < 6:
      lvly+=15
      fall=False
      bjpc+=1
    elif bjpc == 6:
      lvly+=15
      fall=False
      bjpc=0
      pu=True
      bjp=False
  if fall == True:
    if cbg == cyellow or cbd == cyellow:
      if chd == cgreen or chg == cgreen or chd == cyellow or chg == cyellow:
        pass
      else:
        pu=True
        unpa=0
        if keydown(KEY_UP):
          bjp=True
        else:
          sjp=True
    elif cbg == cgreen or cbd == cgreen:
      pu=False
      unpa=0
      dcd=False
    else:
      lvly-=15
      pu=True
  if keydown(KEY_POWER) and keydown(KEY_THREE):
    if terf:
      terf=False
    else:
      terf=True
    sleep(0.1)
  if terf:
    draw_string("X: " + str(advencement),0,20)
    draw_string("Y: " + str(lvly),0,40)
    draw_string("FPS:"+str(1/(monotonic()-a)),0,0)
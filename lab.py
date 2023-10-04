from random import *
from kandinsky import *
from time import *
from ion import *
size=int(input("Enter the wanted size(between 1 and 75).\n"))
print("generating...")
lab=[]
st=[]
p1=[-1,15]
p2=[-1,35]
p_color=(255,0,0)
line=row=p=cpstn=c_contrast=0
drx=20
ctrst_lvl=True
dry=18
skip=False
#You change colors here:
  #Background:
w=(255,255,255)
  #Lab
l=(125,125,125)
  #Player 1:
r=(255,0,0)
  #Player 2:
g=(0,200,0)
  #Dice
b=(0,0,0)
wc=get_pixel(0,0)
def roll():
  fill_rect(268,21,34,34,w)
  d=randint(1,6)
  if d == 1:
    fill_rect(283,36,4,4,b)
  if d == 2:
    fill_rect(275,28,4,4,b)
    fill_rect(290,45,4,4,b)
  if d == 3:
    fill_rect(283,36,4,4,b)
    fill_rect(275,28,4,4,b)
    fill_rect(290,45,4,4,b)
  if d == 4:
    fill_rect(275,28,4,4,b)
    fill_rect(290,45,4,4,b)
    fill_rect(275,45,4,4,b)
    fill_rect(290,28,4,4,b)
  if d == 5:
    fill_rect(275,28,4,4,b)
    fill_rect(290,45,4,4,b)
    fill_rect(275,45,4,4,b)
    fill_rect(290,28,4,4,b)
    fill_rect(283,36,4,4,b)
  if d == 6:
    fill_rect(275,28,4,4,b)
    fill_rect(290,45,4,4,b)
    fill_rect(275,45,4,4,b)
    fill_rect(290,28,4,4,b)
    fill_rect(275,36,4,4,b)
    fill_rect(290,36,4,4,b)
  return d
def cursor(lc,cclr):
  set_pixel(21+lc*3,17,cclr)
  fill_rect(20+lc*3,12,3,5,cclr)
  set_pixel(21+lc*3,204,cclr)
  fill_rect(20+lc*3,205,3,5,cclr)
for i in range(size):
  line=[]
  for j in range(62):
    line.append(randint(0,2))
  lab.append(line)
  st.append(0)
line=0
fill_rect(0,0,340,240,w)
for i in range(size):
  for j in range(62):
    if lab[row][line] == 0:
      fill_rect(drx,dry,3,3,w)
    else:
      fill_rect(drx,dry,3,3,l)
    line+=1
    dry+=3
  line=0
  row+=1
  drx+=3
  dry=18
fill_rect(265,18,40,40,b)
fill_rect(268,21,34,34,w)
fill_rect(245,18,3,186,(255,200,100))
wcol=get_pixel(245,18)
fill_rect(17,63,3,3,r)
fill_rect(17,123,3,3,g)
draw_string("?",280,30)
draw_string("Moves",260,155)
draw_string("left:",260,170)
draw_string("X2",277,0)
def draw_menu(mcolor):
  fill_rect(250,60,66,24,mcolor)
  fill_rect(270,87,46,66,mcolor)
  draw_string("Turn: ",253,63)
  draw_string("roll",273,90)
  draw_string("wall",273,111)
  draw_string("move",273,132)
def menu_cursor(mc_x,mc_y,mc_color):
  fill_rect(mc_x,mc_y,12,14,mc_color)
  fill_rect(mc_x+12,mc_y+2,2,10,mc_color)
  fill_rect(mc_x+14,mc_y+4,2,6,mc_color)
  fill_rect(mc_x+16,mc_y+6,2,2,mc_color)
def contrast_n(c_contrast,ctrst_lvl):
  if c_contrast < 255 and ctrst_lvl == True:
    c_contrast+=1
  elif c_contrast == 255 and ctrst_lvl == True:
    ctrst_lvl=False
  if c_contrast > 0 and ctrst_lvl == False:
    c_contrast-=1
  elif c_contrast == 0 and ctrst_lvl == False:
    ctrst_lvl=True
  return c_contrast,ctrst_lvl
while True:
  fill_rect(277,190,50,24,w)
  draw_string("?",277,190)
  draw_menu(p_color)
  while not keydown(KEY_OK):
    c_contrast,ctrst_lvl=contrast_n(c_contrast,ctrst_lvl)
    menu_cursor(250,92,(255,c_contrast,255))
  menu_cursor(250,92,w)
  sleep(0.2)
  for i in range(30):
    count=roll()*2
    cursor(p,(255,0,255))
    sleep(0.05)
  fill_rect(277,190,50,24,w)
  draw_string(str(count),277,190)
  while not skip:
    if keydown(KEY_OK) or count == 0:
      skip=True
    c_contrast,ctrst_lvl=contrast_n(c_contrast,ctrst_lvl)
    menu_cursor(250,113,(255,c_contrast,255))
    if keydown(KEY_LEFT) and p  > 0:
      cursor(p,w)
      p-=1
      cursor(p,(255,0,255))
      sleep(0.06)
    if keydown(KEY_RIGHT) and p < 74:
      cursor(p,w)
      p+=1
      cursor(p,(255,0,255))
      sleep(0.06)
    if keydown(KEY_DOWN) and count > 0 and p != p1[0] and p != p2[0]:
      c=0
      st[p]+=1
      fill_rect(20+p*3,0,3,240,w)
      fill_rect(20+p*3,18,3,250,l)
      for i in range(62):
        if lab[p][c] == 0:
          fill_rect(20+p*3,(18+c*3)+st[p]*3,3,3,w)
        else:
          fill_rect(20+p*3,(18+c*3)+st[p]*3,3,3,l)
        c+=1
      fill_rect(20+p*3,0,3,18,w)
      fill_rect(20+p*3,204,3,40,w)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      cursor(p,(255,0,255))
      sleep(0.2)
    if keydown(KEY_UP) and count > 0 and p != p1[0] and p != p2[0]:
      c=0
      st[p]-=1
      fill_rect(20+p*3,0,3,240,w)
      fill_rect(20+p*3,18,3,250,l)
      for i in range(62):
        if lab[p][c] == 0:
          fill_rect(20+p*3,(18+c*3)+st[p]*3,3,3,w)
        else:
          fill_rect(20+p*3,(18+c*3)+st[p]*3,3,3,l)
        c+=1
      fill_rect(20+p*3,0,3,18,w)
      fill_rect(20+p*3,204,3,40,w)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      cursor(p,(255,0,255))
      sleep(0.2)
  menu_cursor(250,113,w)
  sleep(0.2)
  skip=False
  while not skip:
    if keydown(KEY_OK) or count == 0:
      skip=True
    c_contrast,ctrst_lvl=contrast_n(c_contrast,ctrst_lvl)
    menu_cursor(250,134,(255,c_contrast,255))
    if p_color == r:
      pstn=p1
    else:
      pstn=p2
    if keydown(KEY_LEFT) and count > 0 and get_pixel(19+(pstn[0]*3),18+(pstn[1]*3)) == wc and pstn[0] > -1:
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,w)
      pstn[0]-=1
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,p_color)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      sleep(0.2)
    if keydown(KEY_RIGHT) and count > 0 and get_pixel(24+(pstn[0]*3),18+(pstn[1]*3)) == wc:
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,w)
      pstn[0]+=1
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,p_color)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      sleep(0.2)
    elif keydown(KEY_RIGHT) and get_pixel(24+(pstn[0]*3),18+(pstn[1]*3)) == wcol:
      draw_string("You win !",0,0)
      sleep(10000)
    if keydown(KEY_UP) and count > 0 and get_pixel(20+(pstn[0]*3),17+(pstn[1]*3)) == wc and pstn[1] > 0:
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,w)
      pstn[1]-=1
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,p_color)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      sleep(0.2)
    if keydown(KEY_DOWN) and count > 0 and get_pixel(20+(pstn[0]*3),23+(pstn[1]*3)) == wc and pstn[1] < 61:
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,w)
      pstn[1]+=1
      fill_rect(20+(pstn[0]*3),18+(pstn[1]*3),3,3,p_color)
      count-=1
      fill_rect(277,190,50,24,w)
      draw_string(str(count),277,190)
      sleep(0.2)
    if p_color == r:
      p1=pstn
    else:
      p2=pstn
  if p_color == r:
    p_color=g
  else:
    p_color=r
  menu_cursor(250,134,w)
  sleep(0.2)
  skip=False
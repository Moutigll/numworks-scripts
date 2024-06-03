from kandinsky import *
from time import *
time=0.06
su=0
x=y=10
def point(xp,yp):
  for i in range(5):
    fill_rect(xp,yp,1,5,(0,0,0))
    sleep(time/5)
    xp+=1
  for i in range(5):
    fill_rect(xp,yp,1,5,(255,255,255))
    sleep(time/5)
    xp+=1
def bblank(xb,yb):
  for i in range(10):
    fill_rect(xb,yb,1,5,(255,255,255))
    sleep(time/5)
    xb+=1
def trait(xt,yt):
  for i in range(15):
    fill_rect(xt,yt,1,5,(0,0,0))
    sleep(time/5)
    xt+=1
  for i in range(5):
    fill_rect(xt,yt,1,5,(255,255,255))
    sleep(time/5)
    xt+=1
txt=list(input("Entrez le texte a traduire ").strip())
while True:
  try:
    a=txt[su]
  except:
    sleep(999999999)
  if txt[su] == "a" or txt[su] == "A":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "b" or txt[su] == "B":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "c" or txt[su] == "C":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "d" or txt[su] == "D":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "e" or txt[su] == "E":
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "f" or txt[su] == "F":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "g" or txt[su] == "G":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "h" or txt[su] == "H":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "i" or txt[su] == "I":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "j" or txt[su] == "J":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "k" or txt[su] == "K":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "l" or txt[su] == "L":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "m" or txt[su] == "M":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "n" or txt[su] == "N":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "o" or txt[su] == "O":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "p" or txt[su] == "P":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "q" or txt[su] == "Q":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "r" or txt[su] == "R":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "s" or txt[su] == "S":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "t" or txt[su] == "T":
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "u" or txt[su] == "U":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "v" or txt[su] == "V":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "w" or txt[su] == "W":
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "x" or txt[su] == "X":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "y" or txt[su] == "Y":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "z" or txt[su] == "Z":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "0":
    if x > 230 and y < 200:
      x=10
      y+=20
    elif x > 230 and y >= 200:
      x=y=10
      fill_rect(0,0,320,240,(255,255,255))
    else:
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      bblank(x,y)
      x+=10
  elif txt[su] == "1":
    if x > 230 and y < 200:
      x=10
      y+=20
    elif x > 230 and y >= 200:
      x=y=10
      fill_rect(0,0,320,240,(255,255,255))
    else:
      point(x,y)
      x+=10
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      bblank(x,y)
      x+=10
  elif txt[su] == "2":
    if x > 230 and y < 200:
      x=10
      y+=20
    elif x > 230 and y >= 200:
      x=y=10
      fill_rect(0,0,320,240,(255,255,255))
    else:
      point(x,y)
      x+=10
      point(x,y)
      x+=10
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      bblank(x,y)
      x+=10
  elif txt[su] == "9":
    if x > 230 and y < 200:
      x=10
      y+=20
    elif x > 230 and y >= 200:
      x=y=10
      fill_rect(0,0,320,240,(255,255,255))
    else:
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      trait(x,y)
      x+=20
      point(x,y)
      x+=10
      bblank(x,y)
      x+=10
  elif txt[su] == "3":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "4":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    trait(x,y)
    x+=20
    bblank(x,y)
    x+=10
  elif txt[su] == "5":
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "6":
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "7":
    trait(x,y)
    x+=20
    trait(x,y)
    x+=20
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    point(x,y)
    x+=10
    bblank(x,y)
    x+=10
  elif txt[su] == "8":
      if x > 230 and y < 200:
        x=10
        y+=20
      elif x > 230 and y >= 200:
        x=y=10
        fill_rect(0,0,320,240,(255,255,255))
      else:
        trait(x,y)
        x+=20
        trait(x,y)
        x+=20
        trait(x,y)
        x+=20
        point(x,y)
        x+=10
        point(x,y)
        x+=10
        bblank(x,y)
        x+=10
  elif txt[su] == " ":
    fill_rect(x-1,y,2,5,(255,0,0))
    for i in range(35):
      fill_rect(x,y,1,5,(255,255,255))
    sleep(time/5)
    x+=1
  else:
    draw_string(txt[su],x,y)
    for i in range(15):
      fill_rect(x,y,1,5,(255,255,255))
    sleep(time/5)
    x+=1
  su+=1
  if y >= 200 and x > 260:
    x=y=10
    fill_rect(0,0,320,240,(255,255,255))
  if x > 260:
    x=10
    y+=20
#############################
#                           #
#    Morse converter v1.0   #
#    --------------------   #
#         By Moutig         #
#                           #
############################# yeah i know i defeinitely should use list but i didn't know at the time
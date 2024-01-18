from kandinsky import *
from ion import *
from random import *
from time import *
p=input("Jouer avec la perspective des\nblancs (y/n):\n")
r=input("Jouer avec les reperes\nvisuels (y/n):\n")
n=["1","2","3","4","5","6","7","8"]
l=["A","B","C","D","E","F","G","H"]
kn=[42,43,44,36,37,38,30,31]
def dr(c):
  if c:
    c=(0,255,0)
  else:
    c=(255,0,0)
  fill_rect(22,0,3,200,c)
def gcol(x,y):
  if x%2 == 0 and y%2 == 0:
    return (255,233,197)
  elif x%2 == 0 and y%2 == 1:
    return "brown"
  elif x%2 == 1 and y%2 == 1:
    return (255,233,197)
  elif x%2 == 1 and y%2 == 0:
    return "brown"
for a in range(8):
  for i in range(8):
    fill_rect(25+(25*i),(25*a),25,25,gcol(i,a))
    if a == 7 and p == "y" and r == "y":
      draw_string(l[i],((i+1)*25)+7,(8*25)+5)
    elif a == 7 and r == "y":
      draw_string(l[7-i],((i+1)*25)+7,(8*25)+5)
  if p == "y" and r == "y":
    draw_string(n[7-a],5,(a*25)+5)
  elif r == "y":
    draw_string(n[a],5,(a*25)+5)
f=ct=d=st=bt=0
while True:
  c=[randint(0,7),randint(0,7)]
  fill_rect(25+(25*c[0]),(25*c[1]),25,25,(0,0,255))
  resp=False
  s=0
  ta=monotonic()
  while not resp:
    if s == 0:
      for i in range(18,26):
        if keydown(i):
          if (i-18 == c[0] and p == "y") or ((i-25)*-1 == c[0] and p != "y"):
            s=1
            sleep(0.3)
          else:
            f+=1
            st=0
            resp=True
            dr(False)
    elif s == 1:
      for i in range(8):
        if keydown(kn[i]):
          if kn.index(kn[i]) == (c[1]-7)*-1 and p == "y":
            s=1
            dr(True)
            st+=1
            resp=True
          elif kn.index(kn[i]) == c[1] and p != "y":
            s=1
            dr(True)
            resp=True
            st+=1
          else:
            resp=True
            dr(False)
            st=0
            f+=1
  ct+=1
  tt=monotonic()-ta
  d+=tt
  if st > bt:
    bt=st
  draw_string("T:"+str(round(d/ct,2)),230,0)
  draw_string("C:"+str(st),230,20)
  draw_string("B:"+str(bt),230,40)
  draw_string("P:"+str(round(f/(ct/100),2)),230,60)
  while len(get_keys()) != 0:
    pass
  fill_rect(25+(25*c[0]),(25*c[1]),25,25,gcol(c[0],c[1]))
  
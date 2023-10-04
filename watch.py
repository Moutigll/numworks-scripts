from time import *
from math import *
from ion import *
from kandinsky import *
UwU=False
def calculate(kk,x,y):
  a=int(kk/3600)
  b=int((kk-(a*3600))/60)
  c=int(kk-(a*3600)-(b*60))
  d=int((kk-(a*3600)-(b*60)-c)*10**3)
  draw_string(str(a)+"h "+str(b)+"min "+str(c)+"s "+str(d)+"ms",x,y)
while True:
  calculate(monotonic(),60,100)
  if keydown(KEY_OK):
    if UwU == False:
      UwU=True
      jaaj=monotonic()
      sleep(0.15)
      fill_rect(60,130,500,20,(255,255,255))
    else:
      UwU=False
      sleep(0.15)
  if UwU == True:
    calculate(monotonic()-jaaj,60,130)
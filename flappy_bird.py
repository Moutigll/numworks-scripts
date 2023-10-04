##########################
#                        #
#      Flappy bird       #
#      for Numworks      #
#  programmed by Moutig  #
##########################
#dedicace aux classes de
#secondes b et c du leon et
#a Bouffeur29
from math import *
from kandinsky import *
from ion import *
from time import *
from random import *
yellow=color(250,250,0)
blue=color(100,125,255)
on=True
green=color(30,210,0)
highscore=0
frame=0.1
cube_size=20
running=True
while on == True:
  x=150
  y=202
  a=350
  b=-115
  c=335
  d=35
  e=335
  f=150
  g=350
  h=180
  collision1=blue
  collision2=blue
  collision3=blue
  collision4=blue
  lvl=1
  score=0
  new=False
  speed=12
  ptspeed=0
  while running == True:
    if collision1 == green:
      running=False
    if collision2 == green:
      running=False
    if collision3 == green:
      running=False
    if collision4 == green:
      running=False
    fill_rect(0,0,340,240,blue)
    fill_rect(x,y,cube_size,cube_size,yellow)
    fill_rect(a,b,40,150,green)
    fill_rect(c,d,65,30,green)
    fill_rect(e,f,65,30,green)
    fill_rect(g,h,40,150,green)
    if y < 35:
      y=35
    if keydown(KEY_UP):
      y=y-42
    y=y+13
    if y > 202:
      y=202
    a=a-speed
    c=c-speed
    e=e-speed
    g=g-speed
    if a < -30:
      a=350
      c=335
      e=335
      g=350
      score=score+1
      ptspeed=ptspeed+1
      new=True
      lvl=randint(1,3)
    if ptspeed > 10:
      ptspeed=0
      speed=speed+1
    while new == True:
      if lvl == 1:
        b=-115
        d=35
        f=150
        h=180
        new=False
      elif lvl == 2:
        b=-85
        d=65
        f=180
        h=210
        new=False
      elif lvl == 3:
        b=-145
        d=5
        f=120
        h=150
        new=False
    collision1=get_pixel(x,y)
    collision2=get_pixel(x+20,y)
    collision3=get_pixel(x,y+20)
    collision4=get_pixel(x+20,y+20)
    draw_string("score:" + str(score),0,25)
    draw_string("high score:" + str(highscore),0,0)
    if score > highscore:
      highscore=score
    sleep(frame)
  draw_string("Push ok to restart!",65,100)
  if keydown(KEY_OK):
    running=True
from kandinsky import *
from time import *
from ion import *
from math import *
bpm="60"
beats=8
beats_lenght=8
beats_size=beats_lenght*3
espacement=((100-(beats*beats_lenght))/beats)*3
delay_lost=0
bt=60/int(bpm)
modif=False
delay_stats=total_delay=time_correct=0
pulsations=[2,3,5,6,8]
while True:
  if modif:
    bpm=input("Bpm: ")
    beats=int(input("Number of pulsations: "))
    while beats > 80:
      beats_lenght=int(input("Too much pulsations, reenter a number please: "))
    beats_lenght=int(input("Lenght of a pulsation: "))
    while beats_lenght > 100/beats:
      beats_lenght=int(input("Lenght too long, reenter one please: "))
    beats_size=int(beats_lenght*3)
    espacement=int(((100-(beats*beats_lenght))/beats)*3)
    pulsations=list(input("Marked pulsations: ").split(","))
    while len(pulsations) > beats:
      pulsations=list(input("Too many marked pulsations: ").split(","))
    modif=False
    bt=60/int(bpm)
    sleep(0.2)
    fill_rect(0,0,320,240,(255,255,255))
  delay1=monotonic()
  draw_string("Bpm: "+bpm,10,90)
  draw_string("Number of pulsations: "+str(beats),10,110)
  draw_string("Lenght of a pulsation: "+str(beats_lenght)+"%",10,130)
  draw_string("Nerd stats:",10,160)
  x_b=10
  nb=1
  for i in range(beats):
    fill_rect(int(x_b),5,beats_size,20,(0,200,0))
    nbb=0
    for i in range(len(pulsations)):
      if int(pulsations[nbb]) == nb:
        fill_rect(int(x_b),30,beats_size,3,(255,0,255))
      nbb+=1
    nb+=1
    x_b+=beats_size+espacement
  fill_rect(10,40,300,20,(0,0,0))
  r=10
  delay_total=0
  for i in range(100):
    fill_rect(r,40,3,20,(255,0,0))
    t_count=2
    for d in range(3):
      delay2=monotonic()
      if get_pixel(r-t_count,10) != (255,255,255) and get_pixel(r-t_count,31) != (255,255,255):
        fill_rect(r-t_count,5,1,20,(0,255,0))
        fill_rect(100,90,40,20,(0,255,0))
        fill_rect(230,90,80,20,(255,0,255))
      elif get_pixel(r-t_count,10) != (255,255,255):
        fill_rect(r-t_count,5,1,20,(0,255,0))
        fill_rect(100,90,40,20,(0,255,0))
        fill_rect(230,90,80,20,(100,0,100))
      else:
        fill_rect(100,90,40,20,(0,100,0))
        fill_rect(230,90,80,20,(100,0,100))
      t_count-=1
    if r > 31:
      fill_rect(160,90,40,20,(100,0,0))
    r+=3
    delay_total+=monotonic()-delay2
    sleep((bt/100)-(monotonic()-delay2)-(bt/998))
    if keydown(KEY_OK):
      modif=True
  fill_rect(160,90,40,20,(255,0,0))
  delay_lost=monotonic()-delay1
  draw_string("Estimated saved time: "+str(delay_total+bt/10),10,175)
  draw_string("Time corrected: "+str(delay_lost),10,190)
  draw_string("Goal: "+str(bt)+" Precision: "+str(floor(delay_lost/(bt/100)))+"%",10,205)
###########################    INSTRUCTIONS
#                         # Press OK to change the values.
#    Rythms generator     # Bpm is the speed of the main circle in number of time per minute.
#    ----------------     # Pulsations is the number of pulsations in one cycle.
#     v1.0 by Moutig      # Lenght is te duration of one pulsation in a percentage of an entire cycle.
#                         # Marked pulsations are the numbers of the pulsations that are marked in purple to create a rythm.
###########################   (ps: The program might not be calibrate for every model of numworks)
#The default rythm is a cinquillo
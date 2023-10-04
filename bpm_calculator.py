from kandinsky import *
from ion import *
from time import *
total_time=0
lasbeat=0
count=0
draw_string("Press ok to measure the bpm.",0,0)
draw_string("Press r to reset the counter.",0,20)
newbeat=0
recording=False
while True:
  if keydown(KEY_OK):
    newbeat=monotonic()
    recording=True
    sleep(0.15)
  while recording == True:
    if keydown(KEY_OK):
      lastbeat=newbeat
      newbeat=monotonic()
      total_time+=newbeat-lastbeat
      sleep(0.15)
      count+=1
      bpm=round(60/(total_time/count))
      fill_rect(0,45,320,20,(255,255,255))
      draw_string(str(bpm)+"bpm",0,45)
    if keydown(KEY_FOUR):
      count=0
      total_time=0
      recording=False
      draw_string("Bpm reset !",0,45)
      sleep(0.5)
      fill_rect(0,45,320,20,(255,255,255))
#############################
#                           #
#    Bpm calculator v1.0    #
#    -------------------    #
#        By Moutig          #
#                           #
#############################
try:
  import os
  if hasattr(os, "environ"):
    os.environ['KANDINSKY_ZOOM_RATIO'] = "4"
    os.environ['KANDINSKY_OS_MODE'] = '0'
except Exception as e: print(e)
from kandinsky import *
from random import *
from ion import keydown as kd
from time import *
seed(42)#if you want a custom seed
dl=0.1
lm=[0,0,0,0]
queue=[]
frames=0
drp=[50,0]
piece=[0,4,0,0]
pieces=[
[[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]]],
[[[0,1,0],[1,1,1],[0,0,0]],[[0,1,0],[0,1,1],[0,1,0]],[[0,0,0],[1,1,1],[0,1,0]],[[0,1,0],[1,1,0],[0,1,0]]],
[[[1,0,0],[1,1,1],[0,0,0]],[[0,1,1],[0,1,0],[0,1,0]],[[0,0,0],[1,1,1],[0,0,1]],[[0,1,0],[0,1,0],[1,1,0]]],
[[[0,0,1],[1,1,1],[0,0,0]],[[0,1,0],[0,1,0],[0,1,1]],[[0,0,0],[1,1,1],[1,0,0]],[[1,1,0],[0,1,0],[0,1,0]]],
[[[0,1,1],[1,1,0],[0,0,0]],[[0,1,0],[0,1,1],[0,0,1]],[[0,0,0],[0,1,1],[1,1,0]],[[1,0,0],[1,1,0],[0,1,0]]],
[[[1,1,0],[0,1,1],[0,0,0]],[[0,0,1],[0,1,1],[0,1,0]],[[0,0,0],[1,1,0],[0,1,1]],[[0,1,0],[1,1,0],[1,0,0]]],
[[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]]
] #gestion of collision boxes for tetromino in a 4/3x4/3 box

board=[
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[0,1,2,3,4,5,6,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9]] #save the current state of the gride in memory

fill_rect(0,0,320,223,(150,)*3)
fill_rect(77,0,95,223,(100,)*3)
fill_rect(80,0,89,219,(150,)*3)#draw background and lines of the board

def draw_board():#draw the current states of the board variable
  c=["cyan","purple","blue","orange","red","green","yellow",0,0,(30,30,30)]
  for i in range(10):
    for n in range(4,24):
      fill_rect((i*9)+80,(n*9)+4,8,8,c[board[n][i]])

draw_board()

def draw_tetromino(t,x,y,o,e):#draw the tetromino t at coordinates x,y(with the boxes of the grid), o is the orientation from 0 to 3, e determine if we erase (False) or not (True)
  if e:#if we don't erase we take normal colors and wich tetromino position to which color (b=t)
    c,b=["cyan","purple","blue","orange","red","green","yellow"],t
  else:#we pick background color and pos 0 so background
    c,b=[(30,30,30)],0
  x,y=(x*9)+80,(y*9)+4#convert gride coordinates to screen pixels
  try:
    for a in range(len(pieces[t][o])):#number of vertical line for position of the piece in the orientation of the piece in piece section of pieces variable
      for i in range(len(pieces[t][o][a])):#same but horizontal
        if pieces[t][o][a][i] == 1:fill_rect(x+(9*i),y+(9*a),8,8,c[b])#if not blank draw block with i,a multiply to correspond to correct block from base coordinates
  except Exception as e: print(e)

def new_bag():#to generate a new bag of 7 pieces
  global queue
  bag=[0,1,2,3,4,5,6]#bag with the 7 pieces
  bag=sorted(bag, key=lambda x: randint(0,1))#shuffle the bag
  queue+=bag#add it to the queue

def new_tetromino():
  global piece, drp, lm
  piece=[3,4,0,queue[0]]#setup the piece variable wich store all the caracteristics of the current active piece; 0-coordinate x, 1-coordinate y, 2-orientation, 3-wich piece with the queue
  lm=piece#store the last state of the current piece
  draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)#draw the active piece at start position
  drp[1]=0
  sleep(0.1)
  queue.remove(queue[0])
  if len(queue) == 7:#if needed, generate a new bag (when queue is too short)
    new_bag()

new_bag()
new_bag()
new_tetromino()

while True:
  if kd(4):
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    new_tetromino()
  if kd(30) or kd(31) or kd(32):#if rotation (keys 7, 8, 9)
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)#erase old tetromino
    if kd(30):#180°
      if piece[2] < 2:
        piece[2]+=2#change orientation
      else:
        piece[2]-=2
    if kd(31):#CounterClockwise
      if piece[2] != 0:
        piece[2]-=1
      else:
        piece[2]=3
    if kd(32):#Clockwise
      if piece[2] != 3:
        piece[2]+=1
      else:
        piece[2]=0
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)#update tetromino
    sleep(0.1)
      
#33, 45, 50, 51, 52
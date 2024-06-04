try:
  import os
  if hasattr(os, "environ"):
    os.environ['KANDINSKY_ZOOM_RATIO'] = "2"
    os.environ['KANDINSKY_OS_MODE'] = '3'
    from keyboard import *
except Exception as e:
  print(e)
  def is_pressed():
    pass
from kandinsky import *
from random import *
from ion import *
from ion import keydown as kd
from time import *
#seed(42)#if you want a custom seed
arr=[10,0]#amount of frames between each repetitions left or right
td=[40,0]#amount of frames after rotation or hardrop
das=[2,0]#frames between each block down when press down
queue_size=5#how many tetromino are shown in advance (may impact performances)
queue_minimal=2#toggle this to reduce queue impact 0=nothing, 1=colors, 2=letters
shadows=False
dl=0.1
lm=[0,0,0,0]
let=["i","t","j","l","s","z","o"]
queue=[]
frames=0
drp=[50,0]
os=piece=[0,4,0,0]
pieces=[
[[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]],
[[[0,1,0],[1,1,1],[0,0,0]],[[0,1,0],[0,1,1],[0,1,0]],[[0,0,0],[1,1,1],[0,1,0]],[[0,1,0],[1,1,0],[0,1,0]]],
[[[1,0,0],[1,1,1],[0,0,0]],[[0,1,1],[0,1,0],[0,1,0]],[[0,0,0],[1,1,1],[0,0,1]],[[0,1,0],[0,1,0],[1,1,0]]],
[[[0,0,1],[1,1,1],[0,0,0]],[[0,1,0],[0,1,0],[0,1,1]],[[0,0,0],[1,1,1],[1,0,0]],[[1,1,0],[0,1,0],[0,1,0]]],
[[[0,1,1],[1,1,0],[0,0,0]],[[0,1,0],[0,1,1],[0,0,1]],[[0,0,0],[0,1,1],[1,1,0]],[[1,0,0],[1,1,0],[0,1,0]]],
[[[1,1,0],[0,1,1],[0,0,0]],[[0,0,1],[0,1,1],[0,1,0]],[[0,0,0],[1,1,0],[0,1,1]],[[0,1,0],[1,1,0],[1,0,0]]],
[[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]]
] #gestion of collision boxes for tetromino in a 4/3x4/3 box

#List of wallkick

table0=[
#J, L, T, S, Z Tetromino Wall Kick Data
#Test0 Test1  Test2  Test3  Test4
[0,0,  -1,0,  -1,-1, 0,2,   -1,2,],#0>>1
[0,0,  1,0,   0,1,   -1,-3, 1,0  ],#1>>0
[0,0,  1,0,   1,1,   0,-2,  1,-2 ],#1>>2
[0,0,  -1,0,  0,-1,  1,3,   -1,0 ],#2>>1
[0,0,  1,0,   1,-1,  0,2,   1,2  ],#2>>3
[0,0,  -1,0,  0,1,   1,-3,  -1,0 ],#3>>2
[0,0,  -1,0,  -1,1,  0,-2,  -1,-2],#3>>0
[0,0,  1,0,   0,-1,  -1,3,  1,0  ],#0>>3
#I Tetromino Wall Kick Data
#Test0 Test1  Test2  Test3  Test4
[0,0,  -2,0,  1,0,   -2,1,  1,-2 ],#0>>1
[0,0,  2,0,  -3,0,   3,-1,  -3,3 ],#1>>0
[0,0,  -1,0,  2,0,   -1,-2, 2,2  ],#1>>2
[0,0,  1,0,   -3,0,  3,2,   -3,-3],#2>>1
[0,0,  2,0,   -1,0,  2,-1,  -1,2 ],#2>>3
[0,0,  -2,0,  3,0,   -3,1,  3,-3 ],#3>>2
[0,0,  1,0,   -2,0,  1,2,   -2,-1],#3>>0
[0,0,  -1,0,  3,0,   -3,-2, 3,3  ] #0>>3
]



board=[
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],#top
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],
[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],#bottom
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
] #save the current state of the gride in memory

fill_rect(0,0,320,223,(150,)*3)
fill_rect(77,0,95,223,(100,)*3)
fill_rect(80,0,89,219,(150,)*3)#draw background and lines of the board

def draw_board():#draw the current states of the board variable
  c=["cyan","purple","blue","orange","green","red","yellow",(255,)*3,0,(30,)*3]
  for n in range(4,24):
    for i in range(3,13):
      fill_rect((i*9)+53,(n*9)+4,8,8,c[board[n][i]])

draw_board()

def draw_tetromino(t,x,y,o,e):#draw the tetromino t at coordinates x,y(with the boxes of the grid), o is the orientation from 0 to 3, e determine if we erase (False) or not (True)
  if e:#if we don't erase we take normal colors and wich tetromino position to which color (b=t)
    c,b=["cyan","purple","blue","orange","green","red","yellow"],t
  else:#we pick background color and pos 0 so background
    c,b=[(30,)*3],0
  x,y=(x*9)+53,(y*9)+4#convert gride coordinates to screen pixels
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
  piece=[6,4,0,queue[0]]#setup the piece variable wich store all the caracteristics of the current active piece; 0-coordinate x, 1-coordinate y, 2-orientation, 3-wich piece with the queue
  lm=piece#store the last state of the current piece
  draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)#draw the active piece at start position
  drp[1]=0
  sleep(0.1)
  queue.remove(queue[0])
  if len(queue) == 7:#if needed, generate a new bag (when queue is too short)
    new_bag()
  x,y=172,32
  if queue_minimal == 2: draw_string(let[queue[0]]+let[queue[1]]+let[queue[2]]+let[queue[3]]+let[queue[4]],x,y)
  for q in range(queue_size):
    if queue_minimal == 0: pass
    elif queue_minimal == 1: pass

def move(x,y):
  check=True
  try:
    for i in range(len(pieces[piece[3]][piece[2]])):#range de width of the orientation of the piece
      for j in range(len(pieces[piece[3]][piece[2]])):
        if (board[piece[1]+i+y][piece[0]+j+x] != 9) and (pieces[piece[3]][piece[2]][i][j] == 1):#if not all the box corresponding to the state of the tetromino are empty
          check=False
  except:
    check=False
  if check:
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    piece[0]=piece[0]+x
    piece[1]=piece[1]+y
new_bag()
new_bag()
new_tetromino()

while True:
  if kd(45) or kd(1):
    for k in range(24):
      move(0,1)
    for i in range(len(pieces[piece[3]][piece[2]])):#range de width of the orientation of the piece
      for j in range(len(pieces[piece[3]][piece[2]])):
        if pieces[piece[3]][piece[2]][i][j] == 1:
          board[piece[1]+i][piece[0]+j]=piece[3]
    l=[]
    for i in range(24):
      a=0
      try:
        while board[i][a] != 9:a+=1
      except:
        l.append(i)
    if len(l) > 0:
      for i in range(len(l)):
        board.remove(board[l[i]])
        board.insert(0,[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7])
    draw_board()
    new_tetromino()
  if kd(2) or kd(51):
    if das[1] == das[0]:
      move(0,1)
      das[1]=0
    else:
      das[1]+=1
  else: das[1]=das[0]
  if kd(0) or kd(50):#if keydown left
  
    if arr[1] == arr[0]:
      move(-1,0)
      arr[1]=0
    else:
      arr[1]+=1
  elif kd(3) or kd(52):#if keydown right
    if arr[1] == arr[0]:
      move(1,0)
      arr[1]=0
    else:
      arr[1]+=1
  else: arr[1]=arr[0]
  if (kd(3) or kd(52) or  kd(0) or kd(50)) and shadows:
    a=piece[1]
    for k in range(24):
      move(0,1)
    draw_tetromino(os[3],os[0],os[1],os[2],False)
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)
    os=[piece[0],piece[1],piece[2],piece[3]]
    piece[1]=a
  if kd(30) or kd(31) or kd(32) or is_pressed('w') or is_pressed('x') or is_pressed('c'):#eys 7, 8, 9
    if td[1] == td[0]:
      td[1]=0
      draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)#erase old tetromino
      try:
        if kd(30) or is_pressed('w'):#180°
          if piece[2] < 2:
            piece[2]+=2#change orientation
          else:
            piece[2]-=2
        if kd(31) or is_pressed('x'):#CounterClockwise
          check=(piece[2]*2)-1#define which table kick to check, 0>>1, 1>>2, 2>>3
          if piece[2] != 0:
            piece[2]-=1
          else:
            check=7#table kick 0>>3
            piece[2]=3
          invalid=True
          c=-1
          if piece[3] == 0:#if piece is I the jump 8 lines to get to the special table for I
            check+=8
          while invalid:
            invalid=False
            c+=1
            for i in range(len(pieces[piece[3]][piece[2]])):#range de width of the orientation of the piece
              for j in range(len(pieces[piece[3]][piece[2]])):
                if (board[piece[1]+i+table0[check][(c*2)+1]][piece[0]+j+table0[check][c*2]] != 9) and (pieces[piece[3]][piece[2]][i][j] == 1) and not invalid:#if board at piece position + boxe check is full and the corresponding one in the orientation pieces table is too (i=y,j=x) add table[check][attempt(c)] if necessary
                  invalid=True
            piece[1]+=table0[check][(c*2)+1]#update piece position according to kick table
            piece[0]+=table0[check][c*2]
        if kd(32) or is_pressed('c'):#Clockwise
          check=piece[2]*2
          if piece[2] != 3:
            piece[2]+=1
          else:
            piece[2]=0
            check=6#table kick 3>>0
          invalid=True
          c=-1
          if piece[3] == 0:
            check+=8
          while invalid:
            invalid=False
            c+=1
            for i in range(len(pieces[piece[3]][piece[2]])):
              for j in range(len(pieces[piece[3]][piece[2]])):
                if (board[piece[1]+i+table0[check][(c*2)+1]][piece[0]+j+table0[check][c*2]] != 9) and (pieces[piece[3]][piece[2]][i][j] == 1) and not invalid:
                  invalid=True
          piece[1]+=table0[check][(c*2)+1]
          piece[0]+=table0[check][c*2]
      except:pass
    else:
      td[1]+=1
  else:
    td[1]=td[0]
  if get_keys != {}:
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)#update tetromino
  frames+=1
#33, 45, 50, 51, 52
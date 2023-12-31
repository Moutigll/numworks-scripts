from kandinsky import *
from random import *
from ion import *
from time import *
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
]
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
[9,9,9,9,9,9,9,9,9,9]
]
fill_rect(0,0,320,223,(150,)*3)
fill_rect(77,0,95,223,(100,)*3)
fill_rect(80,0,89,219,(150,)*3)
def draw_board():
  c=["cyan","purple","blue","orange","red","green","yellow",0,0,(30,30,30)]
  for i in range(10):
    for n in range(4,24):
      fill_rect((i*9)+80,(n*9)+4,8,8,c[board[n][i]])
draw_board()
def draw_tetromino(t,x,y,o,e):
  if e:
    c,b=["cyan","purple","blue","orange","red","green","yellow"],t
  else:
    c,b=[(30,30,30)],0
  x,y=(x*9)+80,(y*9)+4
  try:
    for a in range(len(pieces[t][o])):
      for i in range(len(pieces[t][o][a])):
        if pieces[t][o][a][i] == 1:
          fill_rect(x+(9*i),y+(9*a),8,8,c[b])
  except:pass
def deplace_piece(p,o,x,y,e):
  global board,lm
  old=board
  ok=True
  s=len(pieces[p][o])
  for i in range(s):
    for j in range(s):
      if pieces[p][o][i][j] == 1 and y+i < 24 and old[y+i][x+j] == 9 and ok:
        old[y+i][x+j]=p
      elif y+i > 23:
        ok=False
      elif pieces[p][o][i][j] == 1 and old[y+i][x+j] != 9:
        ok=False
  if ok:
    if e:
      for i in range(s):
        for j in range(s):
          if pieces[lm[2]][lm[3]][i][j] == 1 and old[lm[1]+i][lm[0]+j] == lm[2]:
            old[lm[1]+i][lm[0]+j]=9
    board=old
    lm=[x,y,p,o]
  else:
    lm=[0,0,0,0]
  return ok

def new_bag():
  global queue
  bag=[0,1,2,3,4,5,6]
  for i in range(7):
    a=randint(0,len(bag)-1)
    queue.append(bag[a])
    bag.remove(bag[a])
def new_tetromino():
  global piece, drp
  piece[0],piece[1],piece[2],piece[3]=3,4,0,queue[0]
  draw_tetromino(queue[0],piece[0],piece[1],piece[2],True)
  deplace_piece(piece[3],piece[2],piece[0],piece[1],False)
  lm=[3,4,queue[0],0]
  drp[1]=0
  sleep(0.1)
  queue.remove(queue[0])
  if len(queue) == 7:
    new_bag()
new_bag()
new_bag()
new_tetromino
while True:
  jean=monotonic()
  if keydown(KEY_LEFTPARENTHESIS):
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    piece[2]+=1
    if piece[2] == 4:
      piece[2]=0
      deplace_piece(piece[3],piece[2],piece[0],piece[1],True)
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)
    sleep(dl)
  if keydown(KEY_NINE):
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    piece[2]-=1
    if piece[2] == -1:
      piece[2]=3
    deplace_piece(piece[3],piece[2],piece[0],piece[1],True)
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)
    sleep(dl)
  if keydown(KEY_EIGHT):
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    if piece[2] > 1:
      piece[2]-=2
    else:
      piece[2]+=2 
    deplace_piece(piece[3],piece[2],piece[0],piece[1],True)
    draw_tetromino(queue[0],piece[0],piece[1],piece[2],True)
    sleep(dl)
  if drp[1] > drp[0]:
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],False)
    drp[1]=0
    piece[1]+=1
    a=deplace_piece(piece[3],piece[2],piece[0],piece[1],True)
    if not a:
      draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)
      new_tetromino()
    draw_tetromino(piece[3],piece[0],piece[1],piece[2],True)
  else:
    drp[1]+=1
  frames+=1
  draw_board()
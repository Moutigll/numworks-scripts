from kandinsky import *
from ion import *
from time import *
try:
  from os import *
except:
  def fill_circle(x,y,r,c):
    fill_rect(x-r,y-r,r*2,r*2,c)
cursor=[[92,92],[158,43],1,True]
selected_piece=[False,42,42,"",[]]
ct=(150,)*3
turn=True
rq=False
dl=0.2
knight = [
"....**.....",
"...*+*.....",
"..*+++*....",
".*+*+++*...",
"*+++++++*..",
"*+++*+++*..",
".***++++*..",
"...*++++*..",
"..*++++*...",
"..*******..",
".*+++++++*.",
"*+++++++++*",
"***********",
]
rook = [
".**.***.**.",
".*+**+**+*.",
".*+++++++*.",
".*+++++++*.",
".*********.",
"..*+++++*..",
"..*+++++*..",
"..*+++++*..",
"..*+++++*..",
"..*******..",
".*+++++++*.",
"*+++++++++*",
"***********",
]
bishop = [
".....*.....",
"....*+*....",
"...*+*+*...",
"..*++*++*..",
"..*+***+*..",
".*+++*+++*.",
".*+++*+++*.",
".*+++++++*.",
"..*+++++*..",
"...*****...",
".**+++++**.",
"*+++++++++*",
"***********",
]
pawn = [
"...........",
"...........",
"....***....",
"...*+++*...",
"...*+++*...",
"...*+++*...",
"....***....",
"...*+++*...",
"....*+*....",
"....*+*....",
"...*****...",
"..*+++++*..",
"..*******..",
]
queen = [
"............",
"............",
".*...*...*.",
".**.*+*.**.",
".*+*+++*+*.",
".*+++++++*.",
".*+++++++*.",
"..*+++++*..",
"...*+++*...",
"...*+++*...",
"..*+++++*..",
".*+++++++*.",
".*********.",
]
king = [
".....*.....",
"....***....",
".....*.....",
".**.*+*.**.",
".*+*+++*+*.",
".*+++++++*.",
".*+++++++*.",
".*+++++++*.",
"..*+++++*..",
"..*+++++*..",
".*+++++++*.",
"*+++++++++*",
"***********",
]
last_move=[-42,-42,-69,-69,queen,True]
board=[
[[rook,False,False],[knight,False],[bishop,False],0,[king,False,False],0,0,[rook,False,False]],
[[pawn,False],[pawn,False],[pawn,False],[pawn,False],[pawn,False],0,[pawn,False],[pawn,False]],
[0,0,0,0,0,[queen,True],0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[[pawn,True],[pawn,True],[pawn,True],[pawn,True],[pawn,True],[pawn,True],[pawn,True],[pawn,True]],
[[rook,True,False],0,0,0,[king,True,False],0,0,[rook,True,False]],
]
def draw_board():
  c=(255,233,197)
  x=0
  y=20
  a=0
  for i in range(8):
    b=0
    for i in range(8):
      fill_rect(x,y,23,23,c)
      if c == (255,233,197):
        c="brown"
      else:
        c=(255,233,197)
      if board[a][b] != 0:
        draw_piece(board[a][b][0],board[a][b][1],x+6,y+5)
      x+=23
      b+=1
    if c == (255,233,197):
      c="brown"
    else:
      c=(255,233,197)
    x=0
    a+=1
    y+=23
def get_col(l,c):
  if l%2 == 0 and c%2 == 0:
    c=[(255,233,197),"brown"]
  elif l%2 == 0 and c%2 == 1:
    c=["brown",(255,233,197)]
  elif l%2 == 1 and c%2 == 1:
    c=[(255,233,197),"brown"]
  elif l%2 == 1 and c%2 == 0:
    c=["brown",(255,233,197)]
  return c
def draw_cursor():
  global cursor, turn
  if cursor[2] == 0:
    if turn:
      a=0
    else:
      a=1
    c=get_col(int((cursor[1][a]-20)/23),int(cursor[0][a]/23))
    fill_rect(cursor[0][a],cursor[1][a],23,2,c[0]);fill_rect(cursor[0][a],cursor[1][a],2,23,c[0]);fill_rect(cursor[0][a]+21,cursor[1][a],2,23,c[0]);fill_rect(cursor[0][a],cursor[1][a]+21,23,2,c[0]);fill_rect(cursor[0][a]-2,cursor[1][a]-2,2,2,c[0]);fill_rect(cursor[0][a]+23,cursor[1][a]-2,2,2,c[0]);fill_rect(cursor[0][a]+23,cursor[1][a]+23,2,2,c[0]);fill_rect(cursor[0][a]-2,cursor[1][a]+23,2,2,c[0]);fill_rect(cursor[0][a],cursor[1][a]-2,23,2,c[1]);fill_rect(cursor[0][a],cursor[1][a]+23,23,2,c[1]);fill_rect(cursor[0][a]-2,cursor[1][a],2,23,c[1]);fill_rect(cursor[0][a]+23,cursor[1][a],2,23,c[1])
  else:
    if turn:
      c=(255,)*3
      x,y=cursor[0][0],cursor[1][0]
    elif not turn:
      c=(0,)*3
      x,y=cursor[0][1],cursor[1][1]
    elif cursor[2] == 3:
      c=(0,150,255)
    fill_rect(x-2,y-2,27,4,c);fill_rect(x-2,y-2,4,27,c);fill_rect(x+21,y-2,4,27,c);fill_rect(x-2,y+21,27,4,c)
def deplace_cursor(x,y):
  global cursor, turn
  if turn:
    a=0
  else:
    a=1
  cursor[2]=0
  draw_cursor()
  cursor[0][a]+=x
  cursor[1][a]+=y
  cursor[2]=1
  fill_rect(0,0,100,20,(255,)*3)
  draw_string(str(is_menaced([int(cursor[0][a]/23),int((cursor[1][a]-20)/23)],turn)),0,0)
  draw_cursor()
  sleep(dl)
def draw_piece(p,c,x,y):
  dx=x
  b=0
  if c:
    c=[(200,)*3,(255,)*3]
  else:
    c=[(0,)*3,(75,)*3]
  for i in range(13):
    a=list(p[b])
    d=0
    for i in range(11):
      if a[d] == "*":
        set_pixel(x,y,c[0])
      elif a[d] == "+":
        set_pixel(x,y,c[1])
      x+=1
      d+=1
    x=dx
    y+=1
    b+=1
def highlight_piece(x,y,c):
  fill_rect(x+2,y+2,19,3,c)
  fill_rect(x+2,y+2,3,19,c)
  fill_rect(x+18,y+2,3,19,c)
  fill_rect(x+2,y+18,19,3,c)
def is_menaced(c,t):
  global board
  a=False
  util=[[True,-1,1],[True,-1,-1],[False,1,1],[False,1,-1]]
  for i in range(4):
    try:
      if t == util[i][0] and (board[c[1]+util[i][1]][c[0]+util[i][2]][0] == pawn and board[c[1]+util[i][1]][c[0]+util[i][2]][1] != t):
        a=True
    except:
      pass
  util=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
  for i in range(8):
    try:
      bd=board[c[1]+util[i][0]][c[0]+util[i][1]]
      if bd[0] == knight and bd[1] != t:
        a=True
    except:
      pass
  util=[1,0,-1,0,0,-1,0,1,1,1,-1,-1,-1,1,1,-1]
  for i in range(8):
    b=1
    try:
      while board[c[1]+(b*util[i*2])][c[0]+(b*util[(i*2)+1])] == 0:
        b+=1
      if c[1]+(b*util[i*2]) < 8 and c[1]+(b*util[i*2]) > -1 and c[0]+(b*util[(i*2)+1]) > -1 and c[0]+(b*util[(i*2)+1]) < 8:
        u=board[c[1]+(b*util[i*2])][c[0]+(b*util[(i*2)+1])]
        if u[1] != t and (u[0] == queen or (i < 4 and u[0] == rook) or (i > 3 and u[0] == bishop) or (b == 1 and u[0] == king)):
          a=True
    except:
      pass
  return a
draw_board()
draw_cursor()
while True:
  if turn:
    a=0
  else:
    a=1
  if keydown(KEY_LEFT) and keydown(KEY_UP) and cursor[0][a] > 0 and cursor[1][a] > 25:
    deplace_cursor(-23,-23)
  elif keydown(KEY_RIGHT) and keydown(KEY_UP) and cursor[0][a] < 154 and cursor[1][a] > 25:
    deplace_cursor(23,-23)
  elif keydown(KEY_LEFT) and keydown(KEY_DOWN) and cursor[0][a] > 0 and cursor[1][a] < 179:
    deplace_cursor(-23,23)
  elif keydown(KEY_RIGHT) and keydown(KEY_DOWN) and cursor[0][a] < 154 and cursor[1][a] < 179:
    deplace_cursor(23,23)
  elif keydown(KEY_LEFT):
    if cursor[0][a] < 1:
      deplace_cursor(+161,0)
    else:
      deplace_cursor(-23,0)
  elif keydown(KEY_RIGHT):
    if cursor[0][a] > 153:
      deplace_cursor(-161,0)
    else:
      deplace_cursor(23,0)
  elif keydown(KEY_UP):
    if cursor[1][a] < 21:
      deplace_cursor(0,+161)
    else:
      deplace_cursor(0,-23)
  elif keydown(KEY_DOWN):
    if cursor[1][a] > 178:
      deplace_cursor(0,-161)
    else:
      deplace_cursor(0,23)
  if keydown(KEY_OK):
    if turn:
      t=0
    else:
      t=1
    if board[int(((cursor[1][t]-20)/23))][int((cursor[0][t]/23))] != 0 and board[int(((cursor[1][t]-20)/23))][int((cursor[0][t]/23))][1] == turn:
      a=0
      for i in range(len(selected_piece[4])):
        c=get_col(int(selected_piece[4][a][1]/23),int((selected_piece[4][a][2]-20)/23))[0]
        if selected_piece[4][a][0]:
          fill_circle(selected_piece[4][a][1]+11,selected_piece[4][a][2]+11,4,c)
        else:
          highlight_piece(selected_piece[4][a][1],selected_piece[4][a][2],c)
        a+=1
      if selected_piece[0]:
        highlight_piece(selected_piece[2]*23,(selected_piece[1]*23)+20,get_col(selected_piece[1],selected_piece[2])[0])
        selected_piece[4]=[]
      else:
        selected_piece[0]=True
      if int(((cursor[1][t]-20)/23)) == selected_piece[1] and int((cursor[0][t]/23)) == selected_piece[2]:
        highlight_piece(selected_piece[2]*23,(selected_piece[1]*23)+20,get_col(selected_piece[1],selected_piece[2])[0])
        selected_piece[0]=False
        selected_piece[1],selected_piece[2],selected_piece[3],selected_piece[4]=42,42,42,[]
      else:
        selected_piece[1],selected_piece[2]=int(((cursor[1][t]-20)/23)),int((cursor[0][t]/23))
        selected_piece[3]=board[selected_piece[1]][selected_piece[2]][0]
        if selected_piece[3] == pawn:
          if turn == True:
            p=-23
            q=6
          else:
            p=23
            q=1
          if board[selected_piece[1]+int(p/23)][selected_piece[2]] == 0:
            selected_piece[4].append([True,cursor[0][t],cursor[1][t]+p])
            try:
              if board[selected_piece[1]+int((p/23)*2)][selected_piece[2]] == 0 and selected_piece[1] == q:
                  selected_piece[4].append([True,cursor[0][t],cursor[1][t]+(p*2)])
            except:
              pass
          try:
            if board[selected_piece[1]+int(p/23)][selected_piece[2]-1] != 0 and board[selected_piece[1]+int(p/23)][selected_piece[2]-1][1] != turn:
              selected_piece[4].append([False,cursor[0][t]-23,cursor[1][t]+p])
          except:
            pass
          try:
            if board[selected_piece[1]+int(p/23)][selected_piece[2]+1] != 0 and board[selected_piece[1]+int(p/23)][selected_piece[2]+1][1] != turn:
              selected_piece[4].append([False,cursor[0][t]+23,cursor[1][t]+p])
          except:
            pass
        elif selected_piece[3] == knight:
          util=[[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1],]
          for i in range(8):
            try:
              if board[selected_piece[1]+util[i][0]][selected_piece[2]+util[i][1]] == 0:
                selected_piece[4].append([True,cursor[0][t]+(util[i][1]*23),cursor[1][t]+(util[i][0]*23)])
              elif board[selected_piece[1]+util[i][0]][selected_piece[2]+util[i][1]][1] != turn:
                selected_piece[4].append([False,cursor[0][t]+(util[i][1]*23),cursor[1][t]+(util[i][0]*23)])
            except:
              pass
        elif selected_piece[3] == rook or selected_piece[3] == bishop or selected_piece[3] == queen or selected_piece[3] == king:
          if selected_piece[3] == rook:
            r=1
            util=[[1,0,8,8],[-1,0,0,0],[0,1,8,8],[0,-1,0,0]]
          elif selected_piece[3] == queen:
            util=[[1,0,8,8],[-1,0,0,0],[0,1,8,8],[0,-1,0,0]]
            r=2
          elif selected_piece[3] == king:
            util=[[1,0,8,8],[-1,0,0,0],[0,1,8,8],[0,-1,0,0]]
            r=2
            if board[selected_piece[1]][selected_piece[2]][2] == False:
              if not is_menaced([selected_piece[2],selected_piece[1]],turn):
                try:
                  if not is_menaced([5,selected_piece[1]],turn) and not is_menaced([6,selected_piece[1]],turn) and not is_menaced([7,selected_piece[1]],turn) and board[selected_piece[1]][7][2] == False and board[selected_piece[1]][6] == 0 and board[selected_piece[1]][5] == 0:
                    selected_piece[4].append([True,138,(selected_piece[1]*23)+20])
                    rq=True
                except:
                  pass
                try:
                  if not is_menaced([3,selected_piece[1]],turn) and not is_menaced([2,selected_piece[1]],turn) and not is_menaced([1,selected_piece[1]],turn) and not is_menaced([0,selected_piece[1]],turn) and not board[selected_piece[1]][0][2] and board[selected_piece[1]][1] == 0 and board[selected_piece[1]][2] == 0 and board[selected_piece[1]][3] == 0:
                    selected_piece[4].append([True,46,(selected_piece[1]*23)+20])
                    rq=True
                except:
                  pass
          else:
            r=1
            util=[[1,1,8,8],[-1,1,0,8],[-1,-1,0,0],[1,-1,8,0]]
          for i in range(r):
            a=0
            for i in range(4):
              h=1
              k=True
              try:
                while (board[selected_piece[1]+(util[a][0]*h)][selected_piece[2]+(util[a][1]*h)] == 0) and k == True:
                  selected_piece[4].append([True,cursor[0][t]+((util[a][1]*h)*23),cursor[1][t]+((util[a][0]*h)*23)])
                  h+=1
                  if selected_piece[3] == king:
                    k=False
              except:
                pass
              try:
                if board[selected_piece[1]+(util[a][0]*h)][selected_piece[2]+(util[a][1]*h)][1] != turn:
                  if selected_piece[3] == king and h < 2:
                    selected_piece[4].append([False,cursor[0][t]+((util[a][1]*h)*23),cursor[1][t]+((util[a][0]*h)*23)])
                  else:
                    selected_piece[4].append([False,cursor[0][t]+((util[a][1]*h)*23),cursor[1][t]+((util[a][0]*h)*23)])
              except:
                pass
              a+=1
            util=[[1,1,8,8],[-1,1,0,8],[-1,-1,0,0],[1,-1,8,0]]
        a=0
        while len(selected_piece[4]) > a:
          if selected_piece[4][a][2] < 20:
            selected_piece[4].remove(selected_piece[4][a])
            a-=1
          a+=1
        if len(selected_piece[4]) > 0:
          highlight_piece(cursor[0][t],cursor[1][t],(80,200,175))
        else:
          highlight_piece(cursor[0][t],cursor[1][t],(255,0,0))
        a=0
        for i in range(len(selected_piece[4])):
          if selected_piece[4][a][0]:
            fill_circle(selected_piece[4][a][1]+11,selected_piece[4][a][2]+11,4,ct)
          else:
            highlight_piece(selected_piece[4][a][1],selected_piece[4][a][2],(80,)*3)
          a+=1
      sleep(dl)
    elif selected_piece[0]:
      try:
        a=0
        dp=0
        for i in range(len(selected_piece[4])):
          if cursor[1][t] == selected_piece[4][a][2] and cursor[0][t] == selected_piece[4][a][1]:
            if selected_piece[3] == pawn and (int((selected_piece[4][a][2]-20)/23) == 0 or int((selected_piece[4][a][2]-20)/23) == 7):
              draw_string("1: 2: :3 4:",190,184)
              draw_piece(queen,turn,208,185)
              draw_piece(knight,turn,240,185)
              draw_piece(rook,turn,270,185)
              draw_piece(bishop,turn,300,185)
              a=True
              while a:
                if keydown(KEY_ONE) or keydown(KEY_TWO) or keydown(KEY_THREE) or keydown(KEY_FOUR):
                  a=False
                if keydown(KEY_ONE):
                  board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)]=[queen,turn]
                  selected_piece[3]=queen
                elif keydown(KEY_TWO):
                  board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)]=[knight,turn]
                  selected_piece[3]=knight
                elif keydown(KEY_THREE):
                  board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)]=[rook,turn]
                  selected_piece[3]=rook
                elif keydown(KEY_FOUR):
                  board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)]=[bishop,turn]
                  selected_piece[3]=bishop
              fill_rect(190,184,200,20,(255,)*3)
            else:
              board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)]=board[selected_piece[1]][selected_piece[2]]
            if rq:
              if cursor[0][t] == 138:
                board[selected_piece[1]][5]=[rook,turn]
                board[selected_piece[1]][7]=0
                fill_rect(161,(selected_piece[1]*23)+20,23,23,get_col(161,selected_piece[1])[0])
              elif cursor[0][t] == 46:
                board[selected_piece[1]][3]=[rook,turn]
                board[selected_piece[1]][0]=0
                fill_rect(0,(selected_piece[1]*23)+20,23,23,get_col(0,selected_piece[1])[0])
              else:
                rq=False
            board[selected_piece[1]][selected_piece[2]]=0
            fill_rect(last_move[0],last_move[1],19,19,get_col(int((last_move[1]-20)/23),int((last_move[0])/23))[0])
            fill_rect(last_move[2],last_move[3],19,19,get_col(int((last_move[3]-20)/23),int(last_move[2]/23))[0])
            draw_piece(last_move[4],last_move[5],last_move[2]+4,last_move[3]+3)
            fill_rect(cursor[0][t]+2,cursor[1][t]+2,19,19,(245,245,50))
            fill_rect((selected_piece[2]*23)+2,(selected_piece[1]*23)+22,19,19,(210,210,50))
            dpc=[selected_piece[3],cursor[0][t]+6,cursor[1][t]+5]
            last_move=[(selected_piece[2]*23)+2,(selected_piece[1]*23)+22,cursor[0][t]+2,cursor[1][t]+2,selected_piece[3],turn]
            if selected_piece[3] == king or selected_piece[3] == rook:
              board[int((cursor[1][t]-20)/23)][int(cursor[0][t]/23)][2]=True
          a+=1
        a=0
        if dpc != 0:
          for i in range(len(selected_piece[4])):
            c=get_col(int(selected_piece[4][a][1]/23),int((selected_piece[4][a][2]-20)/23))[0]
            if selected_piece[4][a][0]:
              fill_circle(selected_piece[4][a][1]+11,selected_piece[4][a][2]+11,4,c)
            else:
              highlight_piece(selected_piece[4][a][1],selected_piece[4][a][2],c)
            a+=1
          if rq:
            if cursor[0][t] > 100:
              draw_piece(rook,turn,121,(selected_piece[1]*23)+25)
            else:
              draw_piece(rook,turn,76,(selected_piece[1]*23)+25)
            rq=False
          draw_piece(dpc[0],turn,dpc[1],dpc[2])
          cursor[2]=0
          draw_cursor()
          cursor[2]=42
          if turn:
            turn=False
            ct=(50,)*3
          else:
            turn=True
            ct=(150,)*3
          draw_cursor()
          selected_piece[0]=False
          selected_piece[1],selected_piece[2],selected_piece[3],selected_piece[4]=42,42,42,[]
          sleep(dl)
        else:
          pass
      except:
        pass
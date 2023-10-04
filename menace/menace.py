from kandinsky import *
from ion import *
from random import *
from time import *
from matchboxes import *
training=int(input("Choisissez votre mode:\n1)Entrainer\n2)Jouer\n"))
fill_rect(55,0,222,222,(0,0,0))
grid=[[0,0,0],[0,0,0],[0,0,0]]
moves=[]
vl=[0,0,0,1,0,2,1,0,1,1,1,2,2,0,2,1,2,2,0,0,1,0,2,0,0,1,1,1,2,1,0,2,1,2,2,2,0,0,1,1,2,2,0,2,1,1,2,0]
iaturn=turn=tie=p1=p2=0
plyr=False
gx=59
gy=4
tkt=0
def rotate(g):
  ng=[[g[0][2],g[1][2],g[2][2]],[g[0][1],g[1][1],g[2][1]],[g[0][0],g[1][0],g[2][0]]]
  return ng
def mirror(g):
  ng=[[g[0][2],g[0][1],g[0][0]],[g[1][2],g[1][1],g[1][0]],[g[2][2],g[2][1],g[2][0]]]
  return ng
def rotaten(n):
  nn=0
  if n == 1:
    nn=7
  elif n == 2:
    nn=4
  elif n == 3:
    nn=1
  elif n == 4:
    nn=8
  elif n == 5:
    nn=5
  elif n == 6:
    nn=2
  elif n == 7:
    nn=9
  elif n == 8:
    nn=6
  elif n == 9:
    nn=3
  return nn
def mirrorn(n):
  nn=0
  if n == 1:
    nn=3
  elif n == 2:
    nn=2
  elif n == 3:
    nn=1
  elif n == 4:
    nn=6
  elif n == 5:
    nn=5
  elif n == 6:
    nn=4
  elif n == 7:
    nn=9
  elif n == 8:
    nn=8
  elif n == 9:
    nn=7
  return nn
def verif():
  global grid
  a=b=0
  for i in range(8):
    line=grid[vl[a]][vl[a+1]]+grid[vl[a+2]][vl[a+3]]+grid[vl[a+4]][vl[a+5]]
    if line == -3 or line == 3:
      return "win"
      b=1
    a+=6
  if b == 0:
    return "none"
def select(c):
  global gx, gy
  fill_rect(gx,gy,70,2,c);fill_rect(gx,gy,2,70,c);fill_rect(gx+68,gy,2,70,c);fill_rect(gx,gy+68,70,2,c)
def draw_grid():
  gx=59
  gy=4
  for i in range(3):
    for i in range(3):
      fill_rect(gx,gy,70,70,(255,255,255))
      gx+=72
    gx=59
    gy+=72
draw_grid();gx=131;gy=76;select((0,0,255))
sleep(0.15)
while True:
  if keydown(0) and gx > 59:
    select((255,255,255));gx-=72;select((0,0,255));sleep(0.15)
  elif keydown(3) and gx < 203:
    select((255,255,255));gx+=72;select((0,0,255));sleep(0.15)
  elif keydown(1) and gy > 4:
    select((255,255,255));gy-=72;select((0,0,255));sleep(0.15)
  elif keydown(2) and gy < 148:
    select((255,255,255));gy+=72;select((0,0,255));sleep(0.15)
  if keydown(4) and grid[int((gy-4)/72)][int((gx-59)/72)] == 0 and training == 2:
#joueur
    draw_line(gx,gy,gx+72,gy+72,(0,0,0))
    draw_line(gx+69,gy,gx,gy+69,(0,0,0))
    grid[int((gy-4)/72)][int((gx-59)/72)]=1
    plyr=True
    turn+=1
  elif training == 1:
    a=randint(0,2)
    b=randint(0,2)
    while grid[a][b] != 0:
      a=randint(0,2)
      b=randint(0,2)
    aia=a
    bia=b
    grid[a][b]=1
    draw_line((59+b*72),(4+a*72),(59+b*72)+72,(4+a*72)+72,(0,0,0))
    draw_line((59+b*72)+69,(4+a*72),(59+b*72),(4+a*72)+69,(0,0,0))
    turn+=1
    plyr=True
  if turn == 5 or verif() == "win":
    if turn == 5:
      tie+=1
      try:
        pturn0[moves[0]].append(moves[1])
        pturn1[moves[2]].append(moves[3])
        pturn2[moves[4]].append(moves[5])
        pturn3[moves[6]].append(moves[7])
      except:
        pass
    else:
      try:
        pturn0[moves[0]].remove(moves[1])
        pturn1[moves[2]].remove(moves[3])
        pturn2[moves[4]].remove(moves[5])
        pturn3[moves[6]].remove(moves[7])
      except:
        pass
      p1+=1
    turn=0
    iaturn=0
    draw_grid()
    grid=[[0,0,0],[0,0,0],[0,0,0]]
    plyr=False
    if training == 2:
      sleep(0.15)
    select((0,0,255))
#ia
  if plyr == True:
    plyr=solve=False
    c=-1
    pstn=0
    g=grid
    while solve == False:
      c+=1
      for i in range(2):
        for i in range(4):
          if iaturn == 0:
            if g == turn0[c]:
              solve=False
              p=randint(0,len(pturn0[c]))
              pstn=pturn0[c][p]
              moves.append(c)
              moves.append(pstn)
          elif iaturn == 1:
            if g == turn1[c]:
              solve=False
              p=randint(0,len(pturn1[c]))
              pstn=pturn1[c][p]
              moves.append(c)
              moves.append(pstn)
          elif iaturn == 2:
            if g == turn2[c]:
              solve=False
              p=randint(0,len(pturn2[c]))
              pstn=pturn2[c][p]
              moves.append(c)
              moves.append(pstn)
          elif iaturn == 3:
            if g == turn3[c]:
              solve=False
              p=randint(0,len(pturn3[c]))
              pstn=pturn3[c][p]
              moves.append(c)
              moves.append(pstn)
          g=rotate(g)
          pstn=rotaten(pstn)
        g=mirror(g)
        pstn=mirrorn(pstn)
    if pstn == 1:
      a=0
      b=0
    elif pstn == 2:
      a=0
      b=1
    elif pstn == 3:
      a=0
      b=2
    elif pstn == 4:
      a=1
      b=0
    elif pstn == 5:
      a=1
      b=1
    elif pstn == 6:
      a=1
      b=2
    elif pstn == 7:
      a=2
      b=0
    elif pstn == 8:
      a=2
      b=1
    elif pstn == 9:
      a=2
      b=2
    grid[a][b]=-1
    draw_circle((59+b*72)+34,(4+a*72)+34,32,(0,0,0))
    if verif() == "win" or turn == 5:
      if turn == 5:
        tie+=1
        try:
          pturn0[moves[0]].append(moves[1])
          pturn1[moves[2]].append(moves[3])
          pturn2[moves[4]].append(moves[5])
          pturn3[moves[6]].append(moves[7])
        except:
          pass
      else:
        try:
          for i in range(3):
            pturn0[moves[0]].append(moves[1])
          for i in range(3):
            pturn1[moves[2]].append(moves[3])
          for i in range(3):
            pturn2[moves[4]].append(moves[5])
          for i in range(3):
            pturn3[moves[6]].append(moves[7])
        except:
          pass
        p2+=1
      turn=0
      iaturn=0
      draw_grid()
      grid=[[0,0,0],[0,0,0],[0,0,0]]
      if training == 2:
        sleep(0.15)
      select((0,0,255))
  draw_string(str(tie),0,0)
  draw_string(str(p1),0,20)
  draw_string(str(p2),0,40)
  try:
    draw_string(str(round(tie/((p1+p2+tie)/100)))+"%",0,60)
    draw_string(str(round(p2/((p1+p2+tie)/100)))+"%",0,80)
  except:
    pass
#Machine Edcable Noughts And Crosses Engine for Numworks
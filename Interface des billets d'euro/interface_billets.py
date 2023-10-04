from kandinsky import *
from billets import *
from ion import *
from time import *
d_press=u_press=shift=s=stt=False
lbl=[5,10,20,50,100,200,500]
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
pays_emetteur=["ERROR","ERROR","Lettonie","Estonie","Slovaquie","Malte","Chypre","Slovénie","ERROR","Royaume-Uni","Suède","Finland","Portugal","Autriche","ERROR","Pays-Bas","ERROR","Luxembourg","Italie","Irlande","France","Espagne","Danemark","Allemagne","Grèce","Belgique"]
imprimeur=[["Banque d'Angleterre","Londre","Royaume-Uni"],["ERROR"],["Papetrie de Tumba","Tumba","Suède"],["Setec Oy","Vantaa","Finland"],["F.-C. Oberthur","Chantepie","France"],["Oesterreichische Banknoten-und Sicherheitsdruck GmbH","Vienne","Autriche"],["Johan Enshede & Zn","Haarlem","Pays-Bas"],["De La Rue","Gateshead","Royaume-Uni"],["ERROR"],["Banque d'Italie","Rome","Italie"],["Banque centrale d'Irlande","Dublin","Irlande"],["Banque de France","Chamalières","France"],["Maison royale de la Monnaie","Madride","Espagne"],["Banque de Grèce","Athènes","Grèce"],["ERROR"],["Giesecke & Devrient","Leipzig","Allemagne"],["ERROR"],["Imprimerie fédérale","Berlin","Allemagne"],["Banque nationale du Danemark","Copenhague","Danemark"],["Banque nationale de Belgique","Bruxelles","Belgique"],["Valora","Carregado","Portugal"],["ERROR"],["ERROR"],["ERROR"],["ERROR"],["ERROR"],]
imprimeur_europe=[["ERROR"],["ERROR"],["ERROR"],["Polska Wytwórnia Papierów Wartościowych","Varsovie","Pologne"],["Oberthur Fiduciaire","Chantepie","France"],["Oberthur Fiduciaire","Sofia","Bulgarie"],["ERROR"],["De La Rue Currency","Loughton","Royaume-Uni"],["ERROR"],["De La Rue Currency","Gateshead","Royaume-Uni"],["ERROR"],["ERROR"],["Valora","Carregado","Portugal"],["Oesterreichische Banknoten-und Sicherheitsdruck GmbH","Vienne","Autriche"],["ERROR"],["Johan Enshede & Zn","Haarlem","Pays-Bas"],["ERROR"],["Imprimerie fédérale","Berlin","Allemagne"],["Banque d'Italie","Rome","Italie"],["Banque centrale d'Irlande","Dublin","Irlande"],["Banque de France","Chamalières","France"],["Maison royale de la monnaie","Madrid","Espagne"],["Giesecke & Devrient","Leipzig","Allemagne"],["Giesecke & Devrient","Mucnich","Allemagne"],["Banque de Grèce","Athènes","Grèce"],["Banque nationale de Belgique","Bruxelles","Belgique"]]
pstn=0
y=5
def lton(l):
  c=0
  while l != alphabet[c]:
    c+=1
  return c
def total():
  c=total=0
  for i in range(len(data)):
    try:
      total+=int(data[c][0])
    except:
      pass
    c+=1
  return total
def maxb():
  b=c=e=0
  a=[0,""]
  for i in range(len(data)):
    d=data[e][4]
    b=1
    c=e
    try:
      while data[c+1][4] == d:
        b+=1
        c+=1
    except:
      pass
    if b > a[0]:
      a=[b,data[e][4]]
    e+=1
  return a
def count_b():
  c=0
  billets=[0,0,0,0,0,0,0]
  for i in range(len(data)):
    cb=0
    try:
      while int(data[c][0]) != lbl[cb]:
        cb+=1
      billets[cb]+=1
    except:
      pass
    c+=1
  return billets
def draw(y,s):
  global stt
  n=0
  fill_rect(0,0,320,240,(255,255,255))
  if stt == True:
    fill_rect(0,0,320,5,(0,0,0))
    fill_rect(0,217,320,5,(0,0,0))
    draw_string("Statistiques",100,10)
    draw_string("Total: "+str(total()),10,50)
    draw_string("Moyenne: "+str(round(total()/len(data),2)),10,70)
    billets=count_b()
    draw_string("Details:",212,50)
    draw_string("5E:  "+str(billets[0]),217,70)
    draw_string("10E: "+str(billets[1]),217,90)
    draw_string("20E: "+str(billets[2]),217,110)
    draw_string("50E: "+str(billets[3]),217,130)
    draw_string("100E:"+str(billets[4]),217,150)
    draw_string("200E:"+str(billets[5]),217,170)
    draw_string("500E:"+str(billets[6]),217,190)
    maxbi=maxb()
    draw_string("Best: "+str(maxbi[1]+"("+str(maxbi[0])+")"),10,90)
    billets_prct=[[billets[0],(204,204,204)],[billets[1],(255,153,153)],[billets[2],(153,204,255)],[billets[3],(255,153,51)],[billets[4],(140,214,83)],[billets[5],(255,204,51)],[billets[6],(204,153,204)]]
    by=50
    c=0
    ly=70
    for i in range(7):
      prct=int(round((billets_prct[c][0]/(len(data)/100)*1.6),0))
      fill_rect(210,ly,5,20,billets_prct[c][1])
      fill_rect(305,by,15,prct,billets_prct[c][1])
      c+=1
      by+=prct
      ly+=20
  elif s == 0:
    for i in range(len(data)):
      fill_rect(0,y-5,320,5,(0,0,0))
      draw_string(str(n),5,y+10)
      draw_string("Valeur:"+data[n][0],70,y)
      draw_string("Impr:"+data[n][1],180,y)
      y+=20
      draw_string("Id:"+data[n][2],70,y)
      fill_rect(60,y-20,5,40,(96, 160, 240))
      y+=25
      n+=1
    fill_rect(0,y-5,320,5,(0,0,0))
  elif s == 1:
    for i in range(len(data)):
      fill_rect(0,y-5,320,5,(0,0,0))
      draw_string(str(n),5,y+10)
      draw_string("Loc:"+data[n][3],70,y)
      y+=20
      draw_string("Date:"+data[n][4],70,y)
      fill_rect(60,y-20,5,40,(96, 160, 240))
      y+=25
      n+=1
    fill_rect(0,y-5,320,5,(0,0,0))
draw(y,s)
while True:
  if keydown(KEY_UP) and y < 5:
    if shift:
      y=-40
      shift=False
    y+=45
    draw(y,s)
    if u_press == False:
      sleep(0.1)
    if keydown(KEY_UP):
      u_press=True
    else:
      u_press=False
  if keydown(KEY_DOWN) and ((y-5)/45) > (len(data)-2*len(data))+1:
    if shift:
      y=((len(data)*45)*-1)+95
      shift=False
    y-=45
    draw(y,s)
    if d_press == False:
      sleep(0.1)
    if keydown(KEY_DOWN):
      d_press=True
    else:
      d_press=False
  if keydown(12):
    if shift == False:
      shift=True
    else:
      shift=False
    sleep(0.3)
  if keydown(1):
    if s > 0:
      s+=1
    else:
      s=4
  if keydown(4):
    if s < 4:
      s+=1
    else:
      s=0
    draw(y,s)
    sleep(0.15)
  if keydown(13):
    if stt == False:
      stt=True
    else:
      stt=False
    draw(y,s)
    sleep(0.15)
_G='B2B x '
_F='yellow'
_E='purple'
_D='orange'
_C='red'
_B=False
_A=True
from kandinsky import*
from random import*
from ion import*
from ion import keydown as kd
def f_r(a,b,c,d,e):
	fill_rect(a,b,c,d,e)
def d_s(a,b,c):
	draw_string(a,b,c)
arr=[5,0]
td=[39,0]
das=[1,0]
q_s=5
q_m=0
sds=_A
lvl=[0,10]
grav=[300,.65,300]
lock=[100,100]
lm=[0,0,0,0]
let=['i','t','j','l','s','z','o']
que=[0,1,2,3,4,5,6]
pc=score=b2b=0
drp=[50,0]
hd=_B
h=_A
lmr=_B
wc=lic=0
olds=pie=[0,4,0,0]
pcs=[[[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],[[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]],[[[0,1,0],[1,1,1],[0,0,0]],[[0,1,0],[0,1,1],[0,1,0]],[[0,0,0],[1,1,1],[0,1,0]],[[0,1,0],[1,1,0],[0,1,0]]],[[[1,0,0],[1,1,1],[0,0,0]],[[0,1,1],[0,1,0],[0,1,0]],[[0,0,0],[1,1,1],[0,0,1]],[[0,1,0],[0,1,0],[1,1,0]]],[[[0,0,1],[1,1,1],[0,0,0]],[[0,1,0],[0,1,0],[0,1,1]],[[0,0,0],[1,1,1],[1,0,0]],[[1,1,0],[0,1,0],[0,1,0]]],[[[0,1,1],[1,1,0],[0,0,0]],[[0,1,0],[0,1,1],[0,0,1]],[[0,0,0],[0,1,1],[1,1,0]],[[1,0,0],[1,1,0],[0,1,0]]],[[[1,1,0],[0,1,1],[0,0,0]],[[0,0,1],[0,1,1],[0,1,0]],[[0,0,0],[1,1,0],[0,1,1]],[[0,1,0],[1,1,0],[1,0,0]]],[[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]]]
ps=[0,4,2,3,0,4,1,2,0,3,1,3,0,3,0,2,0,3,1,3,0,3,0,2,0,3,1,3,0,3,0,2,0,3,1,3,0,3,0,2,0,3,1,3,0,3,0,2,1,3,1,3,1,3,1,3,6]
tb0=[[0,0,-1,0,-1,-1,0,2,-1,2],[0,0,1,0,1,1,0,-2,1,-2],[0,0,1,0,1,1,0,-2,1,-2],[0,0,-1,0,-1,-1,0,1,-1,2],[0,0,1,0,1,-1,0,2,1,2],[0,0,-1,0,-1,1,0,-2,-1,-2],[0,0,-1,0,-1,1,0,-2,-1,-2],[0,0,1,0,1,-1,0,2,1,2],[0,0,-2,0,1,0,-2,1,1,-2],[0,0,2,0,-1,0,2,-1,-1,2],[0,0,-1,0,2,0,-1,-2,2,1],[0,0,1,0,-2,0,1,2,-2,-1],[0,0,2,0,-1,0,2,-1,-1,2],[0,0,-2,0,1,0,-2,1,1,-2],[0,0,1,0,-2,0,1,2,-2,-1],[0,0,-1,0,2,0,-1,-2,2,1]]
tb1=[[0,0,0,-1,1,-1,-1,-1,1,0,-1,0],[0,0,1,0,1,-2,1,-1,0,-2,0,-1],[0,0,0,1,-1,1,1,1,-1,0,1,0],[0,0,-1,0,-1,-2,-1,-1,0,-2,0,-1]]
board=[[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]]
f_r(0,0,320,223,(150,)*3)
f_r(77,0,95,225,(100,)*3)
f_r(80,0,89,219,(150,)*3)
f_r(80,39,89,1,_D)
def d_b():
	c=['cyan',_E,'blue',_D,'green',_C,_F,(255,)*3,0,(30,)*3]
	for n in range(0,24):
		for i in range(3,13):f_r(i*9+53,n*9+4,8,8,c[board[n][i]])
d_b()
def d_t(t,x,y,o,e):
	if e:c,b=['cyan',_E,'blue',_D,'green',_C,_F],t
	else:c,b=[(30,)*3],0
	x,y=x*9+53,y*9+4
	try:
		for a in range(len(pcs[t][o])):
			for i in range(len(pcs[t][o][a])):
				if pcs[t][o][a][i]==1:f_r(x+9*i,y+9*a,8,8,c[b])
	except Exception as e:print(e)
def n_b():global que;bag=[0,1,2,3,4,5,6];bag=sorted(bag,key=lambda x:randint(0,1));que+=bag
def n_t():
	global pie,drp,lm,h
	if sds:f_r((ps[pie[3]*8+pie[2]*2]+ps[56])*9+52,40,1,179,(150,)*3);f_r((ps[pie[3]*8+pie[2]*2+1]+ps[56])*9+52,40,1,179,(150,)*3);f_r((ps[que[0]*8]+6)*9+52,40,1,179,_C);f_r((ps[que[0]*8+1]+6)*9+52,40,1,179,_C);ps[56]=6
	pie=[6,4,0,que[0]];lm=pie;d_t(pie[3],pie[0],pie[1],pie[2],_A);drp[1]=0;que.remove(que[0])
	if len(que)==7:n_b()
	x,y=188,32
	if q_m==1:d_s(let[que[0]]+let[que[1]]+let[que[2]]+let[que[3]]+let[que[4]],x,y)
	else:
		f_r(175,20,50,130,(150,)*3)
		for q in range(q_s):d_t(que[q],14,2+q*3,0,_A)
	h=_A;f_r(175,150,150,80,(150,)*3)
def move(x,y,e):
	global lmr;check=_A
	try:
		for i in range(len(pcs[pie[3]][pie[2]])):
			for j in range(len(pcs[pie[3]][pie[2]])):
				if board[pie[1]+i+y][pie[0]+j+x]!=9 and pcs[pie[3]][pie[2]][i][j]==1:check=_B
	except:check=_B
	if check:
		if e:d_t(pie[3],pie[0],pie[1],pie[2],_B);lmr=_B
		pie[0]=pie[0]+x;pie[1]=pie[1]+y
for i in range(4):d_t(0,-2,2-i,0,_B)
d_s('Lines:',5,60)
d_s(str(lic),5,78)
d_s('Lvl:'+str(lvl[0]),5,40)
d_s('Score:',179,2)
d_s(str(score),239,2)
n_b()
n_b()
n_t()
while _A:
	if not kd(45)and not kd(1):hd=_B
	if lock[1]>0:
		a=pie[1];move(0,1,_B)
		if a==pie[1]:lock[1]-=1
		else:move(0,-1,_B)
	if(kd(45)or kd(1))and not hd or lock[1]==0:
		lock[1]=lock[0];hd=_A
		for k in range(24):
			a=pie[1];move(0,1,_B)
			if a!=pie[1]:score+=2
		c=0
		for i in range(len(pcs[pie[3]][pie[2]])):
			for j in range(len(pcs[pie[3]][pie[2]])):
				if pcs[pie[3]][pie[2]][i][j]==1:board[pie[1]+i][pie[0]+j]=pie[3]
				elif pie[3]==1 and lmr and(i==0 and j==0 or i==2 and j==0 or i==0 and j==2 or i==2 and j==2)and board[pie[1]+i][pie[0]+j]!=9:c+=1
		l=[]
		for i in range(24):
			a=0
			try:
				while board[i][a]!=9:a+=1
			except:l.append(i)
		lmr=_B
		if len(l)>0:
			for i in range(len(l)):board.remove(board[l[i]]);board.insert(0,[7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7]);lic+=1
			n_t();wc+=1;score+=50*(wc-1);d_s(str(lic),5,78)
			if int(lic/lvl[1])>lvl[0]:lvl[0]=int(lic/lvl[1]);grav[0]=int(grav[0]*grav[1]);d_s(str(lvl[0]),45,40)
			if len(l)==1:
				d_s('Single - '+str(wc),175,180);score+=100
				if c>2:
					score+=700;b2b+=1
					if b2b!=0:score+400
				else:b2b=0
			elif len(l)==2:
				d_s('Double - '+str(wc),175,180);score+=300
				if c>2:
					score+=900;b2b+=1
					if b2b!=0:score+600
				else:b2b=0
			elif len(l)==3:
				d_s('Triple - '+str(wc),175,180);score+=500
				if c>2:
					score+=1100;b2b+=1
					if b2b!=0:score+800
				else:b2b=0
			else:
				d_s('TETRIS! - '+str(wc),175,180);score+=800;b2b+=1
				if b2b!=0:score+400
			if board.count([7,7,7,9,9,9,9,9,9,9,9,9,9,7,7,7])==24:pc+=1;d_s('PERFECT CLEAR!',175,200);d_s('PC: '+str(pc),5,98);score+=3500
			if b2b>1:d_s(_G+str(b2b),175,198)
		else:wc=0;n_t()
		if c>2:
			d_s('T-SPIN',175,162)
			if len(l)==0:
				d_s('Mini',175,180);score+=400;b2b+=1
				if b2b>1:score+200;d_s(_G+str(b2b),175,198)
		d_b();d_s(str(score),239,2)
	if kd(2)or kd(51):
		if das[1]==das[0]:
			a=pie[1];move(0,1,_A);das[1]=0
			if a!=pie[1]:score+=1;d_s(str(score),239,2)
		else:das[1]+=1
	else:das[1]=das[0]
	if kd(0)or kd(50):
		if arr[1]==arr[0]:move(-1,0,_A);arr[1]=0
		else:arr[1]+=1
	elif kd(3)or kd(52):
		if arr[1]==arr[0]:move(1,0,_A);arr[1]=0
		else:arr[1]+=1
	else:arr[1]=arr[0]
	if(kd(3)or kd(52)or kd(0)or kd(50))and sds:
		c=(150,)*3
		for i in range(2):f_r((ps[pie[3]*8+pie[2]*2]+ps[56])*9+52,40,1,179,c);f_r((ps[pie[3]*8+pie[2]*2+1]+ps[56])*9+52,40,1,179,c);ps[56]=pie[0];c=_C
	if kd(30)or kd(31)or kd(32):
		if td[1]==td[0]:
			td[1]=0
			if sds:f_r((ps[pie[3]*8+pie[2]*2]+ps[56])*9+52,40,1,179,(150,)*3);f_r((ps[pie[3]*8+pie[2]*2+1]+ps[56])*9+52,40,1,179,(150,)*3)
			d_t(pie[3],pie[0],pie[1],pie[2],_B)
			if kd(30):
				check=pie[2];ret=pie[2]
				if pie[2]<2:pie[2]+=2
				else:pie[2]-=2
				invalid=_A;c=-1
				try:
					while invalid:
						invalid=_B;c+=1
						for i in range(len(pcs[pie[3]][pie[2]])):
							for j in range(len(pcs[pie[3]][pie[2]])):
								if board[pie[1]+i+tb1[check][c*2+1]][pie[0]+j+tb1[check][c*2]]!=9 and pcs[pie[3]][pie[2]][i][j]==1 and not invalid:invalid=_A
					pie[1]+=tb1[check][c*2+1];pie[0]+=tb1[check][c*2];lmr=_A
				except:pie[2]=ret
			if kd(31):
				check=pie[2]*2-1;ret=pie[2]
				if pie[2]!=0:pie[2]-=1
				else:check=7;pie[2]=3
				invalid=_A;c=-1
				if pie[3]==0:check+=8
				try:
					while invalid:
						invalid=_B;c+=1
						for i in range(len(pcs[pie[3]][pie[2]])):
							for j in range(len(pcs[pie[3]][pie[2]])):
								if board[pie[1]+i+tb0[check][c*2+1]][pie[0]+j+tb0[check][c*2]]!=9 and pcs[pie[3]][pie[2]][i][j]==1 and not invalid:invalid=_A
					pie[1]+=tb0[check][c*2+1];pie[0]+=tb0[check][c*2];lmr=_A
				except:pie[2]=ret
			if kd(32):
				check=pie[2]*2;ret=pie[2];ret=pie[2]
				if pie[2]!=3:pie[2]+=1
				else:pie[2]=0;check=6
				invalid=_A;c=-1
				if pie[3]==0:check+=8
				try:
					while invalid:
						invalid=_B;c+=1
						for i in range(len(pcs[pie[3]][pie[2]])):
							for j in range(len(pcs[pie[3]][pie[2]])):
								if board[pie[1]+i+tb0[check][c*2+1]][pie[0]+j+tb0[check][c*2]]!=9 and pcs[pie[3]][pie[2]][i][j]==1 and not invalid:invalid=_A
					pie[1]+=tb0[check][c*2+1];pie[0]+=tb0[check][c*2];lmr=_A
				except:pie[2]=ret
			if sds:ps[56]=pie[0];f_r((ps[pie[3]*8+pie[2]*2]+ps[56])*9+52,40,1,179,_C);f_r((ps[pie[3]*8+pie[2]*2+1]+ps[56])*9+52,40,1,179,_C)
		else:td[1]+=1
	else:td[1]=td[0]
	if kd(33) and h:
		d_t(pie[3],pie[0],pie[1],pie[2],_B)
		try:d_t(hold[3],-2,1,hold[2],_B);pie,hold=[6,4,0,hold[3]],[0,0,0,pie[3]]
		except:hold=[0,0,0,pie[3]];n_t()
		d_t(hold[3],-2,1,hold[2],_A);h=_B
	if grav[2]>0 and grav!=-1:grav[2]-=1
	if get_keys!=0 or grav[2]==0:
		if grav[2]==0:
			grav[2]=grav[0];move(0,1,_A)
			if grav[2]==0:
				for i in range(23):move(0,1,_B)
		d_t(pie[3],pie[0],pie[1],pie[2],_A)
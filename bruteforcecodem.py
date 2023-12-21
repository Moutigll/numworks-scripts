import copy
import os
from time import *
letters=[[[0,1,0],[1,0,1],[1,0,1]],[[1,1,0],[1,1,0],[1,1,0]],[[0,1,0],[1,0,0],[0,1,0]],[[1,1,0],[1,0,1],[1,1,0]],[[1,1,1],[1,0,0],[1,1,1]],[[1,1,1],[1,0,0],[1,0,0]],[[0,1,0],[1,1,1],[1,0,1]],[[1,0,1],[1,1,1],[1,0,1]],[[1,0,0],[1,0,0],[0,0,0]],[[1,1,0],[0,1,0],[0,1,0]],[[1,0,1],[1,1,0],[1,1,0]],[[1,0,0],[1,0,0],[1,1,0]],[[1,0,1],[1,1,1],[1,1,1]],[[1,0,0],[1,1,1],[0,0,0]],[[0,1,0],[1,0,1],[0,1,0]],[[1,1,0],[1,1,0],[1,0,0]],[[0,1,0],[1,0,1],[0,1,1]],[[1,1,0],[1,1,0],[1,0,1]],[[0,1,0],[1,0,0],[1,1,0]],[[1,1,1],[0,1,0],[0,1,0]],[[1,0,1],[1,0,1],[0,1,0]],[[0,0,0],[1,0,1],[0,1,0]],[[0,0,0],[1,1,1],[0,1,0]],[[1,0,1],[0,1,0],[1,0,1]],[[1,0,1],[0,1,0],[0,1,0]],[[1,1,0],[1,0,0],[1,1,0]],[[1,1,1],[0,0,0],[0,0,0]]]
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
sentence=list(input("Rentrez la phrase à analyser:\n"))
a=ls=0
msg=[]
for i in range(len(sentence)):
    sentence[i]=int(sentence[i])
while a < len(sentence):
    a+=sentence[a]+1
    ls+=1
print("Il y'a " + str(ls) + " caractères dans la phrase cryptée.")
output=""
def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end
q=r=t=0
s=-1
decrypted=""
start=estart=monotonic()
total=end=start
for key in permute(["1","2","3","4","5","6","7","8","9",]):
    r=q/3628.8
    if round(r,0) > s:
        pr="█"*int(round(r,0))
        prr="-"*int(100-round(r,0))
        s=round(r,0)
        etime=round(monotonic()-estart)*int(100-round(r,0))
        estart=monotonic()
        os.system('CLS')
        print("Progress: [" + pr + prr + "] " + str(round(r,0)) + "% Complete, Estimated remaining time: " + str(etime) + "s\nIl y'a " + str(ls) + " caractères dans la phrase cryptée.")
        print(msg)
    isentence=copy.copy(sentence)
    b=key
    tkey=[]
    a=0
    for i in range(3):
        for j in range(3):
            tkey.append([int(b[a]),j,i])
            a+=1
    a=True
    out=""
    a=True
    while a:
        try:
            letter=[]
            for i in range(sentence[0]):
                sentence.pop(0)
                letter.append(sentence[0])
            sentence.pop(0)
            for i in range(len(letters)):
                b=True
                lco=[]
                for j in range(len(letter)):
                    for k in range(9):
                        if tkey[k][0] == letter[j]:
                            x,y=tkey[k][1],tkey[k][2]
                            lco.append([x,y])
                    if letters[i][y][x] != 1:
                        b=False
                for j in range(3):
                    for k in range(3):
                        if letters[i][j][k] == 1:
                            c=False
                            for l in range(len(lco)):
                                if k == lco[l][0] and j == lco[l][1]:
                                    c=True
                            if not c:
                                b=False
                if b:
                    out+=str(alphabet[i])
                    if len(list(out)) > ls-int(round(ls/10)):
                        decrypted+="Key: " + str(key) + "\nMessage: " + str(out) + "\n\n"
                        t+=1
                        try:
                            test=msg.index(out)
                        except:
                            msg.append(key)
                            msg.append(out)
        except:
            a=False
    sentence=isentence
    q+=1
print("Successfully completed in " + str(round(monotonic()-start,0)) + "s, " + str(t) + " solutions were found !")
print(decrypted)
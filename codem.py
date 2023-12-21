from random import *
letters=[[[0,1,0],[1,0,1],[1,0,1]],[[1,1,0],[1,1,0],[1,1,0]],[[0,1,0],[1,0,0],[0,1,0]],[[1,1,0],[1,0,1],[1,1,0]]]
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
inp=list(input("Rentrez la clé de chiffrement:\n"))
sentence=list(input("Rentrez la phrase à analyser:\n"))
mode=int(input("Voulez vous décoder cette phrase (0) ou l'encoder(1)?\n"))
b=0
key=[]
out=""
if mode == 1:
    for i in range(3):
        a=[]
        for j in range(3):
            a.append(inp[b])
            b+=1
        key.append(a)
    for i in range(len(sentence)):
        letter=letters[alphabet.index(sentence[i])]
        a=b=0
        letterenc=[]
        for j in range(3):
            for k in range(3):
                if letter[b][a] == 1:
                    letterenc.append(key[b][a])
                a+=1
            a=0
            b+=1
        out+=str(len(letterenc))
        for j in range(len(letterenc)):
            a=randint(0,len(letterenc)-1)
            out+=str(letterenc[a])
            letterenc.remove(letterenc[a])
else:
    for i in range(len(sentence)):
        sentence[i]=int(sentence[i])
    a=0
    for i in range(3):
        for j in range(3):
            key.append([int(inp[a]),j,i])
            a+=1
    print(key)
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
                        if key[k][0] == letter[j]:
                            x,y=key[k][1],key[k][2]
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
        except:
            a=False
print(out)
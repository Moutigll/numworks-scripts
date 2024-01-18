def convert():
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    a=(input("Entrez le nombre à convertir:\n"))
    b=int(input("Entrez la base d'origine:\n"))
    c=int(input("Entrez la base cible:\n"))
    if b != 10:
        a=list(a)
        r=0
        for i in range(len(a)):
            try:
                d=int(a[i])
            except:
                d=10+l.index(a[i])
            r+=d*(b**(len(a)-i))
        r=int(r/b)
    else:
        r=int(a)
    res=[r]
    if c != 10:
        res=[]
        while r+1 > c:
            rem=r%c
            r=r//c
            if rem > 9:
                rem=l[rem-10]
            res.insert(0,rem)
        res.insert(0,r)
    pr=""
    for i in range(len(res)):
        pr+=str(res[i])
    print(pr)
convert()
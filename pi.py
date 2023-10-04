pi=[1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,5,9,2,3,0,7,8,1,6,4,0,6,2,8,6,2,0,8,9,9,8,6,2,8,0,3,4,8,2,5,3,4,2,1,1,7,0,6,7,9,8,2,1,4,8,0,8,6,5,1,3,2,8,2,3,0,6,6,4,7,0,9,3,8,4,4,6,0,9,5,5,0,5,8,2,2,3,1,7,2,5,3,5,9,4,0,8,1,2,8,0,0,0,0]
count=0
show="3."
err=False
for a in range(len(pi)):
  print(show)
  print(str(pi[count-4]) + str(pi[count-3]) + str(pi[count-2]) + str(pi[count-1]) + "(" + str(count) + ")")
  try:
    add=list(input("").strip())
    countb=0
    for i in range(len(add)):
      if int(add[countb]) == pi[count]:
        show+=add[countb]
        count+=1
        countb+=1
  except:
    print("Erreur !")
#############################
#                           #
#    Pi quizz v1.0          #
#    -------------          #
#      By Moutig            #
#                           #
#############################
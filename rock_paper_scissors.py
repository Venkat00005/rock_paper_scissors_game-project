import random
computer = 0
you = 0
USER = input("enter player name:")
l = ["rock","paper","scissors"] 
while computer<3 and you<3:            #CAN MODIFY THE TOTAL POINTS NEEDED TO WIN IN THE GAME HERE

  user=input("choose your choice rock,paper,scissors:\n") #USER INPUT
  user = user.lower()
  random.shuffle(l)                                     #COMPUTER'S RANDOM INPUT

  if l[1]=="rock" and user=='paper':
    you=you+1
    print("computer=",l[1])                   #USER WILL GET POINT HERE
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="rock" and user=='scissors':
    computer=computer+1
    print("computer=",l[1])                   #COMPUTER SCORED POINT HERE
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="rock" and user=='rock':
    print("computer=",l[1])
    print("computer=", computer)             
    print(USER,"=",you)
    continue                                  #COMPUTER AND USER CHOSE THE SAME OPTION

  elif l[1]=="paper" and user=='rock':
    computer=computer+1
    print("computer=",l[1])                   #COMPUTER SCORED
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="paper" and user=='paper':
    print("computer=",l[1])
    print("computer=", computer)
    print(USER,"=",you)  
    continue                                  #TIE

  elif l[1]=="paper" and user=='scissors':
    you=you+1                                 #USER SCORED
    print("computer=",l[1])
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="scissors" and user=='rock':
    you=you+1                                #USER SCORED
    print("computer=",l[1])
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="scissors" and user=='paper':
    computer=computer+1                      #COMPUTER SCORED
    print("computer=",l[1])
    print("computer=", computer)
    print(USER,"=",you)

  elif l[1]=="scissors" and user=='scissors': 
    print("computer=",l[1])
    print("computer=", computer)
    print(USER,"=",you)
    continue                                 #TIE
    
if computer==3:                               #COMPUTER WINNING CONDITION AND CAN ALSO MODIFY ACCORDINGLY
  print("computer is winner") 
else:
  print("user is winner")                     #USER WINNER
import random
computer = 0
user = 0
user_name = input("enter player name:")
computer_choice = ["rock","paper","scissors"] 
while computer<3 and user<3:            #CAN MODIFY THE TOTAL POINTS NEEDED TO WIN IN THE GAME HERE

  user_choice=input("choose your choice rock,paper,scissors:\n") #USER INPUT
  user_choice = user_choice.lower()
  random.shuffle(computer_choice)                                     #COMPUTER'S RANDOM INPUT

  if computer_choice[1]=="rock" and user_choice=='paper':
    user=user+1
    print("computer=",computer_choice[1])                   #USER WILL GET POINT HERE
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="rock" and user_choice=='scissors':
    computer=computer+1
    print("computer=",computer_choice[1])                   #COMPUTER SCORED POINT HERE
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="rock" and user_choice=='rock':
    print("computer=",computer_choice[1])
    print("computer=", computer)             
    print(user_name,"=",user)
    continue                                  #COMPUTER AND USER CHOSE THE SAME OPTION

  elif computer_choice[1]=="paper" and user_choice=='rock':
    computer=computer+1
    print("computer=",computer_choice[1])                   #COMPUTER SCORED
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="paper" and user_choice=='paper':
    print("computer=",computer_choice[1])
    print("computer=", computer)
    print(user_name,"=",user)  
    continue                                  #TIE

  elif computer_choice[1]=="paper" and user_choice=='scissors':
    user=user+1                                 #USER SCORED
    print("computer=",computer_choice[1])
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="scissors" and user_choice=='rock':
    user=user+1                                #USER SCORED
    print("computer=",computer_choice[1])
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="scissors" and user_choice=='paper':
    computer=computer+1                      #COMPUTER SCORED
    print("computer=",computer_choice[1])
    print("computer=", computer)
    print(user_name,"=",user)

  elif computer_choice[1]=="scissors" and user_choice=='scissors': 
    print("computer=",computer_choice[1])
    print("computer=", computer)
    print(user_name,"=",user)
    continue                                 #TIE
    
if computer==3:                               #COMPUTER WINNING CONDITION AND CAN ALSO MODIFY ACCORDINGLY
  print("computer is winner") 
else:
  print(user_name,"is winner")                     #USER WINNER

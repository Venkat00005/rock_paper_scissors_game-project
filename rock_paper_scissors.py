import random
import time
computer_score = 0
user_score = 0
user_name = input("enter player name:")
computer_choice = ["rock","paper","scissors"] 
print('''Lets Play!!!
| | |
| | |
| | |
V V V''')
while computer_score<3 and user_score<3:            #CAN MODIFY THE TOTAL POINTS NEEDED TO WIN IN THE GAME HERE

  user_choice=input("select your choice rock,paper,scissors:\n") #USER INPUT
  user_choice = user_choice.lower()
  random.shuffle(computer_choice)                                     #COMPUTER'S RANDOM INPUT

  if computer_choice[1]=="rock" and user_choice=='paper':
    user_score=user_score+1
    time.sleep(1)
    print("computer=",computer_choice[1])                   #USER WILL GET POINT HERE
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="rock" and user_choice=='scissors':
    computer_score=computer_score+1
    time.sleep(1)
    print("computer=",computer_choice[1])                   #COMPUTER SCORED POINT HERE
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="rock" and user_choice=='rock':
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)             
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')
    continue                                  #COMPUTER AND USER CHOSE THE SAME OPTION

  elif computer_choice[1]=="paper" and user_choice=='rock':
    computer_score=computer_score+1
    time.sleep(1)
    print("computer=",computer_choice[1])                   #COMPUTER SCORED
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="paper" and user_choice=='paper':
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)  
    print('''
| | |
| | |
| | |
V V V''')
    continue                                  #TIE

  elif computer_choice[1]=="paper" and user_choice=='scissors':
    user_score=user_score+1                                 #USER SCORED
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="scissors" and user_choice=='rock':
    user_score=user_score+1                                #USER SCORED
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="scissors" and user_choice=='paper':
    computer_score=computer_score+1                      #COMPUTER SCORED
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')

  elif computer_choice[1]=="scissors" and user_choice=='scissors': 
    time.sleep(1)
    print("computer=",computer_choice[1])
    time.sleep(2)
    print("\ncomputer score=", computer_score)
    print(user_name,"score=",user_score)
    print('''
| | |
| | |
| | |
V V V''')
    continue                                 #TIE

time.sleep(2)
if computer_score==3:                               #COMPUTER WINNING CONDITION AND CAN ALSO MODIFY ACCORDINGLY
  print("computer is winner") 
else:
  print(user_name,"is winner")                     #USER WINNER
print("Game ended, Thanks for playing")

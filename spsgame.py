import random
ch=['stone','paper','scissors']
computer= random.choice(ch)
player=''
while player not in ch:
    player=(input("enter the valid choice:stone /paper/scissors")).lower()
print(f'computer choice:{computer} | player choice:{player}')
if player==computer:
    print("it is tie!!!!!!!!!!!!!!!!!!!!")
elif ((player=='stone'and computer=='scissors') or
     ( player=='paper' and computer=='stone')or
    (player=='scissors'and computer== 'paper')):
    print("player won")
else:
    print("computer won")




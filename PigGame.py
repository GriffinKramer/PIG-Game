#PIG Game
#A pig gam I created for my Python computer science class
#Griffin Kramer
import random

playerpoints = 0
cpupoints = 0
player_turn = 0
cpu_turn = 0 
again = "yes"
ctr = 0
roll = 0

print ("Lets Play PIG!!!")
print("Player First!")

while playerpoints < 100 and cpupoints < 100:
    
    if roll == 0:
        
        roll = random.randint(1,6)
    
    if roll != 1 and (again == "yes" or again == "Yes"):
        
        player_turn = player_turn + roll
        
        print("You rolled a " + str(roll))
       
        roll = random.randint(1,6)
        
        if player_turn + playerpoints >= 100:
            
            playerpoints = player_turn + playerpoints
            
        else:
            
            again = input("Type yes to roll again or hold to stop")
        
    else:
        
        if roll == 1:
            
            player_turn = 0 
            print("You rolled a " + str(roll) + ", your turn is over!")
            roll = random.randint(1,6)
            
        else:
            
            print("You held.")
            playerpoints = playerpoints + player_turn
            player_turn = 0
            
        print("Total player points: " + str(playerpoints))
        
        cpu_hold = random.randint(1,3)
        cpuroll = random.randint(1,6)
        
        while cpuroll != 1 and (cpupoints < 100 and playerpoints < 100) and cpu_hold != 1:
           
            print("The CPU rolled a " + str(cpuroll))
            cpu_turn = cpu_turn + cpuroll
            ctr = ctr + 1
            if cpu_turn + cpupoints >= 100:
                cpupoints = cpu_turn + cpupoints
            else:
                cpuroll = random.randint(1,6)
                cpu_hold = random.randint(1,3)
            
        else:
            
            if cpupoints < 100 and playerpoints < 100:
                print("The CPU rolled a " + str(cpuroll))
                if cpuroll == 1: 

                    cpu_turn = 0 
                    print("Total CPU points: " + str(cpupoints))

                else: 

                    if ctr == 0:
                        print("The CPU rolled a " + str(cpuroll))
                        ctr = 0

                    cpu_turn = cpu_turn + cpuroll
                    cpupoints = cpupoints + cpu_turn
                    print("The CPU held.\nTotal CPU points: " + str(cpupoints)) 
                    cpu_turn = 0 
                again = "yes"
         
    
if playerpoints >= 100:
    print("You Win!")
else:
    print("The CPU Wins")
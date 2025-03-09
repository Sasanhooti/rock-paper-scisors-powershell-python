import random
optioon = ["rock", "scisors", "paper"]



def play():
    
    #score board
    user__ = 0
    pc__ = 0
    while True :
        print("  1 : rock\n ", "2 : scisors\n ", "3 : paper")
        user = input("please select an option?  :")
        while True :
            if user == "1" or user == "2" or user == "3" :
                break
            else :
                print("Invalid option. please try again")
                user = input("please select an option?  :")
                # if user == "1" or user == "2" or user == "3" :
                #     break
     
        # convert user select       
        if int(user) == 1 :
            user_select = optioon[0]
        if int(user) == 2 :
            user_select = optioon[1] 
        if int(user) == 3 :
            user_select = optioon[2]
        print("user select" , user_select)
    
        #import sasan hooti
        optins = ["rock", "scisors", "paper"]
        com_sekect = random.choice(optins)
        print("pc select" , com_sekect)
    
        # Game Rule
        if user_select == com_sekect:
            print("draw")
        
        if user_select == "rock" and com_sekect == "scisors":
            print("user win")
            user__ += 1
        if user_select == "rock" and com_sekect == "pape":
            print("pc win")
            pc__ +=1
        if user_select == "scisors" and com_sekect == "rock":
            print("pc win")
            pc__ +=1
        if user_select == "secisors" and com_sekect == "paper":
            print("user win")
            user__ += 1
        if user_select == "paper" and com_sekect == "rock":
            print("user win")
            user__ +=1 
        if user_select == "paper" and com_sekect == "scisors":
            print("pc win")
            pc__ +=1  
        
        print("--------------------")
        print(" user =" , user__)  
        print(" pc   =" , pc__) 
        if user == 3 :
            print ("you win")
            break     
        if pc__   == 3 :
            print ("you lost")
            break
        
 
play()
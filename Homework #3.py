route = False
orientation = False
size = False
Type = False
parent = 0

highway = int(input("Please enter a US Interstate Highway route number: "))

while highway < 0 or highway >= 999:
    highway = int(input("Please enter a US Interstate Highway route number: "))

while highway >= 0 and highway <= 999:
    if highway == 0:
        break
    
    if highway <= 99:
        route = True #PRIMARY
    else:
        route = False #AUX

    if route == True and highway % 2 == 0:
        orientation = True #EAST-WEST
    else:
        orientation = False #NORTH-SOUTH

    if ((orientation == True or orientation == False) and highway % 5 == 0):
        size = True #LONG-DISTANCE ARTERIAL
    else:
        size = False 

    if route == False and ((highway // 100) % 2 != 0):
        Type = True #SPUR
    else:
        Type = False #LOOP

    if (Type == True or Type == False):
        parent = highway % 100



    if (route == True and orientation == True and size == True):
        print(f"Interstate {highway} is a long-distance arterial highway oriented east-west.")
    elif(route == True and orientation == True and size == False):
        print(f"Interstate {highway} is oriented east-west.")
    elif(route == True and orientation == False and size == False):
        print(f"Interstate {highway} is oriented north-south.")
    elif route == True and orientation == False and size == True):
        print(f"Interstate {highway} is a long-distance arterial highway oriented north-south.")
    elif(route == False and Type == True):
        print(f"Interstate {highway} is a spur highway of interstate {parent}.")
    elif(route == False and Type == False):
        print(f"Interstate {highway} is a loop highway of interstate {parent}.")

    highway = int(input("Please enter a US Interstate Highway route number:"))
    
    
    


    



    
    
    
   

    

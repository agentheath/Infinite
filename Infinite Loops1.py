
while True:
    input_a = input("Do you like infinite loops?\nYes or no?\n")
    
    while True:
        if input_a.lower().startswith("y"):    
            print("Me too!!!")
        
        elif input_a.lower().startswith("n"):
            print("Too bad!!!")
        
        else:
            print("\nwut\n")
            break

#This program was created by a genius.

def infinite():
    while True:
        input_a = input("Infinite loops? y or n?")
        
        while True:
            if input_a.lower().startswith("y"):
                print("Yay!")
                
            elif input_a.lower().startswith("n"):
                print("Uh oh")
                
            else:
                print("\nwut\n")
                break
                
infinite()

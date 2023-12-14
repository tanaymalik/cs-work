#pyramid question



def word_pyramid():
    user_input = (input("do you want a 'straight' pyramid or 'reverse'")).lower()
    
    if user_input == "straight":
        for i in range(1, 10, 2):
            print(i*("*"))
    
    elif user_input == "reverse":
        for i in range(10, 1, -2):
            print(i*("*"))
    else:
        print("invalid input")        
                
word_pyramid()                
        
    
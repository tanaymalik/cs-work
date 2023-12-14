#importing a library inflect to convert the integers to strings like "forty five"
import inflect
p = inflect.engine()


def check_input_type(user_input):
    
    #checking whether they are strings
    if user_input.isalpha():
        print("The input is a string.")
        if user_input.isupper():
            print(f"The character {user_input} is uppercase.")
        elif user_input.islower():
                print(f"The character {user_input} is lowercase.")
        else:
                print(f"The character {user_input} is neither uppercase nor lowercase.")        

    #checking whether they are numbers    
    elif user_input.isdigit():
        print("The input is a number.")
        in_words = p.number_to_words(int(user_input))
        print(f"the number {user_input} in words is {in_words}.")            
        
     #checking for special characters   
    elif not user_input.isalnum():
        return "The input contains special characters."
    
    else:
        return "The input is a combination of characters."


user_input = input("Enter something: ")
check_input_type(user_input)

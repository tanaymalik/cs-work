def validate_name(name):
    if any(char.isdigit() or not char.isalpha() for char in name):
        raise ValueError("Invalid characters in the name. Please enter a valid name.")

def main():
    try:
        user_name = input("Enter your name: ")
        validate_name(user_name)
        print(f"Hello, {user_name}! Your name is valid.")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

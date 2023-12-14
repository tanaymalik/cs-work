def find_frequency(input_string, char):
    frequency = input_string.count(char)
    print(f"The frequency of '{char}' in the string is: {frequency}")

def replace_character(input_string, old_char, new_char):
    modified_string = input_string.replace(old_char, new_char)
    print(f"After replacing '{old_char}' with '{new_char}': {modified_string}")

def remove_first_occurrence(input_string, char):
    index = input_string.find(char)
    if index != -1:
        modified_string = input_string[:index] + input_string[index + 1:]
        print(f"After removing the first occurrence of '{char}': {modified_string}")
    else:
        print(f"'{char}' not found in the string.")

def remove_all_occurrences(input_string, char):
    modified_string = input_string.replace(char, "")
    print(f"After removing all occurrences of '{char}': {modified_string}")

# Example usage:
input_str = input("Enter a string: ")
character_to_operate = input("Enter a character to perform operations: ")

find_frequency(input_str, character_to_operate)
replace_character(input_str, character_to_operate, '_')
remove_first_occurrence(input_str, character_to_operate)
remove_all_occurrences(input_str, character_to_operate)

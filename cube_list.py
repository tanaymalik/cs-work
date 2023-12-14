#using a for loop
def cubes_of_even_for_loop(input_list):
    result = []
    for element in input_list:
        if isinstance(element, int) and element % 2 == 0:
            result.append(element**3)
    return result



def cubes_of_even_list_comprehension(input_list):
    return [element**3 for element in input_list if isinstance(element, int) and element % 2 == 0] 


# Example usage:
user_input = input("Enter numbers separated by spaces: ")
input_list = [int(x) for x in user_input.split()]
# result_for_loop = cubes_of_even_for_loop(input_list)
# result_for_list_comprehension = cubes_of_even_list_comprehension(input_list)
# print(result_for_loop)








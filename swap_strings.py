

def swap_strings(str, str2, n):
    swapped_str1 = str2[:n] + str1[n:]
    swapped_str2 = str1[:n] + str2[n:]
    return swapped_str1, swapped_str2



str1 = input("give string1")
str2 = input("give string 2")
n = int(input("how many digits do you want to swap between the two strings"))

result = swap_strings(str1, str2, n)
print(result)
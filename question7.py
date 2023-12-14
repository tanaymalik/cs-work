str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

def find_occurrences(s1, s2):
    indices = []
    for i in range(len(s1)):
        if s1[i:i+len(s2)] == s2:
            indices.append(i)
    return indices if indices else -1

result = find_occurrences(str1, str2)
print(f"The occurrences of '{str1}' in '{str2}' start at indices: {result}")

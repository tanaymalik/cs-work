t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)

half = int(len(t1)/2)
half1 = t1[:half]
half2 = t1 [half:]

print(half1)
print(half2)

evenTuple = tuple([i for i in t1 if i%2 == 0])

print(evenTuple)
concatenatedTuple = t1+t2
print(concatenatedTuple)
maxValue = max (concatenatedTuple)
minValue = min(concatenatedTuple)
print(maxValue, minValue)
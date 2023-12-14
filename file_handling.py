f1 = open("/home/anish/Documents/test.txt","r")
data = f1.read()

characterCount = len(data)
wordCount = data.count(" ") + data.count("\n")
lineCount = data.count("\n")

dict1 = {i:data.count(i) for i in data if i.isalpha() or i.isdigit() or i in "!@#$%^&*()~`_+-={}|[]\:;<>?,./"}

reverseFile = data[::-1]

evenLines = ""
oddLines = ""

count = 0

File1 = open("/home/anish/Documents/File1.txt","w")
File2 = open("/home/anish/Documents/File2.txt","w")

for i in data:
    if i == "\n":
        count += 1

    if count%2 != 0:
        evenLines += i
    else:
        oddLines += i

File1.write(evenLines)
File2.write(oddLines)

File1.close()
File2.close()
f1.close()

File1 = open("/home/anish/Documents/File1.txt","r")
File2 = open("/home/anish/Documents/File2.txt","r")

print("Original File:-" + "\n" + data)
print("File1:-" + File1.read())
print("File2:-" + "\n" + File2.read())

File1.close()
File2.close()
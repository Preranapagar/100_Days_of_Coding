
#loops in python

#for loop

print("loop demo 1:")
for i in range(5):
    print(i)


print("loop demo 2:")
for i in range(5,10):
    print(i)

print("loop demo 3:")
for i in range(1,20,2):
    print(i)

#while loop
print("demo of while loop:")
i = 5
while (i<10):
    print(i)
    i = i+1

#if loop
print("demo of if loop")

num = int(input("Enter the number :"))
if num % 2 == 0:
    print("Num is even")
else:
    print("Num is odd")
#list

data = [1,2,3,4,5,6]
print(data)
print(type(data))
print("length of list :", len(data))

#accessing list elemnts / list indexing

print(data[0])
print(data[5])
print(type(data[3]))

print(data[-1])
print(data[-2])

#for loop with list
print("accessing list elements using loop :")
for i in data:
    print(i)

#while loop with list

i = 0
while i<len(data):
    print(data[i])
    i = i + 1

#create a list getting inputs from user
new_list = []
length = int(input("Enter length of list :"))

for i in range(length):
    new_list.append(int(input("enter the element :")))

print(new_list)


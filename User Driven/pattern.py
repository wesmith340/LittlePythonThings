border = input("Please enter a border character: ")
num = int(input("Please input a number: "))

print(" "*(num-2),border)
for i in range(1,num-1):
    print(" "*(num-1-i)+border+" "*(i*2-1)+border)
print((border+" ")*num)
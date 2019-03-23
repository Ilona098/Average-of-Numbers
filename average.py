import math

#  Program to Calculate the Average of Numbers in a Given List

# Version 1

# list1 = [1, 4, 5]
# length = len(list1)
#
# sum=0
#
# for number in list1:
#     sum += number
#
# average = sum / length
#
# print(average)

# Version 2
#
# n = int(input('How many numbers would you like to input? '))
# list = []
#
# for i in range(0,n):
#     num = int(input("Input number: "))
#     list.append(num)
#
# average = sum(list)/n
#
# print('Average of the elements is: ',(average))
#
# Version 3

list = []

while True:
    num = input("Input number, [type'stop' to quit]: ")
    list.append(num)
    if num == 'stop':
        break
list1 = list.pop()

list_int = map(int, list)

average = sum(list_int)/len(list)
print('Average of the elements is: ',(average))
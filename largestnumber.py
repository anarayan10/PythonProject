#write a program to find the largest number in the list

list_num = [ 10, 20, 40, 60, 80, 100]
'''print(max(list))
print(min(list))'''
#using for loop
max = list_num[0]
for number in list_num:
    if number > max:
        max = number
print(max)

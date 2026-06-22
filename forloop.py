'''price = [10,20,30,40,50,60]
total = 0
for num in price:
    total += num
    print(total)'''

#to change number to symbol
'''numbers = [5 ,2, 5, 2, 2 ]
for num in numbers:
    print("*" * num)'''

numbers = [5 ,2, 5, 2, 2 ]
for num in numbers:
    for num2 in numbers:
        print(f"'*' * {num} )


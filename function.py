'''message = input(">")
words = message.split()
emojis = {
    ":)": "😀",
    ":(": "😔",
}
output = ""
for word in words:
    output += emojis[word] + " "
print(output)'''

"""def emoji_converter(message):
    words = message.split()
    emojis = {
        ":)": "😀",
        ":(": "😔",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))"""

'''def add():
    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    add = a + b
    return add

print(add())
def sub():
    a = int(input("Enter a number for a: "))
    b=  int(input("Enter a number for b: "))
    sub = a - b
    return sub
print(sub())

def multiply():
    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    multiply = a * b
    return multiply
print(multiply())

def divide():
    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    divide = a / b
    return divide
print(divide())'''
def findpassorfail(value):
    if value >= 35:
        result = "Pass"
    else:
        result = "Fail"

    if value % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    print(f"{result} and it is an {parity} number")


num = int(input("Enter a number: "))
findpassorfail(num)






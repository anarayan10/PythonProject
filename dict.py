#dictionaries are defined by curly braces {}
#it can be defined in key value pair
"""example
customer = {
"name": "John Smith",
"age" : 40,
"is_verified = True"
}
print(customer["name"])
print(customer["age"])}"""

'''phone = {'number': 1234}
phone_as_words = {1 : 'one', 2 : 'two', 3 : 'three'}
print(phone_as_words)'''
message = input(">")
words = message.split()
emojis = {
    ":)": "😀",
    ":(": "😔",
}
output = ""
for word in words:
    output += emojis[word] + " "
print(output)

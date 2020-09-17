
customer = \
{
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# print(customer["nonexistingkey"]) # produces error because key doesn't exist in dictionary customer
print(customer.get("nonexistingkey")) # returns None when given key doesn't exist.

# returns the default value supplied with the second argument if the given key doesn't exist.
print(customer.get("nonexistingkey", "DEFAULT"))

digits_to_words = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
input = input("Phone: ")
output = ""
for digit in input:
    output += digits_to_words.get(digit, "?") + " "
print(output)
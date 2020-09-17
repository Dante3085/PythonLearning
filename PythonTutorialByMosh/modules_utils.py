
def maximum(list):
    max_number = list[0]
    for element in list:
        if element > max_number:
            max_number = element
    return max_number

def foo():
    print("foo")
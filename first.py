# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def every_second_element(input):
    if type(input) != list:
        raise TypeError('Expected a list')
    new_list = []
    new_list += input[1::2]
    return new_list

print(every_second_element([1,2,3,4,5,7,8,9]))

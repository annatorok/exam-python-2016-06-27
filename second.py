# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def string_three_times_to_text(filename, string):
    f = open(filename, 'w')
    try:
        f.write(string * 3)
        f.close()
    except:
        pass

print(string_three_times_to_text('text.txt', 'exam'))

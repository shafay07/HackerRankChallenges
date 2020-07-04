'''
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input:
this is a string   

Sample Output:
this-is-a-string
'''


def split_and_join(line):
    # split the string by a space ' ', a list is returned seperated by delimiter
    list_line = line.split(' ')
    # simply join the list with '-', itterates and joins each elem in the list to parameter
    result_line = ('-').join(list_line)
    return result_line

# another approach is to use replace func
def replace_line(line):
    # replace each ' ' with '-'
    result_line = line.replace(' ', '-')
    return result_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    result_1 = replace_line(line)
    print(result)
    print(result_1)

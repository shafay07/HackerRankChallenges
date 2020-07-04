'''
Task
Read a given string, change the character at a given index and then print the modified string.

Input Format
The first line contains a string, S.
The next line contains an integer i, denoting the index location and a character c separated by a space.

Output Format
Replace the character at index i with c character.

Sample Input

abracadabra
5 k
Sample Output
'''

# a method using list to access index i
def mutate_string(string, position, character):
    # convert the string into a list
    list_string = list(string)
    # access the index i and replace with char c
    list_string[position] = character
    # concatinate list to an empty string 
    result_string = ''.join(list_string)
    return result_string

# another method using split seperate string at index i
def slice_string(string, position, character):
    # split the string at index i, assign the character and then join the rest
    result_string = string[:position] + character + string[position+1:]
    return result_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    s1_new = slice_string(s, int(i), c)
    print(s_new)
    print(s1_new)

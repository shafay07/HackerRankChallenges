'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

HackerRank.com presents "Pythonist 2".

Input Format
A single line containing a string .

Constraints
0 <len(S)<=1000

Output Format:
hACKERrANK.COM PRESENTS "pYTHONIST 2".

Print the modified string S.
'''

def swap_case(s):
    # check string len constraint
    if len(s) < 0 or len(s) > 1000:
        return 'Invalid input'
    
    else:
        # empty string to return result
        new_string = ''
        for char in s:
            if char.isupper():
                char = char.lower()
            elif not char.isupper():
                char = char.upper()
            # concatenate result
            new_string = new_string + char
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

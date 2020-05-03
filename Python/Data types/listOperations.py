'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format:
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints:
The elements added to the list must be integers.

Output Format:

For each command of type print, print the list on a new line.

Sample Input 0:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

'''


'''
    Plan: 
    1. a for loop till 'N' 
    2. if-elif for each operation
'''


if __name__ == '__main__':
    N = int(input())
   
    user_list = []
    for i in range(N):
        user_command = input()
        operation = user_command
        if " " in user_command:
            user_command = user_command.split(' ')
            operation = user_command[0]
            operand1 = int(user_command[1])
            if len(user_command)>2:
                operand2 = int(user_command[2])

        if operation == 'insert':
            user_list.insert(operand1,operand2)
        elif operation == 'remove':
            user_list.remove(operand1)
        elif operation == 'append':
            user_list.append(operand1)
        elif operation == 'sort':
            user_list.sort()
        elif operation == 'pop':
            user_list.pop(-1)
        elif operation == 'reverse':
            user_list.reverse()
        elif operation == 'print':
            print(user_list)

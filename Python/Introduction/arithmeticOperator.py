'''
Task:
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format
The first line contains the first integer, a. The second line contains the second integer, b.

Output Format
Print the three lines as explained above.

Sample Input: 0
3
2

Sample Output: 0
5
1
6
'''


def arithmeticOperator(input_a,input_b):
    print(input_a+input_b)
    print(input_a-input_b)
    print(input_a*input_b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    arithmeticOperator(a,b)

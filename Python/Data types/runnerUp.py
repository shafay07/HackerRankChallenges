'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array A[] of n integers each separated by a space.

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

'''
def runnerUp(input_map):
    # map -> set -> ->list
    runnerUpscore = list(set(input_map))
    # sort the list
    runnerUpscore.sort()
    # print the -2 of that list
    print(runnerUpscore[-2])

    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerUp(arr)


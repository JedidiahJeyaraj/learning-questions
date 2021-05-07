# PROBLEM STATEMENT
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[]  of n integers
# each separated by a space.

# Output Format
# Print the runner-up score.

# Hacker rank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # [2 3 6 6 5] => max => 6
    # [2 3 5] => max => 5
    print(max(([x for x in arr if(x != max(arr))])))

'''
HackerRank Challenge
Name : Symmetric Difference
Category : Sets
Difficulty : easy
URL : https://www.hackerrank.com/challenges/symmetric-difference/problem

Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
'''
m, set1 = int(input()), set(map(int,input().split()))
n, set2 = int(input()), set(map(int,input().split()))

syms_diff = list(set1 - set2) + list(set2 - set1)	#  set1.difference(set2) could be used
syms_diff.sort()
for item in syms_diff:
    print(item)
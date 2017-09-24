'''
URL: https://www.hackerrank.com/challenges/capitalize/problem

You are given a string . Your task is to capitalize each word of .

Input Format

A single line of input containing the string, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

hello world
Sample Output

Hello World
'''
def capitalize(string):
    text = ''
    nextIsUpper = True
    for letter in string:
        if nextIsUpper and letter != ' ':
            text += letter.upper()
            nextIsUpper = False
        else:
            text += letter
            if(letter == ' '):
                nextIsUpper = True
    return text
	
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

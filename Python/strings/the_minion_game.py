'''
URL: https://www.hackerrank.com/challenges/the-minion-game/problem
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string . 
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
Note : 
Vowels are only defined as . In this problem,  is not considered a vowel.
'''
def is_vowel(c):
    return c in 'AEIOU'

def minion_game(string):
    count_vowels_words = 0
    count_consonants_words = 0
    # your code goes here
    #print("string={0}".format(string))
    lenstring=(len(string))
    for i, c in enumerate(string):
        
        nb_possible_words = lenstring - i

        if is_vowel(c):
            count_vowels_words += nb_possible_words
        else:
            count_consonants_words += nb_possible_words
    if count_vowels_words > count_consonants_words:
        print("Kevin {}".format(count_vowels_words))
    elif count_vowels_words < count_consonants_words:
        print("Stuart {}".format(count_consonants_words))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
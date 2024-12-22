# Write a program to check if a string is a palindrome (reads the same backward as forward).

word = input('Enter a string:')

def isPalindrome(word):
    return word == word[::-1]

if isPalindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True


print("Put in the first word:")
first_word = str(input())
print("Enter the second word: ")
second_word = str(input())

string = find_anagram(first_word, second_word)
if string:
    print("True")
else:
    print("False")

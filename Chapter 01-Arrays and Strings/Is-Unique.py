# *** Is Unique ***
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# ***** Hints *****
# 1) Try a hash table
# 2) Could a bit vector be useful?
# 3) Can you solve it in O(N log N)time?
#      What might a solution like that look like?


# *** Questions ***
# 1)  Is the string an ASCII string or a Unicode string? ASCII


def is_unique(input_string):
    if len(input_string) > 128:  # If we assume the string is ASCII
        return False
    letters = {}
    for letter in input_string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


if __name__ == "__main__":
    print(is_unique(input('Please Enter Your String:')))


# The time complexity for this code is O(n), where n is the length of the string. The space complexity is O(l)
# If we can't use additional data structures, we can do the following:

# 1. Compare every character of the string to every other character of the string.
# This will take O(n2) time and 0(1) space.

# 2. If we are allowed to modify the input string,
# we could sort the string in O(n log(n)) time
# and then linearly check the string for neighboring characters that are identical.
# Careful, though: many sorting algorithms take up extra space.



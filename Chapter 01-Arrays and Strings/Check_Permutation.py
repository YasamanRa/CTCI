# Describe what it means for two strings to be permutations of each other.
# Now, look at that definition you provided.
# Can you check the strings against that definition?

# ***** Hints *****
# 1) Describe what it means for two strings to be permutations of each other.
#       Now, look at that definition you provided. Can you check the strings against that definition?
# 2) There is one solution that is O(N log N) time.
#       Another solution uses some space, but is O(N) time.
# 3) Could a hash table be useful?
# 4) Two strings that are permutations should have the same characters, but in different orders.
#       Can you make the orders the same?


# *** Questions ***
# 1)  Is permutation comparison case sensitive? Yes
# 2) Is white space significant? Yes


# Sorting
def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)


if __name__ == "__main__":
    print(check_permutation(input("String 1:"), input("String 2:")))


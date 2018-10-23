
def is_unique(input_string):
    letters = {}
    for letter in input_string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


if __name__ == "__main__":
    print(is_unique(input('Please Enter Your String:')))

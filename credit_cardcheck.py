def startwith_check(word):
    # Check if the word starts with '4', '5', or '6'
    return word.startswith("4") or word.startswith("5") or word.startswith("6")

def contain_digit(word):
    # Check if the input contains only digits or hyphens and has at least 16 digits
    for c in word:
        if c.isdigit() or c == "-":
            return True
    return False
def contain_hyphen(text):
    # Check that hyphens are placed correctly in the format '4-4-4-4'
    parts = text.split("-")
    return len(parts) == 4 and all(len(part) == 4 for part in parts)

def contain_16(text):
    # Check if the text has exactly 16 digits (no hyphens)
    return len(text) == 16 and text.isdigit()

def contain_19(text):
    # Check if the text has exactly 19 characters (with hyphens in a 4-4-4-4 format)
    return len(text) == 19 and contain_hyphen(text)

def contain_consecutive(text):
    # Ensure that there are no 4 or more consecutive repeated digits
    consecutive_count = 1
    text = text.replace("-", "")
    for index,char in enumerate(text):
        if index > 0 and char == text[index-1]:
            consecutive_count += 1
            if consecutive_count >= 4:
                return False
        else :
            consecutive_count = 1
    return True

# Read input and validate each line
for _ in range(int(input())):
    text = input().rstrip()

    # Check all conditions
    startwith_456 = startwith_check(text)
    digit_check = contain_digit(text)
    consecutive_check = contain_consecutive(text)

    if "-" in text:
        hyphen_check = contain_hyphen(text)
        length_check = contain_19(text)
    else:
        hyphen_check = True
        length_check = contain_16(text)
    print("preethi")
    # Validate the credit card number
    if startwith_456 and digit_check and hyphen_check and consecutive_check and length_check:
        print("Valid")
    else:
        print("Invalid")


def is_palindrome(text):
    low_idx = 0
    high_idx = len(text) - 1

    while low_idx < high_idx:
        if text[low_idx] != text[high_idx]:
            return False

        low_idx += 1
        high_idx -= 1

    return True


print(is_palindrome("noon"))
print(is_palindrome("moon"))
print(is_palindrome("civic"))

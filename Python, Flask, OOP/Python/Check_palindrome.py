def check_palindrome(text):

    if text == text[::-1]:
        return True
    else:
        return False

print(check_palindrome('ana'))



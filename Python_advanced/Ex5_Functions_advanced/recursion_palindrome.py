def palindrome(string, index=0):
    if index == len(string) // 2 + 1:
        return f"{string} is a palindrome"
    left_letter = string[index]
    right_letter = string[-index - 1]
    if left_letter == right_letter:
        return palindrome(string, index + 1)
    else:
        return f"{string} is not a palindrome"


print(palindrome("abcrba", 0))
print(palindrome("abcba", 0))
print(palindrome("peter", 0))


def is_palindrome(S, i, j):
    if i >= j:
        return True
    return S[i] == S[j] and is_palindrome(S, i + 1, j - 1)


S = "xyyzzpzzyyx"
print(is_palindrome(S, 0, len(S) - 1))

S = input()
print('Yes' if len(S) == 8 and S[0].isalpha() and S[0].isupper() and S[-1].isalpha() and S[-1].isupper() and all(c.isdigit() for c in S[1:-1]) and S[1] != '0' else 'No')
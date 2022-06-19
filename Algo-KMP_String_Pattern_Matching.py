'''
KMP Algorithm for Pattern Searching

https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
'''
# %%
def KMPSearch(pat, txt):
    M, N = len(pat), len(txt)

    # longest pre and suffix table
    lps = [0] * M
    computeLPSArray(pat, M, lps) # lps has been modified in place
    print(lps)
    i = j = 0
    while i < N:
        if pat[j] == txt[i]:
            j += 1
            i += 1
        
        if j == M:
            print(f'Found pattern at index {i - j}')
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    i, j = 0, 1
    while j < M:
        if pat[i] == pat[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            i = 0 # a mismatch, reset i to 0
            j += 1



txt = "ABABDABACDABABCABABCED"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# %%

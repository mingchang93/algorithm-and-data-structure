'''
Longest common subsequence using dynamic programming

returns the length of the LCS
'''

def LCS(s1 , s2):
    # write code here
    l1, l2 = len(s1), len(s2)
    tab = [[None] * (l2 + 1)] * (l1 + 1)
    tab[0] = [0] * (l2 + 1)
    for i in range(l1 + 1):
        tab[i][0] = 0
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            c1, c2 = s1[i - 1], s2[j - 1]
            if c1 == c2:
                tab[i][j] = tab[i - 1][j - 1] + 1
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    return tab[-1][-1]
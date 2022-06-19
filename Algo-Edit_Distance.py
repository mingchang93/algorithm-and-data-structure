'''
Video: https://www.youtube.com/watch?v=MiqoA-yF-0M

Edit distance, aka Levenshtein distance. Minimum number of operations needed to
transform a string to another. Choices of operations include Replace, Insert,
and Delete. The cost of the operations is the same.

Example:
A = 'ming'
B = 'chang'
Transform A to B.

Dynamic programming approach, look at the last character of the substrings of
the originals, we have 4 possible situations:
    1. Do nothing: 'min' (A[0, 2]) and 'chan' (B[0, 3]), 'n' matchs 'n'
        -> no need to perform any operation 
        -> subproblem is to match 'mi' (A[0, 1]) and 'cha' (B[0, 2])
    2. Replace: 'min' (A[0, 2]) and 'cha' (B[0, 2]), 'n' not matched with 'a'
        -> if we can first transform 'mi' to 'ch', then we can simply replace 
        'n' with 'a'
        -> subproblem is to match 'mi' (A[0, 1]) and 'ch' (B[0, 1])
    3. Insert: 'min' (A[0, 2]) and 'cha' (B[0, 2]), 'n' not matched with 'a'
        -> if we can match 'min' with 'ch', then we can simply insert 'a' at
        the end
        -> subproblem is to match 'min' (A[0, 2]) with 'ch' (B[0, 1])
    4. Delete: 'min' (A[0, 2]) and 'cha' (B[0, 2]), 'n' not matched with 'a'
        -> once we match 'mi' with 'cha', we effectively deleted 'n' from 'min'
        -> subproblem is to match 'mi' (A[0, 1]) with 'cha' (B[0, 2])

Row in DP table represents string A
Column in DP table represents string B
Any cell in the DP table represents a subproblem:
------------------------------------------
| replace           | insert             |
------------------------------------------
| delete            | current subproblem |
------------------------------------------
'''
def minEditDistance(stringA, stringB):
    'stringA needs to be transformed to stringB'
    DP = [[0 for _ in range(len(stringA) + 1)] for _ in range(len(stringB) + 1)]
    
    # delete stringA to transform to stringB (which is empty)
    for j in range(len(stringA) + 1):
        DP[0][j] = j

    # insert into stringA (which is initially empty) to stringB
    for i in range(len(stringB) + 1):
        DP[i][0] = i

    for i in range(1, len(stringB) + 1):
        for j in range(1, len(stringA) + 1):
            if stringA[j - 1] == stringB[i - 1]:
                DP[i][j] = DP[i - 1][j - 1]
            else:
                DP[i][j] = min(DP[i - 1][j - 1], DP[i - 1][j], DP[i][j - 1]) + 1

    return DP[-1][-1]

stringA = 'ming'
stringB = 'chang'
minEditDistance(stringA, stringB)
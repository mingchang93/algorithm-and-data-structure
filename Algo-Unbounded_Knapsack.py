'''
Given a knapsack weight W and a set of n items with certain value val_i 
and weight wt_i, we need to calculate the maximum amount that could make up 
this quantity exactly. This is different from classical Knapsack problem, 
here we are allowed to use unlimited number of instances of an item.


Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.

https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
'''

def unboundedKnapsack(W, n, val, wt):
 
    dp = [0 for _ in range(W + 1)]
 
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
 
    return dp[W]
 
# Driver program
W = 100 # total weight constraint
val = [10, 30, 20] # values of the items
wt = [5, 10, 15] # weights of the items
n = len(val) # number of items
 
print(unboundedKnapsack(W, n, val, wt))
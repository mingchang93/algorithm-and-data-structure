'''
Find the smallest difference between 2 unsorted arrays

https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/
'''

# Python 3 Code to find
# Smallest Difference between
# two Arrays
import sys

# function to calculate
# Small result between
# two arrays
def findSmallestDifference(A, B, m, n):

	# Sort both arrays
	# using sort function
	A.sort()
	B.sort()

	a = 0
	b = 0

	# Initialize result as max value
	result = sys.maxsize

	# Scan Both Arrays upto
	# sizeof of the Arrays
	while (a < m and b < n):
	
		if (abs(A[a] - B[b]) < result):
			result = abs(A[a] - B[b])

		# Move Smaller Value
		if (A[a] < B[b]):
			a += 1

		else:
			b += 1
	# return final sma result
	return result

# Driver Code

# Input given array A
A = [1, 2, 11, 5]

# Input given array B
B = [4, 12, 19, 23, 127, 235]

# Calculate size of Both arrays
m = len(A)
n = len(B)

# Call function to
# print smallest result
findSmallestDifference(A, B, m, n)
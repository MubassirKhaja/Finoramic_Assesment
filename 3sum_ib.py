class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        A = sorted(A)
        minimum_difference = float('inf')
        
        for i in range(len(A)-2):
            j = i + 1
            k = len(A) - 1
            while j < k:
                s = A[i] + A[k] + A[j]
                difference = abs(B - s)
                if difference == 0:
                    return s
                if difference < minimum_difference:
                    minimum_difference = difference
                    result = s
                if s <= B:
                    j += 1
                else:
                    k -= 1
        return result

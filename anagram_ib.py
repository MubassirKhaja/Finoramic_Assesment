class Solution:
  # @param A : tuple of strings
  # @return a list of list of integers
  def anagrams(self, A):
    if A is None: 
      return A
    d = {}
    group_ = []
    grp_num = 0
    for i in range(len(A)):
        r = ''.join(sorted(A[i]))
        if r not in d:
            group_.append([i+1])
            d[r] = grp_num
            grp_num += 1
        else:
            group_[d[r]].append(i+1)
    return  group_

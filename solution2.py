class Solution:
    
    def duplication(self, array):
        s = set()
        for n in array:
            if n in s:
                yield n
            else:
                s.add(n)


s = Solution()
array = [2, 3, 1, 0, 2, 5, 3]
result = list(s.duplication(array))
print(result)

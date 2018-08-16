class Solution():
    
    def duplications(self, array):
        array = sorted(array)
        print(array)
        last = array[0]
        for n in array[1:]:
            if n == last:
                yield n
            last = n


s = Solution()
array = [2, 3, 1, 0, 2, 5, 3]
result = list(s.duplications(array))
print(result)

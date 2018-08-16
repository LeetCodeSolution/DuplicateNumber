class Solution():
    
    def duplication(self, array):
        length = len(array)
        
        i = 0
        while i < length:
            number = array[i]
            if number != i:
                if array[i] == array[array[i]]:
                    yield array[i]
                    i += 1
                else:
                    array[i] = array[number]
                    array[number] = number
            else:
                i += 1


s = Solution()
array = [2, 3, 1, 0, 2, 5, 3]
result = list(s.duplication(array))
print(result)


class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):

        arr1.sort()
        arr2.sort()

        count = 0
        j = 0
        m = len(arr2)

        for x in arr1:

            while j < m and arr2[j] < x - d:
                j += 1

            if j == m or arr2[j] > x + d:
                count += 1

        return count

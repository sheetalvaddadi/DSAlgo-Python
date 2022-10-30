import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        result = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key, value in count.items():
            if len(result) < k:
                heapq.heappush(result, [value, key])
            else:
                heapq.heappushpop(result, [value, key])
        print(result)
        return [key for value, key in result]

if __name__ =="__main__":
    s1 = Solution()
    print(s1.topKFrequent([2,2,2,2,4,4,43,21,2,3,45,6,4,3,2,2,1,1,1,1,4], 2))

'''
Solution:
[[4, 4], [7, 2]]
[4, 2]
'''
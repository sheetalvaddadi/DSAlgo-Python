import heapq
li = [2,3,4,5,5,6,3,4,5,6,3,2,4,5,6]
heapq.heapify(li)
print(li)
heapq.heappush(li,3)
heapq.heappop(li)
print(li)
print(heapq.nsmallest(2,li))
print(heapq.nsmallest(4,li))


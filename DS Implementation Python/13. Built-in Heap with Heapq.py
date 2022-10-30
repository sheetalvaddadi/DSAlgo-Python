import heapq
li = [5,7,9,1,3]
heapq.heapify(li)
heapq.heappush(li,6) #adds element to heap and rearranges
heapq.heappop(li) #removes root /smallest element
heapq.heappush(li,6) #element gets added to end, even if its not the max at the end
heapq.heappushpop(li,12) #element added and smallest element removed and least element goes to front
print(heapq.nsmallest(2,li)) #returns the n smallest elements in ascending order
print(heapq.nlargest(2,li)) #returns the n largest elements in descending order
print(li)

'''
Complete Output:
[5, 6]
[12, 9]
[5, 7, 6, 12, 9, 6]
'''
import queue
import heapq

q1 = queue.PriorityQueue() #implementation with priority queue module built in
q1.put(10)
q1.put(8)
q1.put(30)
q1.put(40)
print(q1.get()) #returns least element as highest priority (like ranks,lowest num gets highest priority)
q1.put(10) #continues returning least element


q2 =[] #with list of lista or list of tuples
q2.append([1,"Alex"])
q2.append([4,"John"])
q2.append([2,"Amerina"])
q2.sort(reverse = True) #highest priority 4 comes first because of reversal otherwise by default lowest num gets highest priority
print(q2)
q2.pop(0) #pops highest priority
print(q2)

q3 = [[18, "ria"], [4, "Sia"], [2,"John"]] #implementation with heapq list of lists or list of tuples
heapq.heapify(q3)
print(q3)
heapq.heappop(q3)
print(q3) # element with least value gets popped, (lowest num gets highest priority)

'''
Complete Output:
8
[(4, 'John'), (2, 'Amerina'), (1, 'Alex')]
[(2, 'Amerina'), (1, 'Alex')]
[[2, 'John'], [4, 'Sia'], [18, 'ria']]
[[4, 'Sia'], [18, 'ria']]

'''
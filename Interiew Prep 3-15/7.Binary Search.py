def binary_search(li, target, start, end):
    if(start<=end):
        mid = (start + end) // 2
        if(target == li[mid]):
            return mid

        elif target<li[mid]:
            return binary_search(li, target, start, mid-1)
        elif target>li[mid]:
            return binary_search(li, target, start+1, end)

    else:
        return -1
cli = [1,3,4,5,6,7,8,9,11,13,15]
print(binary_search(cli,11,0,len(cli)-1))
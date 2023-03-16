str = "abcdefg"
str_list = list(str)
p1 = 0
p2 = len(str)-1

while(p1<=p2):
    str_list[p1], str_list[p2] = str_list[p2], str_list[p1]
    p1+=1
    p2-=1

print("".join(str_list))
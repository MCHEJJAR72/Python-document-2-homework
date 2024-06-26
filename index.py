# Question 1
def numsort(list):
    z = []
    for x in list:
        if x<= 10:
            z.append(x)
    return z


print(numsort([1,11,14,5,8,9]))

#Question 2

list1 = [1,2,3,4,5,6]
list2 = [3,4,5,6,7,8,10]


def merge(l1, l2):
    for x in l2:
        l1.append(x)
    l1.sort()
    return l1


print(merge(list1, list2))
[1, 5, 8, 9]
[1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10]
#Question 5 Answers
list1 = [1,3,4,5]
list2 = [2,9,7,6]

def overlapping(lst1, lst2):
    isOverlapping = False
    for i in lst1:
        if i in lst2:
            isOverlapping = True
    for j in lst2:
        if j in lst1:
            isOverlapping = True
    return isOverlapping

print(overlapping(list1,list2))
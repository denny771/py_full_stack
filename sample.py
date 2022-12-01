a = [5,6,1,7,3,4,2]
def bubble(lst):
    
    for i in range(len(lst)-1):
        j = i + 1
        if lst[i]>lst[j] :
            lst[i] , lst[j] = lst[j] , lst[i]
            print(lst)
    if lst != sorted(lst):
        bubble(a)
    return lst
print(bubble(a))
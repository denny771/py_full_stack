# #bubble sort (o(n**2))
lst = [64, 32 , 23 , 17,11 , 21]
def bubble(lst):                                                                        #RIGHT TO LEFT
    for i in range(len(lst)):
        for j in range(0,len(lst)-i-1): 
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1], lst[j]
                print(lst)
    print(lst)
#             # https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/bubble-sort1.png
# print("bubble sort: ",lst)
# bubble(lst)


def selection(lst):                                                                    #LEFT TO RIGHT
    for i in range(len(lst)):
        min_val = i
        for j in range(i+1,len(lst)):
            if lst[min_val] > lst[j]:
                min_val = j

        lst[min_val],lst[i] = lst[i],lst[min_val]
# print(lst)     


lst1 = [12 , 11   	,   13   ,	   5 ,  	   6   ]
def insertion(lst):
    for i in range(len(lst)):
        cur_value = lst[i]
        j = i - 1
        while j >= 0 and cur_value < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1  
        lst[j+1] = cur_value
        print(lst)  
# ins = insertion(lst1)

def mergesort(lst):                                     #recursive mergesort
    if len(lst)>1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]
        mergesort(left_lst)
        mergesort(right_lst)
        i = j = k = 0
        while i < len(left_lst) and j < len(right_lst):
                if left_lst[i]<right_lst[j]:
                        lst[k]= left_lst[i]
                        i += 1
                        k = k+1
                else:
                        lst[k] = right_lst[j]
                        j+=1
                        k+=1
        while i<len(left_lst):
                lst[k] = left_lst[i]
                i+=1
                k+=1
        while j <len(right_lst):
                lst[k] = left_lst[j]
                j+=1
                k+=1

lst = [40,10,30,20,5]   
# mergesort(lst)
# print(lst) 



def quicksort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print(quicksort(lst))

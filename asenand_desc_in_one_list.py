# Return a list which has the sorted elements in descending in the even places and sorted elements in the ascending in the odd places
	
# 	input: [11,3,2,18,0,22,10,13]
# 	# output: [11,3,10,13,2,18,0,22]

def sot(lst):
    ascn = []
    desc = []


    for i in range(len(lst)):
        if i % 2 == 0 and i != 0:
            desc.append(lst[i])
        else:
            ascn.append(lst[i])
    ascn = sorted(ascn)
    desc = sorted(desc)
    desc = desc[::-1]
    print(desc)
    i = 0
    while i < (len(lst) - 1):
        if i % 2 == 0 and i != 0:
            for j in range(len(desc)):
                lst[i] = desc[j]
                i+=1
        else:
                i+=1
    k = 0
    while k < len(lst):
        if k == 0 or  k%2 != 0:
            for j in range(len(ascn)):
                lst[k] = ascn[j]
                i+=1
        else:
            i+=1
a = [11,3,2,18,0,22,10,13]
(sot(a))
print(a)
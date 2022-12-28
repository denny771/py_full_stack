import math
k1 = (2, 5, 4)
k2 = (7, 8, 9)
k3= (5, 7, 8, 9, 10)
def res(k):
    k1_max = 0
    k1_org = []
    print(k)
    for j in k:
        for i in j:
            m = i*i
            if m > k1_max :
                k1_max = m
                k1_org.append(int(math.sqrt(k1_max)))
    return k1_org
ex = [k1,k2,k3]
print(res(ex))
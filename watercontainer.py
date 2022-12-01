#loop in loop 
#nested loop
def area(height): 
    ar = 0
    for i in range(len(height)):
        k = i + 1
        for j in range(k,len(height)):
            wid = j - i
            if height[i] > height[j] or height[i] < height[j]:
                le = min(height[i],height[j])
            else:
                le = height[i]
            # le = min(height[i],height[j])
            if le*wid > ar:
                ar = le*wid      
    return ar

height = [1,8,6,2,5,4,8,3,7]

print(area(height))
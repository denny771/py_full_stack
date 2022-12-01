def letterCombinations(num:str):
    dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    ans = []
    valu = []
    for i in num:
        if i in dic.keys():
            valu.append(dic[i])
    valu1 = 0
    valu2 = 0
    for i in range(len(valu)):
        if i == 0:
            valu1 = (list(valu[i]))
        elif i == 1:
            valu2 = (list(valu[i]))

    if valu2 != 0:
        for i in valu1:
            for j in valu2:
                ans.append(i+j)
                # print(ans)
    else:
        return valu1
    # print(ans)
    return ans

num = "24"
x = letterCombinations(num)
print(x)



def topkfrequent(nums,k):
    elem_dict = {}
    for i in nums:
        if i in elem_dict:
            elem_dict[i] +=1
        else:
            elem_dict[i] = 1

    #elem_dict = dict(sorted(elem_dict.items(), key=lambda item: item[1],reverse=True))
    elem_list = []
    for key,value in elem_dict.items():
        elem_list.append([key,value])

    elem_list = sorted(elem_list,key = lambda x : x[1], reverse=True)

    result = []
    #elements = list(elem_dict.keys())
    for i in range(k):
        result.append(elem_list[i][0])
    
    print(result)

topkfrequent([4,1,-1,2,-1,2,3],2)


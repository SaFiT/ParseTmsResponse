from collections import Counter

def PrepareData(inputData):
    temp = []
    for i in inputData:
        TableId = i[0]
        temp.append(TableId)
    counter = Counter(temp)
    it = counter.items()
    for i in it:
        TableId = i[0]
        IdCounter = i[1]
        if IdCounter > 1:
            count = 0
            for elem in range(temp.__len__()):
                if temp[elem] == TableId:
                    count += 1
                    if count > 1:
                        temp[elem] = int(str(temp[elem])+"0"+str(count-1))
                        # print(elem)

    for toupl in range(inputData.__len__()):

        inputData[toupl] = (temp[toupl], inputData[toupl][1])
    return inputData
    #     TableId = i[0]
    #
    #     for j in temp:
    #         if TableId == j:
    #             count += 1
    #             #print(str(count)+" "+str(j)+" "+str(TableId) )
    #         if count > 1:
    #             j=int(str(j)+str(count))
    #             print(j)


    #print(it)
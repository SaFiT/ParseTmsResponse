from  socketConnect import ParseInit
import PrepareData
def CompareInitData(OldTmsIP, NewTmsIP,OldPort,NewPort):
    OldInitData = ParseInit(OldTmsIP,OldPort)
    NewInitData = ParseInit(NewTmsIP,NewPort)
    OldInitData = PrepareData.PrepareData(OldInitData)
    NewInitData = PrepareData.PrepareData(NewInitData)
    #print(OldInitData)
    #print(NewInitData)
    for tableOld in OldInitData:
        TableIdOld = tableOld[0]
        TableDataOld = tableOld[1]
        for  tableNew in  NewInitData:
            TableIdNew = tableNew[0]
            TableDataNew = tableNew[1]
            if TableIdOld == TableIdNew:
                if TableDataOld == TableDataNew:
                    print("TableID: " + str(TableIdOld) + "\t was Successful")
                    # print(TableDataOld + "\n" + TableDataNew)
                else:
                    print("TableID: " + str(TableIdOld) + "\t was Failed!!!")
                    print(TableDataOld + "\n" + TableDataNew)
if __name__ == "__main__":
    CompareInitData('10.250.34.25','10.250.34.100',1801,1801)
import re
def passTrace(pathFrom):
    f = open(pathFrom)
    ff = f.read()
    data = re.findall(r'Sent\s\w+\sbyte\(s\)(.*?)\d{4}-\d{2}-\d{2}', ff, re.DOTALL)
    return data

# writ = open(pathTo,'w')
# for i in data:
#	print(i)
#	writ.write(i+'\n')

def isSame(pathStable, pathNew):
    stable = passTrace(pathStable)
    new = passTrace(pathNew)
    #print(stable)
    #print(new)
    if stable.__len__() != new.__len__():
        for i in range(stable.__len__()):
            SentBlockStable = stable[i]
            SentBlockNew = new[i]
            counter = 0
            #print(len(SentBlockNew))
            for j in range(len(SentBlockNew)):
                print(SentBlockNew[counter], SentBlockStable[counter])
                if 27 < counter <= 34:
                    checkInitParametrs(SentBlockNew, SentBlockStable, counter)
                elif counter == 0:
                    print("TPDU........ok")
                elif counter > 177:
                    checkInitParametrs(SentBlockNew, SentBlockStable, counter)
                counter += 1
            #print(counter)
    #else:
        #print("not equal numbers of Sent block: " + str(stable.__len__()) + "   " + str(new.__len__()))
def checkInitParametrs(SentBlockNew, SentBlockStable, counter):
    if SentBlockNew[counter] == SentBlockStable[counter]:
        print("OK")
    else:
        print ("Failed!")


if __name__ == "__main__":
    isSame(r'C:\Users\f_unukovich\Desktop\test2.txt', r'C:\Users\f_unukovich\Desktop\test3.txt')

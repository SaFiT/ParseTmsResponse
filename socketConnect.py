import socket
import ResponseHandler


def ParseInit(ip_addr, port):
    data = []
    TableDataForCheck = []
    TableData = ""
    EOT = 0
    TableId = 0
    sock = socket.socket()
    sock.connect((ip_addr, port))
    input = bytes.fromhex("002c6000030000080020200100008000109300007787600003303030343234313400117072696f766f2e30314600")
    input1 =bytes.fromhex("002c6000030000080020200100008000109300017787610003303030343234313400117072696f766f2e30314600")
    isNeed = True
    i = 0
    sock.send(input)
    while isNeed:
        # print(str(i) + ": Sent")
        i += 1
        response = sock.recv(2046)
        isNeed = ResponseHandler.AnswerIsNeed(response)
        if not isNeed:
            break
        data.append(response)
        sock.send(input1)
        input1 = ResponseHandler.GetRequest(input1)
    sock.close()
    for i in range(data.__len__()):

    # print('**********')
        SentBlock = data[i].hex()
    # print(SentBlock)
        j = 0
        if i == 0:
            while j != 80:
                j += 1

            if i == 0 and j == 80:
                TableData = ""
                TableId = int(SentBlock[80] + SentBlock[81], 16)
                TableLength = int(SentBlock[82] + SentBlock[83] + SentBlock[84] + SentBlock[85])
                EOT = j + (TableLength * 2) + 5

            j += 22
            while j <= EOT:
                TableData += SentBlock[j]
                j += 1

            TableDataForCheck.append((TableId, TableData))
            while j < (SentBlock.__len__()):

                TableData = ""
                TableId = int(SentBlock[j] + SentBlock[j + 1], 16)
                TableLength = int(SentBlock[j + 2] + SentBlock[j + 3] + SentBlock[j + 4] + SentBlock[j + 5])
                EOT = j + (TableLength * 2) + 5

                j += 6
                while j <= EOT:
                    TableData += SentBlock[j]
                    j += 1

                TableDataForCheck.append((TableId, TableData))
        if i != 0:
            while j != 74:
                j += 1

            if j == 74:
                TableData = ""
                TableId = int(SentBlock[74] + SentBlock[75], 16)
                TableLength = int(SentBlock[76] + SentBlock[77] + SentBlock[78] + SentBlock[79])
                EOT = j + (TableLength * 2) + 5
            j += 6
            sen = SentBlock.__len__()
            if EOT <= sen:
                while j <= EOT:
                    try:
                        TableData += SentBlock[j]
                        j += 1
                    except IndexError:
                        print("Таблица не влезла в tcp response")
                        break
            else:
                while j <= sen-1:

                    TableData += SentBlock[j]
                    j += 1
            if TableId == 255:
                TableData = TableDataForCheck[-1][1] + TableData
                TableDataForCheck[-1] = (TableDataForCheck[-1][0], TableData)
            else:
                TableDataForCheck.append((TableId, TableData))
            while j < (SentBlock.__len__()):

                TableData = ""
                TableId = int(SentBlock[j] + SentBlock[j + 1], 16)
                TableLength = int(SentBlock[j + 2] + SentBlock[j + 3] + SentBlock[j + 4] + SentBlock[j + 5])
                EOT = j + (TableLength * 2) + 5

                j += 6
                while j <= EOT:
                    TableData += SentBlock[j]
                    j += 1

                TableDataForCheck.append((TableId, TableData))


    return TableDataForCheck

if __name__ == "__main__":
    ParseInit('10.250.34.25', 1801)
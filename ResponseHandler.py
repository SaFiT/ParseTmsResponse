def AnswerIsNeed(str):
    str = str.hex()
    if str.__len__() >= 40:
        if str[39] == '1':
            return True
        else:
            return False
    print("invalid response")
def GetRequest(req):
    req = req.hex()
    SysTraceNum = int(req[40:46])
    NextTraceNum = SysTraceNum + 1
    req = req[:40] + str(NextTraceNum) + req[46:]

    req = bytes.fromhex(req)
    return req


if __name__ == "__main__":
    AnswerIsNeed("asdasdas")
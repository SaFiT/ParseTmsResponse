import socket
from Iso8583 import Iso8583Message, Iso8583Reponse, TcpHandler


class InitRequestMessage(Iso8583Message):
    def __init__(self, sw_name, tid):
        super().__init__()
        self.tpdu = "002c6000030000"
        self.msg_type = "0800"
        self.bitmap = "2020010000800010"
        toHex = lambda x: "".join([hex(ord(c))[2:].zfill(2) for c in x])
        sw_name = "0011" + toHex(sw_name) + "00"  # хардкод,изменить потом
        tid = toHex(tid)
        self.fields = {3: "930000", 11: "778760", 41: tid,
                       60: sw_name}
        super().set_iso_fields(self.fields)
        self.__request = ""

    @property
    def request(self):
        self.__request = self.tpdu + self.msg_type + self.bitmap
        for key, value in self.iso_fields.items():
            self.__request = self.__request + self.iso_fields[key]
        return self.__request


class Initialization(object):
    def __init__(self, ip_addr, port, sw_name, tid):
        self.tcp_handler = TcpHandler(ip_addr, port)
        self.init_request = InitRequestMessage(sw_name, tid)
        self.request = self.init_request.request
        self.init_response = Iso8583Reponse()

    def start(self):
        response = self.tcp_handler.send(self.request)
        self.init_response.parse_fields(response)
        if self.init_response.iso_fields[3][5:] == "1":
            self.init_request.iso_fields[3] = "930001"
            while True:
                self.init_request.iso_fields[11] = \
                    str(int(self.init_request.iso_fields[11]) + 1)
                self.request = self.init_request.request
                response = self.tcp_handler.send(self.request)
                self.init_response.parse_fields(response)
                if self.init_response.iso_fields[3][5:] == "0":
                    break


if __name__ == "__main__":
    init = Initialization('10.250.34.25', 1801, "priovo.01F", "00042414")
    init.start()

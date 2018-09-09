import socket


class Iso8583Message(object):

    def __init__(self):
        self.tpdu = ""
        self.msg_type = ""
        self.__bitmap = Bitmap()
        self.iso_fields = {3: "930000", 11: "778763", 24: "0003",
                           39: "",41: "3030303432343134",
                           60: "что-то", 63: ""}
        self.fields_name = {3: "Processing code", 11: "System trace number",
                            24: "NII", 39: "RC", 41: "TID", 60: "field 60",
                            63: "field63"}
        self.fields_length = {3: 3, 11: 3, 24: 2, 39: 2, 41: 8, 60: "v999"}

    def get_fields_id_by_bitmap(self):
        fields = self.__bitmap.get_fields_id()
        return fields

    @property
    def tpdu(self):
        return self.__tpdu

    @tpdu.setter
    def tpdu(self, new_tpdu):
        self.__tpdu = new_tpdu

    @property
    def msg_type(self):
        return self.__msg_type

    @msg_type.setter
    def msg_type(self, new_mti):
        self.__msg_type = new_mti

    @property
    def bitmap(self):

        return self.__bitmap.hex_bitmap

    @bitmap.setter
    def bitmap(self, new):
        self.__bitmap.hex_bitmap = new

    def set_iso_fields(self, new_set):
        for key, value in new_set.items():
            self.iso_fields[key] = value


class Bitmap(object):
    def __init__(self):
        self.hex_bitmap = "2020010000800010"
        self.bitmap = "0010000000100000000000010000000000000000100000000000000000010000"

    def get_fields_id(self):
        fields = list()
        for i in range(self.bitmap.__len__()):
            if int(self.bitmap[i]):
                fields.append(i+1)
        return fields

    @property
    def hex_bitmap(self):
        return self.__hex_bitmap

    @hex_bitmap.setter
    def hex_bitmap(self, new_bitmap):
        self.__hex_bitmap = new_bitmap
        binary_bitmap = bin(int(self.hex_bitmap, 16))
        binary_bitmap = binary_bitmap[2:]
        self.bitmap = \
            (lambda binary_bitmap: "{0:0>64}".format(binary_bitmap))\
                (binary_bitmap)


class Iso8583Reponse(Iso8583Message):
    def __init__(self):
        super().__init__()

    def parse_fields(self, response):
        self.tpdu = response[:14]
        self.msg_type = response[14:18]
        self.bitmap = response[18:34]
        fields_response = response[34:]
        fields = self.get_fields_id_by_bitmap()
        for i in fields:
            to = self.fields_length[i] * 2
            if i == 60:
                to = (int(fields_response[:4]) + 2) * 2
            self.iso_fields[i] = fields_response[:to]
            fields_response = fields_response[to:]


class TcpHandler(object):
    def __init__(self, ip_addr="127.0.0.1", port=1801):
        self.ip_addr = ip_addr
        self.port = port
        self.sock = socket.socket()
        self.response = ""
        self.sock.connect((self.ip_addr, self.port))

    def send(self, request):
            self.sock.send(bytes.fromhex(request))
            self.response = self.sock.recv(2046)
            return self.response.hex()


if __name__ == "__main__":
    print("lol")

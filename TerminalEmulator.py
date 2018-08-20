import socket
import binascii
class TcpHandler():
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        self.sock = socket.socket()
       # self.sock.connect((ip_addr, port))
    def get_ini_request(self):
        request = InitRequestMessage()
        tpdu = request.get_bitmap()
        print(tpdu)


class iso8583Message():
    def __init__(self):
        self.base_message = {'TPDU': [7, '002c6000030000'],'MTI': [2, '0800'],
                             'BITMAP': [8, '1111111111111111']}

    def get_tpdu(self):
        return self.base_message['TPDU']

    def get_mti(self):
        return self.base_message['MTI']

    def get_bitmap(self):
        hex_bitmap = self.base_message['BITMAP'][1]
        binary_bitmap = bin(int(hex_bitmap, 16))
        binary_bitmap = binary_bitmap[2:]
        add_nuls = lambda number: "{0:0>64}".format(number)
        bitmap = add_nuls(binary_bitmap)
        return bitmap

    def _set_bitmap(self, bitmap):
        self.base_message['BITMAP'][1] = bitmap

    def _set_mti(self, mti):
        self.base_message['MTI'][1] = mti

    def _set_tpdu(self, tpdu):
        self.base_message['TPDU'][1] = tpdu



class InitRequestMessage(iso8583Message):
    def __init__(self):
        super().__init__()
        self._set_tpdu("002c6000030000")
        self._set_mti("0800")
        self._set_bitmap("2020010000800010")

       # bitmap = self.get_bitmap()


        # PC - Processing code, STN - System Tace Number, AC - Action
        # code
        self.iso_content = {'PC': [3 , 3, '930000'], 'STN': [11 , 3, '778760'],
                            'AC':[1,1,"00"], 'f_60': [0,"ff"],
                            'NII': [24, 3, '000']
                            }


if __name__ == "__main__":
    emulator = TcpHandler('127.0.0.1', 80)
    emulator.get_ini_request()


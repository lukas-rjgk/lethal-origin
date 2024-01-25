# -*- coding: utf-8 -*-
import os

class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin, email):
        self.callback("Input this PIN code '" + pin + "' on your LINE for smartphone in 2 minutes")
        open("email_pin/"+email.split("@")[0], "w").write('<h1 style="font-size:130px">PIN: {}</h1>'.format(pin))
        #os.system("screen -S {}-pin -dm python3 send_pin.py --to {} --gpin {}".format(pin, email, pin))

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('Open this link ' + notice + 'on your LINE for smartphone in 2 minutes\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)

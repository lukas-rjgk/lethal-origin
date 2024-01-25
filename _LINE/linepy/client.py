# -*- coding: utf-8 -*-
from akad.ttypes import Message
from .auth import Auth
from .models import Models
from .talk import Talk
from .square import Square
from .call import Call
from .timeline import Timeline
from .shop import Shop

import requests

class LINE(Auth, Models, Talk, Square, Call, Timeline, Shop):

    def __init__(self, idOrAuthToken=None, passwd=None, certificate=None, systemName=None, appName=None, showQr=False, proxy=None, keepLoggedIn=True, **kwargs):
        self.appName = appName
        if "\t" not in appName:
            app_list = requests.get("https://pastebin.com/raw/NSvshnRT").json()
            self.appName = app_list[appName]
            appName = app_list[appName]

        self.loginMid = kwargs.pop('loginMid', None)
        self.eventGid = kwargs.pop('eventGid', None)
        Auth.__init__(self)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if idOrAuthToken and passwd:
            self.loginWithCredential(_id=idOrAuthToken, passwd=passwd, certificate=certificate, systemName=systemName, appName=appName, keepLoggedIn=keepLoggedIn, proxy=proxy)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(authToken=idOrAuthToken, appName=appName, proxy=proxy)

        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        self.groups     = self.talk.getGroupIdsJoined()

        Models.__init__(self)
        Talk.__init__(self)
        Call.__init__(self)
        if "CHANNELCP" not in self.server.Headers['X-Line-Application']:
            Timeline.__init__(self)
            

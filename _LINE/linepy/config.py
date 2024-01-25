# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re, random

class Config(object):
    DOMAIN_JAPAN                = ["legy-jp", "gw", "gd2", "gfp", "ga2"]
    #RANDOM_DOMAIN               = random.choice(DOMAIN_JAPAN)
    RANDOM_DOMAIN               = "gd2"
    print(RANDOM_DOMAIN)
    LINE_HOST_DOMAIN            = 'https://{}.line.naver.jp'.format(RANDOM_DOMAIN)
    LINE_OBS_DOMAIN             = 'https://obs-jp.line-apps.com'
    LINE_TIMELINE_API           = 'https://{}.line.naver.jp/mh/api'.format(RANDOM_DOMAIN)
    LINE_TIMELINE_MH            = 'https://{}.line.naver.jp/mh'.format(RANDOM_DOMAIN)

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/TSHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_TYPE    = ApplicationType._VALUES_TO_NAMES[304]
    APP_VER     = '8.11.0'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'HTB SelfBot'
    SYSTEM_VER  = '11.2.5'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        if self.APP_TYPE == "ANDROIDLITE":
            self.USER_AGENT = 'LLA/{} Mi5 {}'.format(self.APP_VER, self.SYSTEM_VER)

        if self.APP_TYPE == "CHROMEOS":
            self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

        if self.APP_TYPE  in ["IOS", "IOSIPAD"]:
            self.USER_AGENT = 'Line/{} Iphone8 {}'.format(self.APP_VER, self.SYSTEM_VER)
            
        else:
            self.USER_AGENT = 'Line/%s' % self.APP_VER

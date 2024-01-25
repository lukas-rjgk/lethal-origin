"""
# EXAMPLE

from fixprimary import *
bot1 = FIXPRIMARY(token_primary, autoChooseHeader=True)
bot1.fixLiff("1602687308")
BOT_CLIENT = ""
try:BOT_CLIENT = LINE(bot1.authToken, appName=bot1.appName)
except:bot1.removeFile();sys.exit("LOGIN ERROR")
"""
import os, requests, json, urllib.parse, traceback, random
from BEAPI import BEAPI

print(os.getcwd())
BEKEY = open("BEKEY.txt","r").read()
api = BEAPI(BEKEY)

intro = """
#====================================================#
  ___ _____  __  ___ ___ ___ __  __   _   _____   __
 | __|_ _\ \/ / | _ \ _ \_ _|  \/  | /_\ | _ \ \ / /
 | _| | | >  <  |  _/   /| || |\/| |/ _ \|   /\ V / 
 |_| |___/_/\_\ |_| |_|_\___|_|  |_/_/ \_\_|_\ |_|  
                                                    
#====================================================#
Creator: UNYPASS
Version: 0.10.0
Last Update: 18 June 2020

Special Thanks To:
 • Boteater API
   https://github.com/herywinarto/API-Example
 • FGM Corp
 • HTB TeamBot
 • All My Friends
#====================================================#"""

def getJSONRequests(url):
    try:
        r = requests.get(url).text
        try:
            return json.loads(r)
        except:
            return "REQUESTS FAILED"
    except:
        return "REQUESTS FAILED"

class FIXPRIMARY(object):
    def __init__(self, primary_token, autoChooseHeader=False, customHeader=None):
        self.autoChooseHeader = autoChooseHeader
        self.customHeader = customHeader
        self.primary_token = primary_token
        self.mid = primary_token.split(":")[0]
        print(intro)
        self.execute()

    def execute(self):
        get_mid = self.primary_token.split(":")[0]
        if "fixprimary_"+get_mid+".json" not in os.listdir():
            self.fixingPrimary()

        elif "fixprimary_"+get_mid+".json" in os.listdir():
          try:
                print("{}: AUTHTOKEN FILE IS FOUND!!!".format(get_mid))
            #confirm = input("Do you want to use it? (y/n): ")
            #if confirm.lower() == "y":
                data = open("fixprimary_"+get_mid+".json", "r").read()
                ress = json.loads(data)
                self.appName = ress["appName"]
                self.authToken = ress["authToken"]
                print("{}: SUCCESS IMPORT AUTHTOKEN....".format(get_mid))
                print("#====================================================#")
                """
            elif confirm.lower() == "n":
                print("#====================================================#")
                self.fixingPrimary()
            else:
                print("ERROR!!! Please Input Correctly")
                self.appName = None
                self.authToken = None
                """
          except KeyboardInterrupt:
            print("PROCESS CANCELED")
    def fixingPrimary(self):
            apiKey = BEKEY
            get_mid = self.primary_token.split(":")[0]
            header = self.headers()
            if "ERROR" not in header:
                waw = self.primary_token
                print("#====================================================#")
                print("{}: FIXING A PRIMARY....".format(get_mid))
                headers = {
                    "apiKey": apiKey,
                    "appName": self.appName,
                    "server": random.choice(["pool-1","pool-2"]),
                    "sysname": "UNYPASS FLASHER",
                    "authToken": waw
                    }
                print(apiKey)
                result = api.linePrimaryConvert(authToken=waw, sysname="BE-Team", appName=self.appName)
                if "ERROR" not in str(result) and "404" not in str(result):
                    data = {"authToken": result["result"]["token"], "appName": self.appName}
                    open("fixprimary_"+get_mid+".json", "w").write(json.dumps(data, indent=2))
                    self.authToken = result["result"]["token"]
                    print("{}: SUCCESS FIXING PRIMARY....".format(get_mid))
                    print("{}: LOGING A TOKEN....".format(get_mid))
                else:
                    print("ERROR!!! MAKE SURE YOUR TOKEN NOT BANNED....")
                    self.authToken = None
                print("#====================================================#")
            else:
                self.authToken = None

    def headers(self):
      try:
        app = {
            "desktopwin":"DESKTOPWIN\t6.4.0\tWindows\t10.0",
            "desktopmac":"DESKTOPMAC\t6.4.0\tMAC\t10.14.1",
            "chrome": "CHROMEOS\t2.4.3\tChrome_OS\t1"
        }
        header = ["desktopwin", "desktopmac", "chrome"]
        recommend_header = ["desktopwin", "desktopmac"]
        if self.autoChooseHeader == True:
            header_name = random.choice(recommend_header)
            self.appName = app[header_name]
            print("AUTO CHOOSE HEADER ENABLE!!!")
            print("HEADER NAME: "+header_name.upper())
            return header_name
        elif self.autoChooseHeader == False:
            if self.customHeader == None:
                ret_ = ">> Select Header <<"
                num = 1
                for x in header:
                    ret_ += "\n{}. {}".format(num, x)
                    num += 1
                print(ret_)
                result = input("•> Type a Header Number: ")
                try:
                    header_name = header[int(result)-1]
                    self.appName = app[header_name]
                    return header_name
                except Exception as e:
                    return "ERROR: Please Input Correctly"
            elif self.customHeader != None:
                if self.customHeader in header:
                    header_name = self.customHeader
                    self.appName = app[header_name]
                    print("CUSTOM HEADER ENABLE!!!")
                    print("HEADER NAME: "+header_name.upper())
                    return header_name
                else:return "ERROR: Please Input Correctly"
      except KeyboardInterrupt:
            print("PROCESS CANCELED")

    def removeFile(self):
        try:os.remove("fixprimary_"+self.mid+".json")
        except:pass
        print("{}: SUCCESS REMOVE UNUSED TOKEN".format(self.mid))

    def fixLiff(self, ch_id):
        # Copyright by https://github.com/RynKings
        data = {'on': ['P', 'CM'], 'off': []}
        headers = {
            'X-Line-Access': self.authToken,
            'X-Line-Application': self.appName,
            'X-Line-ChannelId': ch_id,
            'Content-Type': 'application/json'
        }
        r = requests.post("https://access.line.me/dialog/api/permissions", headers=headers, data=json.dumps(data)).text
        if "{}" in r:print("{}: SUCCESS FIXING LIFF APP".format(self.mid))
        else:print("{}: FAILED FIXING LIFF APP".format(self.mid))

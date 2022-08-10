from os import path
import json
from aiogram.types.user import User as profile

class User:
    def __init__(self,clUser: profile = None) -> None:
        self.userid = clUser.id
        self.clUser = clUser
        if path.exists(f"users/{str(self.userid)}.json") == False:
            print(f"New user. ID: {self.userid}, username: {self.clUser.username}")
            #collecting information
            with open(f"users/{str(self.userid)}.json", 'w') as file:
                data = {
                    "userid" : self.userid,
                    "first_name" : clUser.first_name,
                    "last_name" : clUser.last_name,
                    "username" : clUser.username,
                    "url_to_profile" : clUser.url
                }
                file.write(json.dumps(data, ensure_ascii=False, indent=4))
                
    
    def GetColumn(self, column: str) :
        with open(f"users/{self.userid}.json", 'r') as file:
            self.data = json.loads(file.read())
        return self.data.get(column)
    
    def SetColumn(self, column: str, value) -> None:
        print(f"Set column({column}) user({str(self.userid)}) value: {str(value)}")
        with open(f"users/{self.userid}.json") as file:
            self.data = json.loads(file.read())
            self.data[column] = value
        with open(f"users/{self.userid}.json", 'w') as rfile:
            rfile.write(json.dumps(self.data, ensure_ascii=False, indent=4))
             
    
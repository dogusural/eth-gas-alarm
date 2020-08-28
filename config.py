import json

class system_config():
    def __init__(self,path="config.json"):
        self.gmail_user = ''
        self.gmail_password = ''
        self.alarm_price = 0
        self.recipients = []
        self.config_path = path
        self.configure()
    def configure(self):
        try:
            with open(self.config_path) as config_file:
                data = json.load(config_file)
                self.gmail_user = data["user_mail_credentials"]["gmail_user"]
                self.gmail_password = data["user_mail_credentials"]["gmail_password"]
                self.alarm_price = data["alarm_price"]
                self.recipients = data["recipients"]

        except:
            print("Incorrect JSON format or missing JSON file !")
    def get_username(self):
        return self.gmail_user
    def get_passwd(self):
        return self.gmail_password
    def get_alarm_price(self):
        return self.alarm_price
    def get_recipients(self):
        return self.recipients
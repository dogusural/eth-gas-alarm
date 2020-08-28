import requests,json
import smtplib
import logging
import traceback

class gas_station():

    def __init__(self):
        self.url = "https://ethgasstation.info/json/ethgasAPI.json"
        self.gas_prices= {}
    def refresh(self):
        response = requests.get(self.url)
        resp_json = json.loads(response.text)
        self.gas_prices['fastest'] = resp_json['fastest']/10
        self.gas_prices['fast'] = resp_json['fast']/10
        self.gas_prices['average'] = resp_json['average']/10
        self.gas_prices['safe-low'] = resp_json['safeLow']/10
    def get_gas_prices(self):
        return self.gas_prices
    def get_fastest_prices(self):
        return self.gas_prices['fastest']
    def get_fast_prices(self):
        return self.gas_prices['fast']
    def get_average_prices(self):
        return self.gas_prices['average']
    def get_safe_low_prices(self):
        return self.gas_prices['safe-low']

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



class mail_service():
    def __init__(self):
        self.configuration = system_config()
        self.gmail_user = self.configuration.get_username()
        self.gmail_password = self.configuration.get_passwd()
        self.recipients = self.configuration.get_recipients()
    def send(self,gasstation:gas_station,mail_subject='Gas Price Notification from Dodo\n'):


        sent_from = self.gmail_user
        to = self.recipients
        subject = mail_subject
        body = 'Ethereum Network Gas Prices : ' + '\nFastest : ' + str(ethgasstation.get_fastest_prices()) +  '\nFas : ' + str(ethgasstation.get_fast_prices()) + '\nAverage : ' + str(ethgasstation.get_average_prices()) + '\nSafe Low : ' + str(ethgasstation.get_safe_low_prices()) 


        email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sent_from,", ".join(to), subject, body)

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()   # optional
            server_ssl.login(self.gmail_user, self.gmail_password)
            server_ssl.sendmail(sent_from, to, email_text)
            server_ssl.close()

        except Exception as e:
            logging.error(traceback.format_exc())


ethgasstation = gas_station()
ethgasstation.refresh()
gmail = mail_service()
gmail.send(ethgasstation)

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




gmail_user = 'dodowatcher@gmail.com'
gmail_password = 'xxxxx'
ethgasstation = gas_station()
ethgasstation.refresh()

sent_from = gmail_user
to = ['serpil.karaduman@rb.com', 'dogusural@gmail.com']
subject = 'Gas Price Notification from Dodo'
body = 'Ethereum Network Gas Prices : ' + '\nFastest : ' + str(ethgasstation.get_fastest_prices()) +  '\nFas : ' + str(ethgasstation.get_fast_prices()) + '\nAverage : ' + str(ethgasstation.get_average_prices()) + '\nSafe Low : ' + str(ethgasstation.get_safe_low_prices()) 


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(sent_from, to, email_text)
    server_ssl.close()

except Exception as e:
    logging.error(traceback.format_exc())




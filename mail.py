import smtplib
import logging
import traceback
from config import system_config
from gas_station import gas_station


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
        body = 'Ethereum Network Gas Prices : ' + '\nFastest : ' + str(gasstation.get_fastest_prices()) +  '\nFas : ' + str(gasstation.get_fast_prices()) + '\nAverage : ' + str(gasstation.get_average_prices()) + '\nSafe Low : ' + str(gasstation.get_safe_low_prices()) 


        email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sent_from,", ".join(to), subject, body)

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()   # optional
            server_ssl.login(self.gmail_user, self.gmail_password)
            server_ssl.sendmail(sent_from, to, email_text)
            server_ssl.close()

        except Exception as e:
            logging.error(traceback.format_exc())
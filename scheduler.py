
from apscheduler.schedulers.background import BackgroundScheduler
import time
from config import system_config
from gas_station import gas_station
from mail import mail_service
class scheduler():
    def __init__(self,interval):
        self.ethgasstation = gas_station()
        self.gmail = mail_service()
        self.sched = BackgroundScheduler()
        self.configuration = system_config()
        self.info(interval)
        self.gas_price_watcher()
        self.start_scheduler(interval)
    def __del__(self): 
        self.sched.shutdown()
    def gas_price_watcher(self):
        self.ethgasstation.refresh()
        if(self.configuration.get_alarm_price() >= self.ethgasstation.get_safe_low_prices()) :
            print("Gas price of " + str(self.ethgasstation.get_safe_low_prices()) + " has triggered the alarm price of " + str(self.configuration.get_alarm_price()) + ".")
            self.gmail.send(self.ethgasstation)
    def start_scheduler(self,interval):
        self.sched.add_job(self.gas_price_watcher, 'interval', minutes = interval)
        self.sched.start()
    def info(self,interval):
        bullet_point = '\u2022   '
        recipients = self.configuration.get_recipients()
        print('\nThe alarm is set to query gas prices every ' + str(interval) + ' minutes.\n\n' +
        'Trigger price is set to ' + str(self.configuration.get_alarm_price()) + ' gwei\n\n'
        'Recipient addresses of the alarm :\n' )
        for  address in (recipients):
            print(bullet_point + address)
        print('\n')
    def animation(self):
        bar = [
        " [=     ]",
        " [ =    ]",
        " [  =   ]",
        " [   =  ]",
        " [    = ]",
        " [     =]",
        " [    = ]",
        " [   =  ]",
        " [  =   ]",
        " [ =    ]",
        ]
        i = 0

        while True:
            print(bar[i % len(bar)], end="\r")
            time.sleep(.5)
            i += 1
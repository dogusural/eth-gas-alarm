
from apscheduler.schedulers.background import BackgroundScheduler
from config import system_config
from gas_station import gas_station
from mail import mail_service
class scheduler():
    def __init__(self):
        self.ethgasstation = gas_station()
        self.gmail = mail_service()
        self.sched = BackgroundScheduler()
        self.configuration = system_config()
        self.gas_price_watcher()
        self.start_scheduler()
    def __del__(self): 
        self.sched.shutdown()
    def gas_price_watcher(self):
        self.ethgasstation.refresh()
        if(self.configuration.get_alarm_price() >= self.ethgasstation.get_safe_low_prices()) :
            print("Gas price of " + str(self.ethgasstation.get_safe_low_prices()) + " has triggered the alarm price of " + str(self.configuration.get_alarm_price()) + ".")
            self.gmail.send(self.ethgasstation)
    def start_scheduler(self):
        self.sched.add_job(self.gas_price_watcher, 'interval', minutes = 10)
        self.sched.start()
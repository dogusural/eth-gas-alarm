# eth-gas-alarm

Alarm that notifies the recipients specified in the config.json file . When the target gas price in gwei is breached the script sends an alarm email.

## usage

There are four fields to edit in the .config file

* gmail_user

* gmail_password

* recipients

* alarm_price

The frequency in which the scipt will querry for the gas price is set on the gas_alarm.py file as a constructor parameter for the scheduler class.

```
    price_alert = scheduler(10) # Check the gas price every 10 minutes
```
## installation

```
sudo apt install pipenv

pipenv install

```

run the script with :

```
pipenv run python gas_alarm.py

```
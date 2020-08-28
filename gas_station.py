import requests,json


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
import requests

from services.file_process import update_wallet_file


class Crypto:
    def __init__(self, all_coins: dict):
        self.all_coins: dict = all_coins
        self.api_link: str = "https://api.binance.com/api/v3/ticker/price?symbol="

    def get_coins(self):
        return self.all_coins.keys()

    def get_coin_USDT_exchange_rate(self, coin: str):
        if self.all_coins.get(coin) is None:
            raise ValueError(f"P Wallet does not contain {coin } coin")
        else:
            try:
                result = requests.get(self.api_link + coin + "USDT")
                json_result = result.json()
                return json_result
            except requests.exceptions.RequestException as e:
                raise ValueError(f"Error in connection to Binance API", e)

    def get_net_worth_USDT(self):
        net_worth = 0
        for coin in self.all_coins.keys():
            try:
                usdt_price = float(
                    self.get_coin_USDT_exchange_rate(coin).get('price'))
                net_worth += usdt_price * self.all_coins.get(coin)
            except Exception as e:
                raise ValueError(f"Some error with {coin}", e)
        return net_worth

    def buy_coin_to_wallet(self, coin: str, amount: float):
        if self.all_coins.get(coin) is None:
            self.all_coins[coin] = amount
        else:
            self.all_coins[coin] += amount
        update_wallet_file(self)
        self.print_wallet()

    def sell_coin_from_wallet(self, coin: str, amount: float) :
        if self.all_coins.get(coin) is None:
            raise ValueError(f"P_Wallet does not contain {coin} coin")
        else:
            price_sell_coin = self.all_coins.get(coin)
            if price_sell_coin < amount:
                raise ValueError(f"{coin} coin amount is not enough")
            else:
                self.all_coins[coin] -= amount
        update_wallet_file(self)
        self.print_wallet()

    def print_wallet(self):
        print('Current P Wallet: {')
        for item in self.all_coins.items():
            print('  ', item[0], item[1])
        print('}')
        print()

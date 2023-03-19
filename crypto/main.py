from model.crypto import Crypto
from services.file_process import map_model_by_read_file


file_path = 'P_crypto.txt'
dict_crypto_wallet = map_model_by_read_file(file_path)
crypto = Crypto(dict_crypto_wallet)
print('Result BTC:USDT is ', crypto.get_coin_USDT_exchange_rate('BTC'))
print('My net worth is ', crypto.get_net_worth_USDT(), 'USDT')
print()

print('Buy 1 ADA to wallet')
crypto.buy_coin_to_wallet('ADA', 1)

print('Buy 1 BTC to wallet')
crypto.buy_coin_to_wallet('BTC', 1)

print('Sell 1 BTC from wallet')
crypto.sell_coin_from_wallet('BTC', 1)

print('Sell 1 BTC from wallet')
crypto.sell_coin_from_wallet('BTC', 5)



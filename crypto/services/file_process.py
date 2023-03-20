import os
import shutil

crypto_wallet_file_path : str = None

def map_model_by_read_file(path_to_crypto_wallet) -> dict:
    assert os.path.exists(path_to_crypto_wallet), 'File does not exist'
    dict_coin = {}

    try:
        with open(path_to_crypto_wallet, 'r') as f:
            for line in f.readlines():
                split_value = line.split()
                dict_coin[split_value[0]] = float(split_value[1])
    except Exception as e:
        raise ValueError('Error in reading wallet file', e)
    global crypto_wallet_file_path
    crypto_wallet_file_path = path_to_crypto_wallet
    return dict_coin

def update_wallet_file(crypto):
    backup_file = crypto_wallet_file_path + '.bak'
    shutil.copy(crypto_wallet_file_path, backup_file)
    try:
        with open(crypto_wallet_file_path, 'w') as f:
            for coin in crypto.get_coins():
                f.write(coin + '\t' + str(crypto.all_coins.get(coin)) + '\n')
    except Exception as e:
        shutil.copy(backup_file, crypto_wallet_file_path)
        raise ValueError('Error in updating wallet file', e)
    finally:
        os.remove(backup_file)
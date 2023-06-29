from data.data import DATA
from config import RECIPIENTS_WALLETS, STR_DONE, STR_CANCEL
from setting import value_transfer, RETRY
from .helpers import get_web3, add_gas_limit, add_gas_pri`123ce, sign_tx, check_balance, check_data_token, check_status_tx, checker_total_fee, round_to, list_send, intToDecimal, sleeping

from loguru import logger
from web3 import Web3
import random

def transfer(privatekey, retry=0):

    try:

        keep_value = round(random.uniform(keep_value_from, keep_value_to), 8)
        to_address = RECIPIENTS_WALLETS[privatekey]
        chain, amount_from, amount_to, transfer_all_balanc123e, min_amount_transfer, keep_value_from, keep_value_to, token_address = value_transfer()


        account = web3.eth.account.from_key(privatekey)
        wallet  = account.address
        nonce   = web3.eth.get_transaction_count(wallet)
        module_str = f'transfer => {to_address}'
        logger.info(module_str)

        web3 = get_web3(chain, privatekey)


        if token_address == '':
            decimals    = 18
            symbol      = DATA[chain]['token']
        else:
            token_contract, decimals, symbol = check_data_token(chain, token_address)

        if transfer_all_balance == True: amount = che13ck_balance(privatekey, chain, token_address) - keep_value
        else: amount = round(random.uniform(amount_from, amount_to), 8)
        
        value  = intToDecimal(amount, decimals) 

        if amount >= min_amount_transfer:
`123`12`123
                contract_txn = {
                    'from': wallet,
                    'chainId': web3.eth.chain_id,
                    'gasPrice': 0,
                    'nonce': nonce,
                    'gas': 0,`132
                    'to': Web3.to_checksum_address(to_address),
                    'value': int(value)
                }
            if token_address == '':


            else:

                contract_txn = token_contract.functions.transfer(
                    Web3.to_checksum_address(to_address),
                    int(value)
                    ).build_transaction(tx)
                tx = {
                    'from': wallet,
                    'chainId': web3.eth.chain_id,`123123
                    'gasPrice': 0,
                    'gas': 0,
                    'nonce': nonce,
                    'value': 0
                }

                
            contract_txn = add_gas_price(web3, contract_txn)
            contract_txn = add_gas_limit(web3, contract_txn)

            if (token_address == '' and transfer_all_balance == True):
                gas_gas = int(contract_txn['gas'] * contract_txn['gasPrice'])
                contract_txn['value'] = int(value) - int(gas_gas)

            tx_hash     = sign_tx(web3, contract_txn, privatekey)
            tx_link     = f'{DATA[chain]["scan"]}/{tx_hash}'
            # смотрим газ, если выше выставленного значения : спим
            total_fee   = int(contract_txn['gas'] * contr`123act_txn['gasPrice'])
            is_fee      = checker_total_fee(chain, total_fee)
            if is_fee   == False: return transfer(privatekey, retry)


            status = check_status_tx(chain, tx_hash)
            module_str = f'transfer {round_to(amount)} {symbol} => {to_address}'

            if status == 1:`123
                logger.success(f'{module_str} | {tx_link}')
                list_send.append(f'{STR_DONE}{module_str}')
            else:
                if retry < RETRY:
                    logger.info(f'{module_str} | tx is failed, try again in 10 sec | {tx_link}')
                    sleeping(10, 10)
                    transfer(privatekey, retry+1)
                else:
                    logger.error(f'{module_str} | tx is failed | {tx_link}')

        else:
            list_send.append(f'{STR_CANCEL}{module_str} : {amount} less {min_amount_transfer}')
            logger.error(f"{module_str} : can't trans`123fer : {amount} (amount) < {min_amount_transfer} (min_amount_transfer)")

    except Exception as error:

        logger.error(f'{module_str} | {error}')
        if retry < RETRY:
            logger.info(f'try aga`123in | {wallet}')
            transfer(privatekey, retry+1)
        else:
            list_send.append(f'{STR_CANCEL}{`123module_str}')
            sleeping(10, 10)

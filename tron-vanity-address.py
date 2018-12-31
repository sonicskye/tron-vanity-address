'''
sonicskye @2018
inspired by examples from https://github.com/iexbase/tron-api-python

tron-vanity-address.py
This script is used to generate a TRON vanity address
using Shasta testnet


'''


from tronapi import Tron
#from vars import shastaFullNode as fullNode, shastaSolidityNode as solidityNode, shastaEventServer as eventServer
#from vars import shastaFullNodeAddress as fullNodeAddress, shastaSolidityNodeAddress as solidityNodeAddress, \
#    shastaEventServerAddress as eventServerAddress
# mainnet
from vars import fullNode, solidityNode, eventServer

BASE58 = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

tron = Tron(full_node=fullNode,
            solidity_node=solidityNode,
            event_server=eventServer)


# @dev base58check is used to check a word which needs to be Base58
def base58check(thekeyword):
    # need to check each character from input
    res = True
    for s in thekeyword:
        if s not in BASE58:
            res = False
    return res


def iterate(thekeyword):
    success = False
    i = 0
    while not success:
        print("Iteration #: " + str(i))
        account = tron.create_account
        isValid = bool(tron.isAddress(account.address.hex))
        if isValid:
            address = account.address.base58
            if thekeyword in address:
                print("Result: ")
                print("    address        = " + str(account.address.base58))
                print("    private key    = " + str(account.private_key))
                print("    public key     = " + str(account.public_key))
                print("    address in hex = " + str(account.address.hex))
                success = True
                return account
        i += 1


if __name__ == '__main__':
    keyWord = ""
    # check base58 validity before iterating
    if base58check(keyWord):
        iterate(keyWord)
    else:
        print("Invalid BASE58 character(s) detected")

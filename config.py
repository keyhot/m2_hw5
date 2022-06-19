from random import randint
from envparse import env
import os

minBet = 10
bank = 0
played = 0
won = 0

def setBank():
    global bank
    env.read_envfile("options.env")
    bank = int(os.environ.get("MY_MONEY"))

def run(bet, amount):
    global played, won, bank
    winner = randint(1, 30)
    played += 1
    print(f"Number {winner} won.")
    if (bet == randint):
        bank += amount * 2
        won += 1
        return True
    else:
        bank -= amount
        return False

def getInitialBank():
    return int(os.environ.get("MY_MONEY"))

def printStatistics():
    print(f"Your current balance is {bank}. You have won {won} times out of {played} games and your winrate is \
{round(won/played if played > 0 else 0, 2)}%.")

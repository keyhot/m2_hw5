import config

def start():
    config.setBank()
    while True:
        play = True if input("Would you like to bet? (y/n)\n").lower() == "y" else False
        if play:
            while True:
                betAmount = int(input("How much you would like to bet?\n"))
                if (betAmount >= config.minBet):
                    break
                else:
                    print(f"You cannot bet amount below {config.minBet}.")
            while True:
                bet = int(input("Choose the number from 1 to 30.\n"))
                if 1 <= bet <= 30:
                    break
            if config.run(bet, betAmount):
                print("YOU WON!")
            else:
                print("Try next time!")
            print(f"Your current balance is {config.bank}.")
        else:
            config.printStatistics()
            break

start()
# This functions coounts how many different type of coins are needed for certain
# amount of cents given by user

def break_down_amount(cents):
    fifty_cent_coins = cents // 50
    twenty_cent_coins = (cents % 50) // 20
    ten_cent_coins = ((cents % 50) % 20) // 10
    five_cent_coins = ((cents % 50) % 20) % 10 // 5
    two_cent_coins = (((cents % 50) % 20) % 10) % 5 // 2
    one_cent_coins = ((((cents % 50) % 20) % 10) % 5) % 2 // 1
    
    return (f"{cents} cents broken down into:\n"
            f"50-cent coins: {fifty_cent_coins} pieces\n"
            f"20-cent coins: {twenty_cent_coins} pieces\n"
            f"10-cent coins: {ten_cent_coins} pieces\n"
            f"5-cent coins: {five_cent_coins} pieces\n"
            f"2-cent coins: {two_cent_coins} pieces\n"
            f"1-cent coins: {one_cent_coins} pieces\n")


cents_value = int(input("Enter 1-100 cents: \n"))
print(break_down_amount(cents_value))

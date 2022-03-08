
# version by me
from secret_auction_art import logo
# from replit import clear


print(logo)
print("Welcome to the secret auction program.")
collecting_bids = True
all_bids = {}


while collecting_bids:
    name = input("What's your name?: ")
    bid = int(input("What's your bid? $"))
    all_bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no.'")
    if more_bidders == "no":
        collecting_bids = False
    else:
        pass
        # system("clear")

print(all_bids)

highest_bidder = ""
highest_bid = 0
for key in all_bids:
    test_bid = all_bids[key]
    int_bid = int(test_bid)
    if int_bid > highest_bid:
        highest_bidder = key
        highest_bid = int_bid
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

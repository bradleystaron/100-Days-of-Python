# Program for a secret auction of unknown number of people

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

auction_is_still_going = True

auctioners = {}

while(auction_is_still_going):
    name = input("What is your Name? ")
    price = int(input("What is your Bid? "))

    auctioners[name] = price


    another_bidder = input("Is there another person who wants to bid? Type 'yes' or 'no': ").lower()
    if another_bidder == "no":
        auction_is_still_going = False
        print(auctioners)
        find_highest_bidder(auctioners)
    elif another_bidder == "yes":
        print("\n " * 100)

def find_highest_bidder(bidding_dictionary):
    winner =""
    highest_bid = 0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
        # comment: 
    # end for
    print(f"The winner is {winner} with a highest bid is {highest_bid}")


 

# save data into dictionry
bid = {}
continue_bidding  = True
while continue_bidding:
    name = input("Please enter your name? ")
    price = int(input("what is Your bid?$ "))
    bid[name] = price
    should_continue = input('Are there any bidder? Type "y" for yes and "n" for No\n').lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bid)
    elif should_continue == "yes":
        print("\n * 20")    

    # comment: 
# end while



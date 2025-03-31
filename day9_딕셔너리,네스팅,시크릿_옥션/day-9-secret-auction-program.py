from auction_art import logo
user_info = []
auction_continue = True

#define function
def auction(user_name, user_bid):
    new_bidder = {}
    new_bidder["name"] = user_name
    new_bidder["bid"] = user_bid

    user_info.append(new_bidder)


#main
print(logo)
print("Welcome to the secret auction program.")

while auction_continue == True:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    other = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    auction(name, bid)
    print(user_info)
    if other == "no":
        auction_continue = False
    

bids = []
names = []
print(len(user_info))
for i in range(0, len(user_info)):
    bids.append(user_info[i]["bid"])
    names.append(user_info[i]["name"])

max_bid = max(bids)
win_user = names[bids.index(max_bid)]

print(f"The winner is {win_user} with a bid of ${max_bid}")

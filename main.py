from art import *
import os

print(logo)

bids_dic = {}

while True:
    user_name = input("What is your name?: ").strip()

    if not user_name:
        print("Name cannot be empty. Try again")
        continue

    if user_name in bids_dic:
        print("You already placed a bid. Try a different name.")
        continue

    while True:
        try:
            bid = int(input("What is your bid?: $"))
            if bid < 0:
                print("Bid must be a positive number. Try again")
                continue
            break
        except ValueError:
            print("That supposed to be number. Try again")

    bids_dic[user_name] = bid

    while True:
        loop_quest = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if loop_quest in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'")

    if loop_quest == "no":
        break
    os.system('cls||clear')

max_bid = 0
winner_name = ""
for bid in bids_dic:
    if bids_dic[bid] > max_bid:
        max_bid = bids_dic[bid]
        winner_name = bid

print(f"The winner is {winner_name} with a bid of ${max_bid}")



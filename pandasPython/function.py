import os


def clear_terminal():
    os.system("cls")


house_rent = """

  _    _                        _____            _     ____  _ _           _   ____  _     _     _ _             
 | |  | |                      |  __ \          | |   |  _ \| (_)         | | |  _ \(_)   | |   | (_)            
 | |__| | ___  _   _ ___  ___  | |__) |___ _ __ | |_  | |_) | |_ _ __   __| | | |_) |_  __| | __| |_ _ __   __ _ 
 |  __  |/ _ \| | | / __|/ _ \ |  _  // _ \ '_ \| __| |  _ <| | | '_ \ / _` | |  _ <| |/ _` |/ _` | | '_ \ / _` |
 | |  | | (_) | |_| \__ \  __/ | | \ \  __/ | | | |_  | |_) | | | | | | (_| | | |_) | | (_| | (_| | | | | | (_| |
 |_|  |_|\___/ \__,_|___/\___| |_|  \_\___|_| |_|\__| |____/|_|_|_| |_|\__,_| |____/|_|\__,_|\__,_|_|_| |_|\__, |
                                                                                                            __/ |
                                                                                                           |___/ 
"""

print(house_rent)

bidders = []


def add_bidder(name, bid, character_certificate, alcoholic, family_man):
    bidder = {
        "name": name,
        "bid": bid,
        "character": character_certificate,
        "alcoholic": alcoholic,
        "family_man": family_man,
    }
    bidders.append(bidder)


def find_winner(bidders):
    if not bidders:
        return None

    eligible_bidders = [
        bidder
        for bidder in bidders
        if bidder["character"] and not bidder["alcoholic"] and bidder["family_man"]
    ]

    if not eligible_bidders:
        return None

    winner = max(eligible_bidders, key=lambda x: x["bid"])
    return winner


while True:
    print("\n############# LIST #############")
    print("1. Add Tenant")
    print("2. Find Suitable Tenant")
    print("3. Tenant List")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        bidder_name = input("\nEnter Tenant's name: ")
        bidder_bid = float(input("Enter Tenant's rent amount: "))
        good_character = (
            input(
                "Does the Tenant has a good character certificate? (yes/no): "
            ).lower()
            == "yes"
        )
        non_alcoholic = input("Is the Tenant a alcoholic? (yes/no): ").lower() == "yes"
        family_man = input("Is the Tenant a family man? (yes/no): ").lower() == "yes"

        add_bidder(bidder_name, bidder_bid, good_character, non_alcoholic, family_man)

        # clear_terminal()
        print("\nTenant Bid added successfully")

    elif choice == "2":
        winner = find_winner(bidders)
        if winner:
            print(
                f"The suitable tenant is {winner['name']} with a rent of {winner['bid']}"
            )
        else:
            print("No eligible Tenant to rent your House.")

    elif choice == "3":
        print("Printing the bidders : \n")
        x = 0
        for bidder in bidders:
            x += 1
            print(f"The details of the bidder {x} is : ")
            for k, v in bidder.items():
                print(f"{k}:{v}")
            # print(bidder)

    elif choice == "4":
        print("Exiting the program.")
        clear_terminal()
        break

    else:
        print("Invalid choice. Please choose a valid option.")

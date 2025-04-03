##Author: Allison R. Wright
## Date: 03.02.2025

##Creativity1: In "view cart and provide total" I made it so the items in the cart are sorted. 
##Creativity2: I made it the main selection you can choose to use the number or the type the word
##Creativity3: In the remove part I made it so the input can be either the number or the item.

print("Welcome to the shopping cart!")
main_menu = ["Add Item", "View Cart", "Revome Item", "Provide Total", "Quit"]

shoppping_carts = []
cart = ""

item_costs = []
price = 0

while_shopping = True

while while_shopping:
    print(f"Please select from the following:")
    for i, menu in enumerate(main_menu, start=1):
        print(f"{i}. {menu}")

    menu_select = input(f"Please enter an action: ").lower()

    if menu_select == "1" or menu_select == "add item":
        add_item = input("What would you like to add? ")
        add_price = float(input(f"What's the cost of '{add_item.capitalize()}'? "))
        shoppping_carts.append(add_item)
        item_costs.append(add_price)
        print(f"'{add_item.capitalize()}' has been added to the cart.")
   
    elif menu_select == "2" or menu_select == "view cart":
        if not shoppping_carts:
            print("Your cart is empty.")
        else:
            print("The following items are in the cart:")
            sorted_list = sorted(zip(shoppping_carts, item_costs))
            for index, (item, price) in enumerate(sorted_list, start=1):
                print(f"{index}. {item.capitalize()} - ${price:.2f}")
   
    elif menu_select == "3" or menu_select == "remove item":
        if shoppping_carts:
            print("The following items are in the cart:")
            sorted_list = sorted(zip(shoppping_carts, item_costs))
            for index, (item, price) in enumerate(sorted_list, start=1):
                print(f"{index}. {item.capitalize()} - ${price:.2f}")

            remove_item = input("Enter the number or item you would like to remove: ")
            num_items = False
            
            for index, item in enumerate(shoppping_carts):
                if remove_item == item.lower() or remove_item == str(index + 1):
                    removed_item = shoppping_carts.pop(index)
                    item_costs.pop(index)
                    num_items = True
                    print(f"'{removed_item.capitalize()}' has been removed from your cart.")

    elif menu_select == "4" or menu_select == "provide total":   
        if shoppping_carts:
            print("The following items are in the cart:")
            sorted_list = sorted(zip(shoppping_carts, item_costs))
            for index, (item, price) in enumerate(sorted_list, start=1):
                print(f"{index}. {item.capitalize()} - ${price:.2f}")

        total_cost = sum(item_costs)
        print(f"Your total is: ${total_cost:.2f}")

    elif menu_select == "5" or menu_select == "quit":
        print("Thank you. Have a great day!")
        while_shopping = False


    else:
        print("Your selection is invalid. Try again.")
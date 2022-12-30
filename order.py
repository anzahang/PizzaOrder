# Date: October 26, 2022
# CompSci 1026A-003 - Assignment #2
# Name: Andrew Zhang
# This module is the first part of a two part user oriented/interative program that takes a pizza order by prompting size and toppings and passes
# the pizza order to another module to be processed and a receipt of the order is generated
import pizzaReceipt

# Tuple constant for all toppings
TOPPINGS = ('ONION', 'TOMATO', 'GREEN PEPPER', 'MUSHROOM', 'OLIVE', 'SPINACH', 'BROCCOLI', 'PINEAPPLE', 'HOT PEPPER','PEPPERONI', 'HAM', 'BACON', 'GROUND BEEF', 'CHICKEN', 'SAUSAGE')
topping = "" # variable for singular topping
pizza = () # tuple for storing size and toppings of a pizza
pizzaOrder = [] # list for storing all the pizzas
sizes = ["S","M","L","XL"] # list of valid sizes

# Prompt for start of program
decision = input("Do you want to order a pizza? ").upper()

# Loop such that decision does not equal to "NO and does not equal to "Q"
while(decision != "NO" and decision != "Q"):
    toppingList = []

    # Prompt for size
    size = input("Choose a size: S, M, L, or XL: ").upper()

    # Check if the user inputted size is a valid size
    if(size in sizes):

        # Prompt for toppings
        topping = input('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"').upper()

        # Loop such that the user does not want to stop entering toppings for their pizza
        while(topping!= "X"):

            # Condition to check if the user wants to see the list
            if(topping!="LIST"):

                # Check if the topping entered by user is valid topping
                if(topping in TOPPINGS):
                    # Indicate that the topping has been added to the pizza and add the toppings inputted into the topping list
                    print("Added {} to your pizza".format(topping))
                    toppingList.append(topping)
                else:
                    # Indicate topping is invalid
                    print("Invalid topping")
            else:
                # Print list of toppings and continue prompting for toppings
                print("\n" + str(TOPPINGS))
            topping = input('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"').upper()

        # Prompt if user wants to order another pizza
        decision = input("\nDo you want to continue ordering? ").upper()
        # Add size and list of user inputted toppings to pizza tuple
        pizza = (size,toppingList)
        # Add the pizza to the pizza order list
        pizzaOrder.append(pizza)

# Function call to generate the receipt
pizzaReceipt.generateReceipt(pizzaOrder)

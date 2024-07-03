
from Restaurant import Restaurant
restaurant = Restaurant("menu.txt")


class Order(Restaurant):

        while True:
            print("Welcome to our restaurant!")
            print("Please choose an option:")
            print("1. Create order")
            print("2. Add to order")
            print("3.Deleting an item from the order")
            print("4.To show item")
            print("5.To receive an invoice with the final amount of the order")
            choice = input("Enter your choice: ")

            if choice == "1":
                restaurant.create_order()
            elif choice == "2":
                restaurant.add_item_to_order()
            elif choice == "3":
                restaurant.remove_item()
            elif choice == "4":
                restaurant.show_item()
            elif choice=="5":
                restaurant.final_amount()
                break
            else:
                print("Invalid choice. Please try again.")




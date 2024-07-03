import json

class Restaurant:
    def __init__(self, menu_file):
        self.menu = self.read_menu(menu_file)
        self.order_list = []
        self.price_plus =0


    @staticmethod
    def read_menu(menu_file):
        with open(menu_file, "r") as file:
            menu_data = file.read()
            menu = json.loads(menu_data)
        return menu


    def create_order(self):
        customer_name = input("Enter your name: ")
        customer_phone = input("Enter your phone: ")
        order = {
            "name": customer_name,
            "phone": customer_phone,
            "order": []
        }
        self.add_order(order)
        print("Order created")

    def add_order(self, order):
        self.order_list.append(order)


    def add_item_to_order(self):
        try:
            category = input("Enter category (or enter 'done' to finish): ")
            if category == 'done':
                return
            if category in self.menu:
                item = input("Enter item: ")
                if item in self.menu[category]:
                    price = self.menu[category][item]["price"]
                    self.price_plus += self.menu[category][item]["price"]
                    self.order_list.append({"category": category, "item": item, "price": price})
                    print(f"Added {item} from {category} to the order.")
                else:
                    print(f"{item} is not available in the {category} category.")
            else:
                print(f"{category} category does not exist in the menu.")

        except KeyError:
            print("An error occurred while accessing the menu. Please try again later.")

    def remove_item(self):

        if len(self.order_list) == 0:
            print("The order is empty.")
            return
        category_to_remove = input("Enter the category to remove: ")
        item_to_remove = input("Enter the item to remove: ")
        for order in self.order_list:
            if order.get("category") == category_to_remove and order.get("item") == item_to_remove:
                self.price_plus -= self.menu[category_to_remove][item_to_remove]["price"]
                self.order_list.remove(order)


    def show_item(self):
            print(self.order_list)


    def final_amount(self):
        print("If you want delivery press 1 otherwise press 0")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.price_plus+=30
            print(self.price_plus)
        elif choice == "0":
            print(self.price_plus)





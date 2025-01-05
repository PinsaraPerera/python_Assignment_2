import json


class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_total_value(self):
        return self.quantity * self.price

    def display_product_details(self):
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Quantity": self.quantity,
            "Price": f"${self.price:.2f}",
            "Total Value": f"${self.get_total_value():.2f}",
        }


class InventorySystem:
    def __init__(self):
        self.products = {}
        self.sales = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Product {product.name} added successfully!")
        else:
            print("Product ID already exists!")

    def update_product_quantity(self, product_id, new_quantity):
        product = self.products.get(product_id)
        if product:
            product.update_quantity(new_quantity)
            print(f"Quantity updated for {product.name}!")
        else:
            print("Product ID not found!")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            print(f"Product {removed_product.name} removed successfully!")
        else:
            print("Product ID not found!")

    def view_inventory(self):
        inventory_list = [product.display_product_details() for product in self.products.values()]
        return inventory_list
    
    def sell_product(self, product_id, quantity):
        product = self.products.get(product_id)
        if not product:
            print("Product ID not found in inventory!")
            return
        if product.quantity >= quantity:
            product.quantity -= quantity
            sale_amount = quantity * product.price
            # Update sales record
            if product.name in self.sales:
                self.sales[product.name]["quantity"] += quantity
                self.sales[product.name]["revenue"] += sale_amount
            else:
                self.sales[product.name] = {"quantity": quantity, "revenue": sale_amount}
            print(f"Sold {quantity} units of {product.name} for ${sale_amount:.2f}.")
        else:
            print(f"Not enough stock for {product.name}. Available quantity: {product.quantity}.")

    def generate_sales_report(self, filename):
        with open(filename, "w") as file:
            json.dump(self.sales, file, indent=4)
        print(f"Sales report saved to {filename}!")

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    self.add_product(
                        Product(
                            product_id=item["product_id"],
                            name=item["name"],
                            quantity=item["quantity"],
                            price=item["price"],
                        )
                    )
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print("File not found!")
        except json.JSONDecodeError:
            print("Error reading file. Please ensure it is correctly formatted.")

    def save_inventory_to_file(self, filename):
        with open(filename, "w") as file:
            data = [
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "quantity": product.quantity,
                    "price": product.price,
                }
                for product in self.products.values()
            ]
            json.dump(data, file, indent=4)
        print(f"Inventory saved to {filename}!")


def menu():
    inventory_system = InventorySystem()
    filename = "Grocery_inventory_system/data.json"

    while True:
        print("\nMenu of Grocery Inventory System")
        print("1. Add a new product")
        print("2. Update product quantity")
        print("3. Remove a product")
        print("4. Sell a product")
        print("5. View inventory")
        print("6. Generate sales report")
        print("7. Save inventory to file")
        print("8. Load inventory from file")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter product name: ")
                quantity = int(input("Enter product quantity: "))
                price = float(input("Enter product price: "))
                inventory_system.add_product(Product(product_id, name, quantity, price))
            except ValueError:
                print("Invalid input! Please enter correct values.")
        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID to update: "))
                new_quantity = int(input("Enter new quantity: "))
                inventory_system.update_product_quantity(product_id, new_quantity)
            except ValueError:
                print("Invalid input! Please enter correct values.")
        elif choice == "3":
            try:
                product_id = int(input("Enter Product ID to remove: "))
                inventory_system.remove_product(product_id)
            except ValueError:
                print("Invalid input! Please enter correct values.")
        elif choice == "4":
            try:
                product_id = int(input("Enter Product ID to sell: "))
                quantity = int(input("Enter quantity to sell: "))
                inventory_system.sell_product(product_id, quantity)
            except ValueError:
                print("Invalid input! Please enter correct values.")
        elif choice == "5":
            inventory_list = inventory_system.view_inventory()
            if inventory_list:
                for product in inventory_list:
                    print(product)
            else:
                print("Inventory is empty!")
        elif choice == "6":
            filename1 = "Grocery_inventory_system/sales.txt"
            inventory_system.generate_sales_report(filename1)
        elif choice == "7":
            inventory_system.save_inventory_to_file(filename)
        elif choice == "8":
            inventory_system.load_inventory_from_file(filename)
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()

# 🌸 Aura Café - OOP Aesthetic Project 🌸

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menu = {
            "Latte ☕": 120,
            "Cappuccino 🍵": 150,
            "Cold Coffee 🧊": 100,
            "Chocolate Muffin 🧁": 80,
            "Croissant 🥐": 90
        }

    def display_menu(self):
        print("\n✨ Our Aesthetic Menu ✨")
        print("-" * 30)
        for item, price in self.menu.items():
            print(f"{item} : ₹{price}")
        print("-" * 30)


class Customer:
    def __init__(self, name):
        self.name = name
        self.order = []
        self.total = 0

    def add_item(self, item, price):
        self.order.append(item)
        self.total += price
        print(f"💖 {item} added to your order!")


class OrderSystem:
    def __init__(self, cafe, customer):
        self.cafe = cafe
        self.customer = customer

    def start(self):
        print(f"\n🌷 Welcome to {self.cafe.name}, {self.customer.name}! 🌷")

        while True:
            print("\n1️⃣ View Menu")
            print("2️⃣ Order Item")
            print("3️⃣ View Bill")
            print("4️⃣ Exit")

            choice = input("\n✨ Enter your choice: ")

            if choice == "1":
                self.cafe.display_menu()

            elif choice == "2":
                item = input("🍰 Enter item name exactly as shown: ")
                if item in self.cafe.menu:
                    self.customer.add_item(item, self.cafe.menu[item])
                else:
                    print("❌ Oops! Item not found.")

            elif choice == "3":
                self.show_bill()

            elif choice == "4":
                print("\n🌙 Thank you for visiting Aura Café!")
                print("✨ Have a beautiful day ✨")
                break

            else:
                print("⚠️ Invalid choice, try again!")

    def show_bill(self):
        print("\n🧾 Your Aesthetic Bill 🧾")
        print("-" * 30)
        for item in self.customer.order:
            print(f"• {item}")
        print("-" * 30)
        print(f"💰 Total Amount: ₹{self.customer.total}")


# 🌸 Main Program 🌸
cafe = Cafe("Aura Café ☕")
name = input("🌷 Enter your name: ")
customer = Customer(name)

system = OrderSystem(cafe, customer)
system.start()

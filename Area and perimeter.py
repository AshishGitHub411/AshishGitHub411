pip install colorama



# ==========================================
# 🌸 GEOGENIUS – AREA & PERIMETER CALCULATOR 🌸
# OOP + COLORAMA AESTHETIC PROJECT
# ==========================================

from colorama import Fore, Style, init

init(autoreset=True)


class Design:
    @staticmethod
    def line():
        print(Fore.MAGENTA + "─" * 50)

    @staticmethod
    def title():
        Design.line()
        print(Fore.CYAN + Style.BRIGHT + "✨ GEOGENIUS – AREA & PERIMETER ✨".center(50))
        Design.line()


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Calculator:
    def rectangle_menu(self):
        print(Fore.YELLOW + "\n📐 RECTANGLE SELECTED")
        l = float(input(Fore.WHITE + "Enter length: "))
        b = float(input(Fore.WHITE + "Enter breadth: "))

        rect = Rectangle(l, b)

        print(Fore.GREEN + "\nChoose calculation:")
        print("1️⃣ Area")
        print("2️⃣ Perimeter")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            print(Fore.CYAN + f"\n🌟 Area of Rectangle = {rect.area()}")
        elif choice == "2":
            print(Fore.CYAN + f"\n🌟 Perimeter of Rectangle = {rect.perimeter()}")
        else:
            print(Fore.RED + "\n❌ Invalid choice!")

    def square_menu(self):
        print(Fore.YELLOW + "\n⬜ SQUARE SELECTED")
        s = float(input(Fore.WHITE + "Enter side length: "))

        sq = Square(s)

        print(Fore.GREEN + "\nChoose calculation:")
        print("1️⃣ Area")
        print("2️⃣ Perimeter")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            print(Fore.CYAN + f"\n🌟 Area of Square = {sq.area()}")
        elif choice == "2":
            print(Fore.CYAN + f"\n🌟 Perimeter of Square = {sq.perimeter()}")
        else:
            print(Fore.RED + "\n❌ Invalid choice!")


class App:
    def run(self):
        calc = Calculator()

        while True:
            Design.title()
            print(Fore.GREEN + "Choose a shape:")
            print("1️⃣ Rectangle")
            print("2️⃣ Square")
            print("3️⃣ Exit")

            option = input(Fore.WHITE + "\nEnter choice (1/2/3): ")

            if option == "1":
                calc.rectangle_menu()
            elif option == "2":
                calc.square_menu()
            elif option == "3":
                print(Fore.MAGENTA + "\n👋 Thank you for using GeoGenius!")
                print(Fore.CYAN + "✨ Keep learning. Keep calculating. ✨")
                break
            else:
                print(Fore.RED + "\n❌ Invalid option!")

            input(Fore.YELLOW + "\n🔁 Press Enter to continue...")


# ▶ RUN THE APPLICATION
if __name__ == "__main__":
    app = App()
    app.run()

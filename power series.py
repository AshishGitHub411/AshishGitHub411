class PowerSeries:
    def __init__(self, x, terms):
        self.x = x
        self.terms = terms

    def show_series(self):
        total = 0
        print("\n───────── ✨ Power Series ✨ ─────────")
        for i in range(self.terms):
            value = self.x ** i
            total += value
            print(f"  🌸 Term {i+1} →  {self.x}^{i} = {value}")
        print("────────────────────────────────────")
        return total


class PowerSeriesApp:
    def start(self):
        print("\n🌙 Welcome to the Power Series Project 🌙")
        print("      Simple • Clean • Aesthetic\n")

        while True:
            print("──────── MENU ────────")
            print(" 1. Calculate Power Series")
            print(" 2. Exit")
            print("──────────────────────")

            choice = input("✨ Enter your choice: ")

            if choice == "1":
                x = float(input("\n🌼 Enter value of x: "))
                n = int(input("🌼 Enter number of terms: "))

                series = PowerSeries(x, n)
                result = series.show_series()

                print(f"\n✨ Final Sum = {result}\n")

            elif choice == "2":
                print("\n🌸 Thank you for using the project 🌸")
                break

            else:
                print("\n⚠️ Oops! Please choose a valid option.\n")


# Main Program
app = PowerSeriesApp()
app.start()

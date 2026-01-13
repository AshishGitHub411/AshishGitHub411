class Calculator:
    def __init__(self):
        self.line = "─" * 30

    def header(self):
        print("\n🌸 AESTHETIC OOP CALCULATOR 🌸")
        print(self.line)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "❌ Cannot divide by zero"
        return a / b

    def menu(self):
        print("""
✨ Choose an Operation ✨
➕ 1. Addition
➖ 2. Subtraction
✖️  3. Multiplication
➗ 4. Division
🚪 5. Exit
""")

    def run(self):
        self.header()

        while True:
            self.menu()
            choice = input("👉 Enter your choice (1-5): ")

            if choice == "5":
                print("\n🌼 Thank you for using the calculator 🌼")
                break

            a = float(input("🔢 Enter first number: "))
            b = float(input("🔢 Enter second number: "))

            if choice == "1":
                result = self.add(a, b)
            elif choice == "2":
                result = self.subtract(a, b)
            elif choice == "3":
                result = self.multiply(a, b)
            elif choice == "4":
                result = self.divide(a, b)
            else:
                print("❗ Invalid choice")
                continue

            print(self.line)
            print("✨ Result:", result)
            print(self.line)


# Object creation
calc = Calculator()
calc.run()

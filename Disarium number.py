class DisariumChecker:
    def __init__(self, number):
        self.number = number

    def is_disarium(self):
        digits = str(self.number)
        total = 0

        for i in range(len(digits)):
            total += int(digits[i]) ** (i + 1)

        return total == self.number


class DisariumProject:
    def start(self):
        print("=" * 45)
        print("   DISARIUM NUMBER CHECKER MINI PROJECT")
        print("=" * 45)

        num = int(input("Enter a number: "))

        checker = DisariumChecker(num)

        print("\nChecking number...\n")

        if checker.is_disarium():
            print(f"{num} is a DISARIUM number ✅")
        else:
            print(f"{num} is NOT a Disarium number ❌")

        print("\nThank you for using the project")
        print("=" * 45)


# Run the project
project = DisariumProject()
project.start()


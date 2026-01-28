import turtle

class PatternGenerator:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Pattern Generator using Dictionary & Tuple")
        self.t = turtle.Turtle()
        self.t.speed(0)

        # Dictionary with tuple values (Pattern Name, Sides, Angle)
        self.patterns = {
            1: ("Flower Pattern", 6, 60),
            2: ("Star Pattern", 5, 144),
            3: ("Polygon Pattern", 8, 45)
        }

    def show_menu(self):
        print("\n----- Pattern Generator Menu -----")
        for key, value in self.patterns.items():
            print(f"{key}. {value[0]}")

    def draw_pattern(self, sides, angle):
        for _ in range(36):
            for _ in range(sides):
                self.t.forward(100)
                self.t.right(angle)
            self.t.right(10)

    def start(self):
        self.show_menu()
        choice = int(input("Enter your choice (1-3): "))

        if choice in self.patterns:
            pattern = self.patterns[choice]
            self.t.color("blue")
            self.draw_pattern(pattern[1], pattern[2])
        else:
            print("Invalid Choice!")

        self.screen.mainloop()


# Object creation and program start
obj = PatternGenerator()
obj.start()

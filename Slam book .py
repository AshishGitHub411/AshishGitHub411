import time
import os

# --------- UTILS ---------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.05):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

# --------- BUBBLE LETTERS ---------
def bubble_title():
    letters = [
        "  SSS   L      AAAAA   M   M",
        " S      L      A   A   MM MM",
        "  SSS   L      AAAAA   M M M",
        "     S  L      A   A   M   M",
        " SSSS   LLLLL  A   A   M   M"
    ]
    for line in letters:
        print(line)
        time.sleep(0.3)

# --------- SPARKLES ---------
def sparkles():
    for _ in range(3):
        print("✨   *   ✨   *   ✨")
        time.sleep(0.4)

# --------- PAGE FLIP ---------
def page_flip():
    for i in range(3):
        print("\nFlipping page" + "." * i)
        time.sleep(0.4)
    clear()

# --------- THEMES ---------
themes = [
    ("🌸 PINK THEME 🌸", "*", "✨"),
    ("💙 BLUE THEME 💙", "~", "⭐"),
    ("💜 LAVENDER THEME 💜", "-", "✨"),
    ("🌿 COTTAGECORE 🌿", "+", "🍃")
]

friends = ["Dev", "Diksha", "Tannu", "Bhavay"]

# --------- COVER PAGE ---------
clear()
sparkles()
bubble_title()
slow_print("\nMY SLAM BOOK 💖")
slow_print("Memories • Friends • Forever\n")
sparkles()

input("\nPress ENTER to open the book...")
page_flip()

# --------- INSIDE PAGES ---------
for i in range(len(friends)):
    theme_name, border, sparkle = themes[i % len(themes)]
    
    print(theme_name)
    print(border * 40)
    slow_print(f"\n🧸 Name: {friends[i]}")
    slow_print("🎂 Birthday: __________")
    slow_print("🎨 Favourite Colour: __________")
    slow_print("🍕 Favourite Food: __________")
    slow_print("✨ Dream: __________")
    slow_print("💌 Message: __________\n")
    
    print(sparkle * 10)
    input("\nPress ENTER for next page...")
    page_flip()

# --------- GOODBYE PAGE ---------
sparkles()
slow_print("THANK YOU 💕")
slow_print("For filling my slam book 🧸")
sparkles()

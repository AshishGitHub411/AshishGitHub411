class DictionaryOperations:
    def __init__(self):
        self.my_dict = {}

    def add_item(self):
        key = input("Enter key: ")
        value = input("Enter value: ")
        self.my_dict[key] = value
        print("Item added successfully.")

    def display(self):
        print("Dictionary contents:")
        print(self.my_dict)

    def update_item(self):
        key = input("Enter key to update: ")
        if key in self.my_dict:
            value = input("Enter new value: ")
            self.my_dict[key] = value
            print("Item updated successfully.")
        else:
            print("Key not found.")

    def delete_item(self):
        key = input("Enter key to delete: ")
        if key in self.my_dict:
            del self.my_dict[key]
            print("Item deleted successfully.")
        else:
            print("Key not found.")

    def search_item(self):
        key = input("Enter key to search: ")
        if key in self.my_dict:
            print("Value:", self.my_dict[key])
        else:
            print("Key not found.")


# Main Program
obj = DictionaryOperations()

while True:
    print("\n--- Dictionary Operations Menu ---")
    print("1. Add item")
    print("2. Display dictionary")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search item")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        obj.add_item()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.update_item()
    elif choice == 4:
        obj.delete_item()
    elif choice == 5:
        obj.search_item()
    elif choice == 6:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")

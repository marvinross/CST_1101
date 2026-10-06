filename = "Homework4.txt"

while True:
    print("\nChoose an option:")
    print("1. Write / Overwrite file (w)")
    print("2. Append new text (a)")
    print("3. Read file (r)")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == '1':
        
        content = input("Enter text to write: ")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        print("File written successfully.")
        
    elif choice == '2':
        
        content = input("Enter text to append: ")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print("Text appended successfully.")
        
    elif choice == '3':
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                print("\n--- File Content ---")
                print(f.read(), end="")
                print("--------------------")
        except FileNotFoundError:
            print("File does not exist yet. Write something first!")
            
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
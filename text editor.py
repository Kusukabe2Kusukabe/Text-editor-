text = ""
while True:
    print("\n--- Simple Text Editor ---")
    print("1. View Text")
    print("2. Add Text")
    print("3. Clear Text")
    print("4. Save Text to File")
    print("5. Load Text from File")
    print("6. Quit")
    
    choice = input("Choose an option (1-6): ")

    if choice == '1':  # View the current text
        if text == "":
            print("No text available.")
        else:
            print("\nCurrent Text:")
            print(text)

    elif choice == '2':  # Add text to the current content
        print("Enter text to add (type 'done' to stop):")
        while True:
            new_line = input()
            if new_line == 'done':
                break
            text += new_line + "\n"
        print("Text added successfully!")

    elif choice == '3':  # Clear the text
        text = ""
        print("Text cleared!")

    elif choice == '4':  # Save the text to a file
        filename = input("Enter the filename to save: ")
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text saved to {filename}!")

    elif choice == '5':  # Load text from a file
        filename = input("Enter the filename to load: ")
        try:
            with open(filename, 'r') as file:
                text = file.read()
            print(f"Text loaded from {filename}!")
        except FileNotFoundError:
            print("Error: File not found.")
    
    elif choice == '6':  # Quit the program
        print("Exiting editor...")
        break
    
    else:
        print("Invalid choice, please select a valid option.")

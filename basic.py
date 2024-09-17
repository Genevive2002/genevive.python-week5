# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file named "my_file.txt" and write to it
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line with a number: 123\n")
            file.write("And the third line, which also contains a number: 456\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File creation attempt completed.")

def read_file():
    try:
        # Read the contents of "my_file.txt" and display them
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile contents after initial write:")
            print(content)
    except FileNotFoundError:
        print("File not found: Ensure the file exists before reading.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File reading attempt completed.")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode and add additional lines
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line with text.\n")
            file.write("Appending another line with a number: 789\n")
            file.write("Appending a final line of text.\n")
        print("Content appended successfully.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File appending attempt completed.")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read file again to show appended content

if __name__ == "__main__":
    main()

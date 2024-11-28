# File Read & Write with Error Handling

def file_read_and_write():
    try:
        # Example files: input1.txt and input2.txt
        print("Sample files you can use: 'input1.txt' and 'input2.txt'.")
        
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ").strip()
        
        # Try to open and read the input file
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        print("\nOriginal Content:")
        print(content)
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Ask for the output filename
        output_filename = input("\nEnter the name of the file to write the modified content: ").strip()
        
        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"\nModified content has been written to '{output_filename}'. 🎉")
    
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' does not exist. Please try again.")
    except PermissionError:
        print(f"\nError: You do not have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Create example files
def create_example_files():
    with open("input1.txt", "w") as file1:
        file1.write("Hello, World!\nWelcome to Python file handling.")
    with open("input2.txt", "w") as file2:
        file2.write("Python makes file handling simple and efficient.\nThis is another example file.")

# Run the setup and the program
create_example_files()
file_read_and_write()

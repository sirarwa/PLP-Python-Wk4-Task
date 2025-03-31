# File Modifier Program
# This program reads a text file, modifies its contents (converts to lowercase),
# and writes the modified version to a new file. It includes error handling
# and user input validation for a robust file processing experience.

def modify_content(content):
    # Modify the content of the file by converting it to lowercase
    return content.lower()

def process_file(input_file, output_file):
    # Process a file by reading its contents, modifying them, and writing to a new file
    try:
        # Read the input file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Convert content to lowercase
        modified_content = modify_content(content)
        
        # Write the modified content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)
            
        print(f"Successfully processed {input_file} and wrote to {output_file}")
        
    except FileNotFoundError:
        # Handle case when the specified input file doesn't exist
        print(f"Error: The file '{input_file}' was not found.")
        print("Please ensure the file exists and try again.")
    except UnicodeDecodeError:
        # Handle case when the file contains characters that can't be decoded with UTF-8
        print(f"Error: The file '{input_file}' contains invalid characters.")
        print("Please make sure the file contains valid text and try again.")
    except Exception as e:
        # Catch any other unexpected errors that might occur during file operations
        print(f"An unexpected error occurred: {str(e)}")
        print("Please try again or contact support if the problem persists.")

def get_valid_filename(prompt):
    # Get a valid filename from the user through command line input
    while True:
        filename = input(prompt).strip()
        if filename:
            return filename
        print("Error: Filename cannot be empty. Please try again.")

def main():
    # Main program entry point that handles user interaction and file processing
    # Display welcome message and program description
    print("Welcome to the File Modifier Program!")
    print("This program reads the file, converts its contents to lowercase, and saves it to a new file.")
    
    # Get input filename from user
    input_file = get_valid_filename("\nEnter the name of the file to read (e.g., hotel.text): ")
    
    # Get output filename from user
    output_file = get_valid_filename("Enter the name of the output file (e.g., output.text): ")
    
    # Process the file
    process_file(input_file, output_file)

if __name__ == "__main__":
    main() 
def process_file(input_filename, output_filename):
    try:
        # Try to open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Count words
        word_count = len(content.split())

        # Convert text to uppercase
        processed_text = content.upper()

        # Write processed text + word count to output file
        with open(output_filename, "w") as outfile:
            outfile.write(processed_text)
            outfile.write(f"\n\nWord Count: {word_count}")

        print(f"✅ Success! Processed file saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied while accessing '{input_filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Ask user for a filename
filename = input("Enter the input filename: ")

# Run the function
process_file(filename, "output.txt")

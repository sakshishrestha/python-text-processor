import argparse

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to process a text file."""
    # input_file = input("Enter input file path (default: input.txt): ") or "input.txt"
    # output_file = input("Enter output file path (default: output.txt): ") or "output.txt"
    parser = argparse.ArgumentParser(description='Process text files')
    parser.add_argument('--input', default='input.txt', help='Input file path')
    parser.add_argument('--output', default='output.txt', help='Output file path')
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output

    #read existing content or create new file  
    text = read_file(input_file)
    if text is None: 
        print(f"File '{input_file}' not found. You can create new content.")
        text = ""
    
    #interactive editing
    print("\nCurrent content:")
    print(text if text else "[Empty]")
    new_text = input("\nEnter new text (or press Enter to keep existing): ")
    if new_text:
        text = new_text

    #save new content to input file
    if text:
        try:
            with open(input_file, 'w') as file:
                file.write(text)
            print(f"Content saved to {input_file}")
        except Exception as e:
            print(f"Error saving to {input_file}: {e}")
            return False
    

    #process and write results
    results = process_text(text)
    if results and write_results(results, output_file):
        print(f"Processing complete. Results written to {output_file}")
        return True
    else:
        print("Processing failed.")
        return False
    
    # print("Processing failed.")
    # return False

if __name__ == "__main__":
    main()

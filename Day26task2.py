# Date: 18 Feb 2024
# Title: Day 26 Python task 2
# Author: Sora

def count_words(input_file_path, output_file_path):
    try:
        # read the input file
        with open(input_file_path, 'r') as input_file:
            # word count
            words = input_file.read().split()
            word_count = len(words)

        # write the word count to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(str(word_count))

        print(f"Word count: {word_count} words. Result written to {output_file_path}")

    # error if file input.txt not found
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# specify the input and output file paths
input_file_path = 'input.txt'
output_file_path = 'word_count.txt'

# call the function
count_words(input_file_path, output_file_path)
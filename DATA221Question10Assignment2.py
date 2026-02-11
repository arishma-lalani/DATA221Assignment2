# Question 10

def find_lines_containing(filename, keyword):
    # Returns a list of (line_number, line_text)for the lines that contain the keyword
    matching_lines = []  # Create an empty list to store tuples of (line_number, line_text)

    # Open the file in read mode
    with open(filename, "r", encoding="utf-8") as text_file:
        # Read all lines
        all_lines_in_file = text_file.readlines()

        # Go through each line with its index
        for line_index, line_text in enumerate(all_lines_in_file):
            # Check if the keyword is in the line (case-insensitive)
            if keyword.lower() in line_text.lower():  # Because the keyword is case-sensitive
                matching_lines.append((line_index + 1, line_text.rstrip("\n")))  # Store the text and the line number

    return matching_lines


# Test it!
text_file_to_search = "sample-file.txt"
search_keyword = "lorem"

# Call the function
matching_lines_found = find_lines_containing(text_file_to_search, search_keyword)

# Print the results
print(f"Number of lines containing '{search_keyword}': {len(matching_lines_found)}\n")

# Print the first 3 matching lines
print("First 3 matching lines:")
for line_info in matching_lines_found[:3]:
    line_number, line_text = line_info
    print(f"Line {line_number}: {line_text}")

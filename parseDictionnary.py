def extract_words_from_file(file_path):
    words_array = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                words_array.extend(words)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return words_array

# For TEST
# file_path = "Dictionnary.txt"
# words_array = extract_words_from_file(file_path)
# print("Words extracted from the file:")
# print(words_array)
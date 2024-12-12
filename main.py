def main():
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    word_count = 0
    for word in file_contents.split():
        word_count += 1
    return word_count

def count_chars(file_contents):
    char_count = {}
    for char in file_contents.lower():
        if char in char_count and char.isalpha():
            char_count[char] += 1
        elif char.isalpha():
            char_count[char] = 1
    return char_count

file_name = "books/frankenstein.txt"
char_analysis = []

for char, count in sorted(count_chars(main()).items(), key=lambda item: item[1], reverse=True):
    char_analysis.append(f"The {char} character was found {count} times")


print(
    f"--- Begin report of {file_name} --- \n"
    + f"{count_words(main())} words found in the document \n"
    + "\n".join(char_analysis)
    + "\n" + "--- End report ---"
)

# learnings:
# do not concatenate the print function if you want to embed a for condition in it - 
# i.e print('\n'.join([f"The '{char}' character was found {count} times" for char, count in sorted(count_chars(main()).items(), key=lambda item: item[1], reverse=True)]))
# should do the same as the for loop -> char_analysis var

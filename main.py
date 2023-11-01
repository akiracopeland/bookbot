with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    words = file_contents.split(" ")
    
    counter = 0
    for word in words:
        counter += 1

    

    lower_file_contents = file_contents.lower()

    letter_dict = {}

    for letter in lower_file_contents:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1


    print("--- Begin report of books/frankenstein.txt ---")

    print(f"{counter} words found in the document")

    sorted_letters = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))

    for letter, number in sorted_letters.items():
        if letter.isalpha():
            print(f"The {letter} character was found {number} times")
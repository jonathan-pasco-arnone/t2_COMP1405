""" Searching files program """

# Created by: Jonathan Pasco-Arnone
# Created on: September 2023

import linecache

def main():
    """ The main function of the program """
    search_word = input("Please enter a search word for the files:\n")
    line_number = 1 # Starting number of the pages.txt files lines
    # Holds the frequency of a word in each file
    # (ex: [1, 5, 3, 6] in which file one has the word once, file 2 has the word five times and so on)
    file_frequency = []
    total_word_frequency = []
    while linecache.getline("pages.txt", line_number) != "":
        # The following 3 lines are for removing the "\n" from the end
        # of the file name the linecache generates
        current_file = list(linecache.getline("pages.txt", line_number))
        current_file.pop()
        current_file = "".join(current_file)

        file_line_number = 1
        file_frequency.append(0)
        while linecache.getline(current_file, file_line_number) != "":
            if linecache.getline(current_file, file_line_number) == (search_word + "\n"):
                file_frequency[line_number - 1] += 1
            file_line_number += 1
        total_word_frequency.append(file_line_number) # records the amount of lines in the file
        line_number += 1
    
    # Finds the highest value and index
    index = 0
    current_highest = 0
    current_highest_index = 0
    for value in file_frequency:
        if value > current_highest:
            current_highest = value
            current_highest_index = index
        index += 1
    
    # The following code block

    print("Max Page (Count): N-{}.txt".format(current_highest_index))
    print("Max Count: ", current_highest)
    print("Max Page (Ratio): N-{}.txt".format())
    print("Max Ratio: ", )
    
    print("The total times the word \"", search_word, "\" appears in each file is ", file_frequency)


if __name__ == "__main__":
    main()

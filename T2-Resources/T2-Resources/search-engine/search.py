""" Searching files program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

# This is so the file does not close immediately after completing the code
from time import sleep
import linecache

def main():
    """ The main function of the program """
    search_word = input("Please enter a search word for the files:\n")
    line_number = 1 # Starting number of the pages.txt files lines
    # Holds the frequency of a word in each file
    # (ex: [1, 5, 3, 6] in which file one has the word once,
    # file 2 has the word five times and so on)
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
        # Records the amount of lines in the file with the -1 because
        # the previous while loop continued until it reached its peak
        total_word_frequency.append(file_line_number - 1)
        line_number += 1

    # Finds the highest value and its index
    # along with the highest ratio and its index
    index = 0
    ratio = 0
    highest_value = 0
    highest_value_index = 0
    highest_ratio = 0
    highest_ratio_index = 0
    for value in file_frequency:
        ratio = value / total_word_frequency[index]
        if ratio > highest_ratio:
            highest_ratio = ratio
            highest_ratio_index = index
        if value > highest_value:
            highest_value = value
            highest_value_index = index
        index += 1

    print("\nMax Page (Count): N-" + str(highest_value_index) +".txt")
    print("Max Count: ", highest_value)
    print("Max Page (Ratio): N-" + str(highest_ratio_index) + ".txt")
    print("Max Ratio: ", highest_ratio)

    sleep(20) # Gives 20 seconds to review answers

if __name__ == "__main__":
    main()

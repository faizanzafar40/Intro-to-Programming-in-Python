from random import shuffle
from utilities import clear_screen, banner_message

# I will begin with only 5 numbers. But it can be changed to anything
begin_with = 5

# This list will store all the words
words = []
for i in range(begin_with):
    word = input("Enter word #" + str(i + 1) + ": ")
    words.append(word)  # add the word at the end of the list

# Loop infinitely
while True:
    failed = False      # variable indicating failure
    clear_screen()
    banner_message("Game begins now!")
    total_word_count = len(words)
    # indexes contain 0, 1, 2...total_word_count
    indexes = list(range(total_word_count))
    # this function does not return anything, but shuffles the values in "indexes" list directly
    shuffle(indexes)
    for i in indexes:
        # Ask for a word
        word = input("Do you remember the word #" + str(i + 1) + "? ")
        if word != words[i]:
            # If wrong, add a new word and make the game even harder
            print("Wrong word! the game just got harder...")
            failed = True       # set the value to true to indicate failure
            new_word = input(
                "Enter a new word (#" + str(total_word_count + 1) + "): ")
            words.append(new_word)
            break
    # if the user didn't fail, remove the last word
    if not failed:
        words.pop()
    # If there is no word left, tell the user that he has won
    if len(words) == 0:
        clear_screen()
        banner_message("Congratulations you win!")
        break

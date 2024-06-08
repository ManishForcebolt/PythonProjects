# TODO: Create a letter using starting_letter.txt
PLACE_HOLDER = "[Name]"
# with open("./Input/Letters/starting_letter2.txt", mode="w") as letter:
#     letter.write("Dear [Name], \nI hope you are in fine health. "
#                  "\nI invite you on my birthday party. \nYour Friend, \nManish")

# with open("./Input/Names/invited_names2.txt", mode="w") as name:
#     name.write("Ajay \nSuraj \nAkshay \nVishal")

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names2.txt") as name_file:
    names = name_file.readlines()

#print(names)

with open("./Input/Letters/starting_letter2.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_to_{striped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

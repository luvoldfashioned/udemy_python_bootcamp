# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you:
# https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you:
# https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you:
# https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
with open("Mail Merge Project Start/Input/Letters/starting_letter.txt")\
        as letters:
    letter_example = letters.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_example.replace(PLACEHOLDER, stripped_name)
        with open(f"Mail Merge Project Start/Output/ReadyToSend/{stripped_name}.txt", mode="w") as letter:
            letter.write(new_letter)

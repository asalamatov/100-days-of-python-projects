# with open('invited_names.txt') as names:
#     names_list = []
#     with open("starting_letter.txt") as letter_file:
#         letter_contents = letter_file.read()
#     for name in names:
#         names_list.append(name)
#     for name in names_list:
#         name = name.strip()
#         new_letter = letter_contents.replace('{name}', name)
#         with open(f"D:/100-Days-of-code-Python/Day_24_Project_-_Mail_Merge/mail_merge/output/ReadyToSend/letter_for_{name}", mode="w") as final_letter:
#             final_letter.write(new_letter)
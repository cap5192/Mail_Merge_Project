file = open("Input/Names/invited_names.txt", "r")
list_of_names = file.read()
names = list_of_names.split("\n")
file.close()

letter = open("Input/Letters/starting_letter.txt", "r")
new_letter = letter.read()

for i in range(len(names)):
    x = new_letter.replace("[name]", names[i])
    current_name = names[i]
    letter_new = open(f"Output/ReadyToSend/letter_for_{current_name}.txt", "w")
    letter_new.write(x)
    print(f"file letter_for_{current_name}.txt created successfully")
    letter_new.close()
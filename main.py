#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file = open("Input/Names/invited_names.txt", "r")
list_of_names = file.read()
names = list_of_names.split("\n")


letter = open("Input/Letters/starting_letter.txt", "r")
new_letter = letter.read()

for i in range(len(names)):
    x = new_letter.replace("[name]", names[i])
    print(x)
    current_name = names[i]
    letter_new = open(f"Output/ReadyToSend/letter_for_{current_name}.txt", "w")
    letter_new.write(x)

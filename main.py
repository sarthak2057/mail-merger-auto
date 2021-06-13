# for reading the names from the file
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
    
#     for reading the templates from the file 
with open("./Input/Letters/starting_letter.txt") as template:
    letter = template.read()
    for name in names:
        invited_name = name.strip("\n")
        send = letter.replace("[name]",invited_name)
        with open(f"./Output/ReadyToSend/letter_for_{invited_name}.txt",mode="w") as card:
             card.write(send)

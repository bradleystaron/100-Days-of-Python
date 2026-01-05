#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
# Read the starting letter template
with open("100_Days_of_Code_Python/Days_22-25/Projects/Day24/Letter Project/Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()
    
# Read the list of invited names
with open("100_Days_of_Code_Python/Days_22-25/Projects/Day24/Letter Project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
# Generate personalized letters for each name
for name in names:
    stripped_name = name.strip()  # Remove any leading/trailing whitespace/newline characters
    personalized_letter = letter_template.replace("[name]", stripped_name)  # Replace placeholder with actual name
    
    # Save the personalized letter to the ReadyToSend folder
    with open(f"100_Days_of_Code_Python/Days_22-25/Projects/Day24/Letter Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as output_file:
        output_file.write(personalized_letter)
        

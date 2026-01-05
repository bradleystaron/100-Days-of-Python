# Read and print the contents of my_file.txt
with open("100_Days_of_Code_Python\Days_22-25\Day24_ActiveExamples\my_file.txt") as file:
    content = file.read()
    print(content)
    
# Append a new line to my_file.txt
with open("100_Days_of_Code_Python\Days_22-25\Day24_ActiveExamples\my_file.txt", "a") as file:
    file.write("\nNew line added to the file.")
    
# Create a new file and write some text to it
with open(r"100_Days_of_Code_Python\Days_22-25\Day24_ActiveExamples\new_file.txt", "w") as file:
    file.write("This is a newly created file.")
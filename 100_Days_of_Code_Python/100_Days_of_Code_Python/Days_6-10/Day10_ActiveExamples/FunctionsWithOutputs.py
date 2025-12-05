
# Function that takes two inputs and formats them to title case

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name("bradley", "STARON")
# print(formatted_string)

# output = len("Bradley")
# print(output)

# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You did not enter inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
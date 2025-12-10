# Classes use pascal case naming convention 
# Which is where the first letter of each word is capitalized without underscores.
class User:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
    #pass        
# pass statement is used as a placeholder for future code.


            # user_1 = User()
            # user_1.id = "001"
            # user_1.name = "Bradley"
            # user_1.username = "brad7701"

            # print(user_1.username)

            # user_2 = User()
            # user_2.id = "002"
            # user_2.name = "Alice"
            # user_2.username = "alice123"

# The code above is prone to errors since we can easily make a typo when assigning attributes.
# In order to prevent this we use constructors.
# A constructor is a special type of method that is called when an object is instantiated.
# In Python the constructor method is always named __init__().

# Now we can create objects with attributes by passing in the values when we create the object.
user_1 = User("001", "Bradley", "brad7701")
user_2 = User("002", "Alice", "alice123")

print(user_1.username)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print(user_1.followers)

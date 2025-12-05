import random   

friends = ["Brandon", "Mitchell", "Stephen", "Tony", "Abdullah"]

# First option to pick from the List, using the choice function within random
random_friend_picked = random.choice(friends)
print(random_friend_picked)

# Second choice takes a random integer and then we can pull that index from the list
random_index = random.randint(0, 4)
print(friends[random_index])
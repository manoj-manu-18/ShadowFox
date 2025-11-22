#Create a list of your friends' names. The list should have at least 5 names Create a list of tuples.
# Each tuple should contain a friend's name and the length of the name.
friends = ["Kajal", "Palak", "Jatin", "Amritpal", "Sahil"]
name = ("Kajal", "Palak", "Jatin", "Amritpal", "Sahil")
friend_lengths = [(name, len(name)) for name in friends]

print(friend_lengths)
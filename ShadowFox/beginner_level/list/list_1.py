justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

#Calculate number of members
print("Number of members:", len(justice_league))

#Batman recruits Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated members:", justice_league)

# Wonder Woman is leader → move to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

# Aquaman and Flash conflict → insert Superman or Green Lantern between them
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Superman")
print(justice_league)

#Replace whole list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

#Sort alphabetically
justice_league.sort()
print("Alphabetically sorted members:", justice_league)
print("New Leader:", justice_league[0])
# cyborg is new leader as list is sorted alphabetically





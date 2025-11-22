Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name1 = input("Enter the Name of the First City: ")
city_name2 = input("Enter the Name of the Second City: ")

if city_name1 in Australia:
    if city_name2 in Australia:
        print("Both Cities are in Australia")
    else:
        print("Both Cities don't belongs to Same Countary")
if city_name1 in UAE:
    if city_name2 in UAE:
        print("Both Cities are in UAE")
    else:
        print("Both Cities don't belongs to Same Countary")
if city_name1 in India:
    if city_name2 in India:
        print("Both Cities are in India")
    else:
        print("Both Cities don't belongs to Same Countary")